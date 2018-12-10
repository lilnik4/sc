from django import forms
from .models import Rating, Rating2

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('user', 'score_1', 'score_2')

class Rating2Form(forms.ModelForm):
    class Meta:
        model = Rating2
        fields = ('user', 'score_1')