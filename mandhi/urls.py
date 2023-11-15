from mandhi.views import *

from django.urls import path

app_name= 'very hungery'

urlpatterns=[
    path('fish/', fish, name='fish'),
    path('rice/', rice, name='rice'),

]