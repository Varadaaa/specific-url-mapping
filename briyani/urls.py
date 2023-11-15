from briyani.views import *

from django.urls import path

app_name= 'hungery'

urlpatterns=[
    path('chicken/', chicken, name='chicken'),
    path('mutton/', mutton, name='mutton'),
    
]
