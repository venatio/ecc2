from django.contrib import admin

# Register your models here.
from .models import Player
from .models import Season
from .models import League
from .models import Fixture
from .models import Campaign
from .models import MatchType
from .models import Result
from .models import Grade
from .models import Team

#admin.site.register(Player)
admin.site.register(Season)
admin.site.register(League)
admin.site.register(Campaign)
#admin.site.register(Fixture)
admin.site.register(MatchType)
#admin.site.register(Result)
#admin.site.register(Grade)
admin.site.register(Team)

class ResultInline(admin.TabularInline):
    model = Result
    extra = 8

class GradeInline(admin.TabularInline):
    model = Grade
    extra = 2
    #ordering = ('-season.fullname',) 
class FixtureAdmin(admin.ModelAdmin):
    fields = ['campaign','date', 'opponent_club','opponent_team','venue','match_result','our_score','their_score', 'white_on',"captains_headline", "captains_comment"]
    js = ('tinymce/jscripts/tine_mce/tiny_mce.js', 'tinymce/jscripts/tine_mce/textarea.js',)
    inlines = [ResultInline]
    ordering = ('-date',)
#class PollAdmin(admin.ModelAdmin):
#    fieldsets = [
#        (None,               {'fields': ['question']}),
#        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#    ]
#    inlines = [ChoiceInline]

class PlayerAdmin(admin.ModelAdmin):
    inlines = [GradeInline]
   
    
admin.site.register(Fixture, FixtureAdmin)
admin.site.register(Player, PlayerAdmin)
