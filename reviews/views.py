from django.shortcuts import render

# Create your views here.


def reviews(request):
    if request.method == "POST":
        username = request.POST.get("username")
        return render(request, "reviews/thank_you.html", {
            "name": username
        })
    return render(request, "reviews/reviews.html")