from django.db import models


class Game(models.Model):
    team_one= models.CharField(max_length=200)
    team_two= models.CharField(max_length=200)
    pub = models.DateTimeField(auto_now_add=True)



class Score(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    score_one= models.IntegerField(default=0)
    score_two= models.IntegerField(default=0)
    user = models.CharField(max_length=70)