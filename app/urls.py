from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.RatingView.as_view(), name='index'),
    path('done/', views.DoneView.as_view(), name='done'),
    path('result/', views.ResultView.as_view(), name='result'),
]
