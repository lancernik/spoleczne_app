from django.urls import path, include

from surveys.views import *

urlpatterns = [
    path(r'survey_fill/', SurveyFillView.as_view(), name='survey_fill'),
    path(r'filled_success/', SurveyFilledView.as_view(), name='filled_success'),
    path(r'survey_stats/', SurveyStatsView.as_view(), name='survey_stats'),
]
