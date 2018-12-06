from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError



class Match(models.Model):
    body = models.TextField()
    team1 = models.CharField(max_length=60)
    team2 = models.CharField(max_length=60)
    active = models.BooleanField(default=True)



    def __str__(self):
        return self.team1 + ' Vs ' + self.team2


class Rating(models.Model):
    user = models.CharField(max_length=32, unique=True)
    score_1 = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    score_2 = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user

