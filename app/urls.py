from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.RatingView.as_view(), name='index')
]
