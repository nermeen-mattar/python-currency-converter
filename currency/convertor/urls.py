from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('currency/', views.get_exchange, name="get_exchange"),

]
