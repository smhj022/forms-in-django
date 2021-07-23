from django.shortcuts import render
from .form import ReviewForm
from django.views import View

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
            data = form.cleaned_data
            name = data["username"]
            form.save()
            return render(request, "reviews/thank_you.html", {
                "name": name
            })
        return render(request, "reviews/reviews.html", {
            "form": form
        })
