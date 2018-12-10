from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError



class Match(models.Model):
    body = models.TextField()
    team1 = models.CharField(max_length=60)
    team2 = models.CharField(max_length=60)
    active = models.BooleanField(default=True)



    def __str__(self):
        return 'Event [ {} Vs {} ]  Active = {}'.format(self.team1, self.team2, self.active)

    class Meta:
        verbose_name = 'Event (2 Field)'
        verbose_name_plural = 'Event (2 Fields)'


class Match2(models.Model):
    body = models.TextField()
    team1 = models.CharField(max_length=60)
    active = models.BooleanField(default=True)

    def __str__(self):
        return 'Event [ {} ]  Active = {}'.format(self.team1, self.active)


    class Meta:
        verbose_name = 'Event (1 Field)'
        verbose_name_plural = 'Event (1 Fields)'


class Rating(models.Model):
    user = models.CharField(max_length=32, unique=True)
    score_1 = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    score_2 = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '{} :  {} - {}'.format(self.user, self.score_1, self.score_2)

    class Meta:
        verbose_name = 'Result (2 Field)'
        verbose_name_plural = 'Result (2 Fields)'


class Rating2(models.Model):
    user = models.CharField(max_length=32, unique=True)
    score_1 = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} :  {} '.format(self.user, self.score_1)

    class Meta:
        verbose_name = 'Result (1 Field)'
        verbose_name_plural = 'Result (1 Fields)'


class Rules(models.Model):
    body = models.TextField()
    active = models.BooleanField(default=True)
