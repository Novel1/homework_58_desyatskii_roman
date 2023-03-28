from django import forms
from django.core.exceptions import ValidationError
from webapp.models import Task


class TaskForm(forms.ModelForm):
    summary = forms.CharField(max_length=30)

    class Meta:

        model = Task
        fields = ('summary', 'description', 'status', 'type')
        labels = {
            'summary': 'Краткое описание',
            'description': 'Описание',
            'status': 'Cтатус',
            'type': 'Тип',
        }

    def clean_summary(self):
        summary = self.cleaned_data.get('summary')
        if len(summary) < 2:
            raise ValidationError('Заголовок должен быть длиннее 1 символа')
        return summary

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) < 10:
            raise ValidationError('Описание должено быть длиннее 10 символов')
        elif len(description) > 150:
            raise ValidationError('Описание должено быть меньше 150 символов')
        return description