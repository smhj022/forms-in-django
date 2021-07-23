from django.urls import path

from . import views

urlpatterns = [
    path("", views.ReviewView.as_view()),
    path("thank_you", views.ThankyouView.as_view()),
    path("reviews_list", views.ReviewListView.as_view()),
    path("reviews_list/<int:id>", views.ReviewDetailView.as_view())
]
