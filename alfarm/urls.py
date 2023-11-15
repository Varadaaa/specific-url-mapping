from alfarm.views import *
from django.urls import path

app_name='tasty'

urlpatterns = [
 path('peper/', peper, name='peper'),
 path('periperi', periperi, name='periperi'),
]