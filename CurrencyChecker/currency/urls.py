from currency.views import currency_tracker_view
from django.urls import path,include
from .views import currency_tracker_view
from django.contrib import admin
urlpatterns=[
    path('',currency_tracker_view)
]