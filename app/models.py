from django.db import models


class Match(models.Model):
    body = models.TextField()
    team1 = models.CharField(max_length=32)
    team2 = models.CharField(max_length=32)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.team1 + ' Vs ' + self.team2


class Rating(models.Model):
    user = models.CharField(max_length=32)
    score_1 = models.IntegerField(default=0)
    score_2 = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user

