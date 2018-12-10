from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.rating_view, name='index'),
    path('done/', views.DoneView.as_view(), name='done'),
    path('result/', views.result_view, name='result'),
]
