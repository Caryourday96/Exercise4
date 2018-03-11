from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'


#Where the forms are created. This is the form that is used to add more notes to the database