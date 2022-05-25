from enum import unique
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
# Create your views here.
from django.views.generic import FormView
from surveys.forms import SurveyForm
from collections import Counter

from surveys.models import Survey

class SurveyFillView(TemplateView, FormView):
    success_url = reverse_lazy('filled_success')
    template_name = "survey_form.html"

    def get_form_class(self):
        return SurveyForm

    def form_valid(self, form):
        form.instance.save()
        return super(SurveyFillView, self).form_valid(form)


    def get_context_data(self, **kwargs):
        context = super(SurveyFillView, self).get_context_data(**kwargs)
        return context


class SurveyFilledView(TemplateView):
    template_name = "survey_filled.html"

    def get_context_data(self, **kwargs):
        context = super(SurveyFilledView, self).get_context_data(**kwargs)
        return context


def unique_counter(queryset,field_name):
    return Counter([getattr(i, field_name) for i in queryset])

class SurveyStatsView(TemplateView):
    template_name = "survey_stats.html"

    def get_context_data(self, **kwargs):
        context = super(SurveyStatsView, self).get_context_data(**kwargs)

        survey_answers = Survey.objects.all()
        context['unique_sample_string'] = unique_counter(survey_answers, 'question_16')
        context['bool_distribution'] = unique_counter(survey_answers, 'question_2')
        context['total_count'] = survey_answers.count()
        return context

