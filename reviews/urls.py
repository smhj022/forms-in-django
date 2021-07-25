from django.urls import path

from . import views

urlpatterns = [
    path("", views.ReviewView.as_view()),
    path("thank_you", views.ThankyouView.as_view()),
    path("reviews", views.ReviewListView.as_view()),
    path("reviews/<int:id>", views.ReviewDetailView.as_view(), name="reviews_detail")
]
