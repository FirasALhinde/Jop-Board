from django import forms
from .models import Apply,Jop
class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields ='__all__'
        exclude = ('jop','created_at')


class JopForm(forms.ModelForm):
    class Meta:
        model = Jop
        fields = '__all__'
        exclude =('slug','owner')