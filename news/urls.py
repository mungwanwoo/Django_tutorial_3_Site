
from django.contrib import admin
from django.urls import path
from . import views

app_name="news"

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:company_id>/',views.detail,name='detail'),
    
]