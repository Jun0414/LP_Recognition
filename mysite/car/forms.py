from django import forms
from .models import License

# class LPForm(forms.ModelForm):
#     class Meta:
#         model = LP
#         fields = ['LP_name', 'LP_img']


# class lpForm(forms.ModelForm):
#     class Meta:
#         model = lpForm
#         fields = ['LP_name', 'LP_img']


class LicenseForm(forms.ModelForm):
    class Meta:
        model = License
        fields = ('LP_name', 'LP_img')