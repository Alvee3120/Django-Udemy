from django.urls import path
from . import views

urlpatterns = [

    path('index',views.index),
    path('<str:month>', views.monthly_challenges, name="monthly-challange")
]