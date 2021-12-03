from django import forms
from .models import curriculum


class CurriculumForm(forms.ModelForm):
    class Meta:
        model = curriculum
        exclude = ['foto']

    def __init__(self, *args, **kwargs):
        super(CurriculumForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'