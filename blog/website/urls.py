from django.urls import path, include
from .views import tosh


urlpatterns = [
    path('', tosh),
    

]
