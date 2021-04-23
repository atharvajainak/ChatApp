from django import forms

from .models import Group

class GroupCreationForm(forms.ModelForm):
    group_info = forms.CharField(max_length=300, widget=forms.Textarea, required=False)
    class Meta:
        model = Group
        fields = ['group_name', 'group_info']