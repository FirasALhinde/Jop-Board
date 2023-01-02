from django.urls import path
from . import views
urlpatterns = [
    path('',views.jop_list,name='jop_list'),
    path('<int:id>/',views.jop_detail,name='jop_detail'),
]
