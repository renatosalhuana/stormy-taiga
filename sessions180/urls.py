from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("drafts", views.drafts, name="drafts"),
    path("ver/<slug:slug>/", views.day_detail, name='ver'),

]