from django.urls import path
from . import views


urlpatterns = [
    path("", views.CreateProfileView.as_view()),
    path("/profile_list", views.ProfilesView.as_view())
] 