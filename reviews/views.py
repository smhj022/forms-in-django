from typing import Any

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView

from .form import ReviewForm
from .models import Reviews

# Create your views here.

# this approach is know as class based views


class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, "reviews/reviews.html", {
            "form": form
        })

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank_you")
        return render(request, "reviews/reviews.html", {
            "form": form
        })


# Templates rendering way 1

# class ThankyouView(View):

#     def get(self, request):
#         return render(request, "reviews/thank_you.html")

# Templates rendering way 2 : template rendering

class ThankyouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works"
        return context


# format to use list views
class ReviewListView(ListView):
    template_name = "reviews/reviews_list.html"
    model = Reviews
    # if object name is not define we need to use object_list in templates
    context_object_name = "reviews"

    # Extra: if we want to render a review greater than 4 we can use get queryset method
    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gte=4)
        return data

# METHOD 1: Using template view
class ReviewDetailView(TemplateView):
    template_name = "reviews/review_detail.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        review_id = kwargs["id"]
        review = Reviews.objects.get(id=review_id)
        context["review"] = review
        return context



