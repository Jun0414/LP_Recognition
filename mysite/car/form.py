from django import form
from .models import lpForm

# class LPForm(forms.ModelForm):
#     class Meta:
#         model = LP
#         fields = ['LP_name', 'LP_img']


class lpForm(forms.ModelForm):
    class Meta:
        model = lpForm
        fields = ['LP_name', 'LP_img']