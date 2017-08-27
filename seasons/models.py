from django.db import models

# Create your models here.
MATCH_RESULT_CHOICES = (
        ('W', 'Won'),
        ('L', 'Lost'),
        ('D', 'Draw'),
    )
    
BOARD_CHOICES = (
        ('O', 'Odd'),
        ('E', 'Even'),
        ('U', 'Unknown'),
    )
TEAM_CHOICES = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
        ('G', 'G'),
    )

VENUE_CHOICES = (
        ('H', 'Home'),
        ('A', 'Away'),
    )
BOARD_RESULT_CHOICES = (
        (2, '1-0'),
        (0, '0.5-0.5'),
        (1, '0-1'),
        (-1, 'Adjourned'),
        (-2, 'Adjudicated'),
    )

class Season(models.Model):
    name = models.CharField(max_length=5)
    fullname = models.CharField(max_length=9) 
    
    def __str__(self):
        return self.name

    class Admin:
        pass

class Player(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=35)
    initials = models.CharField(max_length=5)
    ECF_reg = models.CharField(max_length=10,null=True)
    active = models.PositiveSmallIntegerField(null=True, blank=True)
    gradelist = models.ManyToManyField(Season, through='Grade')
    
    class Meta:
        ordering = ('last_name', 'first_name')
	
    def __str__(self):
        return '%s, %s' % (self.last_name,self.first_name)

    class Admin:
        pass

class League(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=3)

    def __str__(self):
        return self.name

    class Admin:
        pass

class Team(models.Model):
    league = models.ForeignKey(League)
    name = models.CharField(max_length=20)
    number = models.PositiveSmallIntegerField(null=False, blank=False)
    letter = models.CharField(max_length=1)
    code = models.CharField(max_length=20)
    
    def __str__(self):
        return '%s League: %s %s' % (self.league.name,self.name, self.letter)


    class Admin:
        pass

class Boardresult(models.Model):
    homedisplay = models.CharField(max_length=10)
    awaydisplay = models.CharField(max_length=10)
    def __str__(self):
        return '%s' % (self.homedisplay)

    class Admin:
        pass

class MatchType(models.Model):
    matchtype_code = models.CharField(max_length=6)
    matchtype_name = models.CharField(max_length=20)
    
    def __str__(self):
        return '%s' % (self.matchtype_name)

    class Admin:
        pass

class Campaign(models.Model):
    season = models.ForeignKey(Season)
    team = models.ForeignKey(Team)
    captain = models.ForeignKey(Player)
    boards = models.PositiveSmallIntegerField(null=False, blank=False)
    division = models.PositiveSmallIntegerField(null=False, blank=False)

    def __str__(self):
        return '%s: %s - %s %s' % (self.season.name,self.team.league.name,self.team.name, self.team.letter)

    class Admin:
        pass

class Grade(models.Model):
    season = models.ForeignKey(Season)
    player = models.ForeignKey(Player)
    grade = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return '%s: %s ' %(self.season, self.grade)

    class Admin:
        pass


                		
class Fixture(models.Model):
    campaign = models.ForeignKey(Campaign)
    opponent_club = models.CharField(max_length=50)
    opponent_team = models.CharField(max_length=1)
    matchtype = models.ForeignKey(MatchType)
    venue = models.CharField(max_length=1, choices=VENUE_CHOICES)
    date = models.DateTimeField()
    match_result = models.CharField(max_length=1,null=True, blank=True)
    our_score= models.DecimalField(null=True, blank=True, max_digits=2, decimal_places=1)
    their_score = models.DecimalField(null=True, blank=True, max_digits=2, decimal_places=1)
    white_on  = models.CharField(max_length=1, choices=BOARD_CHOICES,null=True, blank=True)
    captains_headline = models.TextField()
    captains_comment = models.TextField()
    #captains_headline = tinymce_models.HTMLField(null=True, blank=True)
    #captains_comment = tinymce_models.HTMLField(null=True, blank=True)

    def __str__(self):
        #return '%s: %s - %s %s' % (self.Campaign,self.date,self.opponent_club, self.opponent_team)
        return "%s %s: %s%s: %s '%s' (%s)" %(self.campaign.season.name,self.date,self.campaign.team.league.code,self.campaign.team.number,self.opponent_club, self.opponent_team, self.venue)

    class Meta:
        ordering = ['date']

    class Admin:
        pass

class Result(models.Model):
    fixture = models.ForeignKey(Fixture)
    board = models.PositiveSmallIntegerField(null=False, blank=False)
    our_player = models.ForeignKey(Player)
    boardresult = models.ForeignKey(Boardresult)
    opponent_name = models.CharField(max_length=30)
    opponent_grade = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return "%s: %s%s: %s '%s' (%s) Board %s" %(self.fixture.campaign.season.name,self.fixture.campaign.team.league.code,self.fixture.campaign.team.number,self.fixture.opponent_club, self.fixture.opponent_team, self.fixture.venue,self.board)
        

    class Admin:
        pass

