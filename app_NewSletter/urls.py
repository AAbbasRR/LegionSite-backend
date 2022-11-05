from django.urls import path
from .views import *

app_name = 'newsletters'
urlpatterns = [
    path('api/add/', CreateNewsletterView.as_view()),
    path('list/', ListNewsletterView.as_view(), name="NewSletterlist"),
]
