from django.shortcuts import render

from .form import ReviewForm

# Create your views here.


def reviews(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            # .cleaned_form is uesd get the form data in dictionary
            name = form.cleaned_data["username"]
            return render(request, "reviews/thank_you.html", {
                "name": name
            })
    else:
        form = ReviewForm()
    return render(request, "reviews/reviews.html", {
        "form": form
    })
