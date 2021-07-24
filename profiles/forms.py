from django import forms


class ProfileForm(forms.Form):
    user_image = forms.ImageField()
    # to use ImageField we need to install pillow
    # use command python3 -m pip install Pillow
    