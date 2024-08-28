from django import forms
from django.core.exceptions import ValidationError

from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(),
            'text': forms.Textarea(),
        }
        labels = {
            'text': 'add your note:'
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title.strip()) <= 5:
            raise ValidationError('Title is too short')
        return title