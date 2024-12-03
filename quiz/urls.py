from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # Dashboard view
    path('quiz/', views.take_quiz, name='take_quiz'),  # Quiz page
    path('submit/', views.submit_answer, name='submit_answer'),  # Submit answer
]