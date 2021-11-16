from django.urls import path
from . import views

urlpatterns = [
    path('actor/', views.ActorList.as_view()),
    path('', views.Actor_view),
]