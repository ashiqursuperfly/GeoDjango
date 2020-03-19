from django.urls import path
from .views import *
from .consts import ViewConstants

urlpatterns = [
    path('', home, name=ViewConstants.HOME_VIEW_FUNCTION),
] 
