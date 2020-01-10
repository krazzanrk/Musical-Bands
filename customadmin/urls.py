from django.urls import path
from .views import *

app_name='customadmin'

urlpatterns=[

    path('hello',TestView.as_view(),name='customadmin'),
    path('', MusicalBandCreateView.as_view(), name='band_create')
]