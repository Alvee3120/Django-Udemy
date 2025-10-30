from django.urls import path
from . import views

urlpatterns = [

   
    path('index',views.myfunction),
    path('<int:month>', views.monthly_challanges_by_number),
    path('<str:month>', views.monthly_challanges, name = "monthly-challanges"),
]