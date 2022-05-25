from django import forms
from datetime import datetime, date
import django
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin.helpers import ActionForm

from surveys.models import Survey

class SurveyForm(forms.ModelForm):
    """
    Form to create and edit template instance. 
    """

    class Meta:
        model = Survey
        fields = '__all__'

        widgets = {
            'question_8': forms.TextInput(attrs={'type': 'range'})
            }