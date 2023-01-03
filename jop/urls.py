from django.urls import path
from . import views

app_name ='jop'

urlpatterns = [
    path('',views.jop_list,name='jop_list'),
    path('<str:slug>',views.jop_detail,name='jop_detail'),
]
