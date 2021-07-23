from django import forms
from .models import Reviews

# class ReviewForm(forms.Form):
#     username = forms.CharField(label="Your Name",max_length=50, error_messages={
#         "required": "This field is required",
#         "max_length": "You exceeds max length"
#     })
#     review_text = forms.CharField(label="Your Review", widget=forms.Textarea)
#     rating = forms.IntegerField(label="Rating", min_value=1, max_value=5)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = "__all__"
        # or fields = ["username", "review", "rating"] fields that we want to include in forms
        labels = {
            "username": "Your Name",
            "review_text": "Review",
            "rating": "Rating"
        }
        error_message = {
            "username": {
                "required": "This field is required",
                "max_length": "You exceeds max length"
            }
            }
        
