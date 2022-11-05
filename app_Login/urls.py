from django.contrib.auth import views
from django.urls import path

app_name = 'login'
urlpatterns = [
    path('', views.LoginView.as_view(template_name="login/login.html"), name='login'),
]
