from django import  forms
from django.db import models
from .models import *

TEAM_CHOICES = (
    ('*', 'All Teams'),
    ('TVL1', 'TVL1'),
    ('TVL2', 'TVL2'),
    ('TVL3', 'TVL3'),
    ('TVL4', 'TVL4'),
    ('MDX1', 'MDX1'),
    ('MDX2', 'MDX2'),
    ('HIL1', 'HIL1'),
    ('HIL2', 'HIL2'),
    ('HIL3', 'HIL3'),
    ('HIL4', 'HIL4'),
    ('TVJ1', 'TVJ1'),
    ('TVJ2', 'TVJ2'),
    ('TVJ3', 'TVJ3'),
)

TEAM_CHOICES2 = (
    ('*', 'All Teams'),
    ('1', 'TVL1'),
    ('2', 'TVL2'),
    ('3', 'TVL3'),
    ('4', 'TVL4'),    
    ('5', 'MDX1'),
    ('6', 'MDX2'),
    ('7', 'HIL1'),
    ('8', 'HIL2'),
    ('9', 'HIL3'),    
    ('10', 'HIL4'),

)
SEASONS_CHOICES = (
    ('16/17', '16/17'),
    ('15/16', '15/16'),
    ('14/15', '14/15'),
    ('13/14', '13/14'),
    ('12/13', '12/13'),
    ('11/12', '11/12'),
    ('10/11', '10/11'),
    ('09/10', '09/10'),
    ('08/09', '08/09'),
    ('07/08', '07/08'),
    ('06/07', '06/07'),
    ('05/06', '05/06'),
    ('04/05', '04/05'),
    ('03/04', '03/04'),
    ('02/03', '02/03'),
    ('01/02', '01/02'),
    ('00/01', '00/01'),
    ('99/00', '99/00'),
    ('98/99', '98/99'),
    ('97/98', '97/98'),
    ('96/97', '96/97'),
    ('95/96', '95/96'),
    ('94/95', '94/95'),
    ('93/94', '93/94'),
    ('92/93', '92/93'),
    ('91/92', '91/92'),
    ('90/91', '90/91'),   
    
)

class FixtureForm(forms.Form):
    team = forms.ChoiceField(choices=TEAM_CHOICES)
    season = forms.ChoiceField(choices=SEASONS_CHOICES)

class Contact2Form(forms.Form):
    team = forms.ChoiceField(choices=TEAM_CHOICES2)
    season = forms.ChoiceField(choices=SEASONS_CHOICES)
    opponent_team = forms.ModelChoiceField(Team.objects.all())
