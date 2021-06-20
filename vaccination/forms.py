from django import forms
from vaccination.models import User_Base



class UserBaseForm(forms.ModelForm):

    class Meta:
        model = User_Base
        fields = '__all__'



    