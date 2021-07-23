from django import forms


class ReviewForm(forms.Form):
    username = forms.CharField(label="Your Name",max_length=50, error_messages={
        "required": "This field is required",
        "max_length": "you exceeds max length"
    })
    review_text = forms.CharField(label="Your Review", widget=forms.Textarea)
    rating = forms.IntegerField(label="Rating", min_value=1, max_value=5)

