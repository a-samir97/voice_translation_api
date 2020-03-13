from django.urls import path, include
from . import views

urlpatterns = [
    path('test/',views.home,name='home'),
    path('',views.index,name='index'),
    path('speech/',views.speech,name='speech'),
]

