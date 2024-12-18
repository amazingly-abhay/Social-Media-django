from django.urls import path
from core.views import *

urlpatterns=[
    path("",home,name='home'),
    path("signup/",signup,name='signup'),
    path("signin/",signin,name='signin'),
    path("profile/",profile,name='profile'),

]