from django.urls import path
from . import views
app_name = "user"

urlpatterns = [
    path('signup/', views.Signup.as_view()),
    path('signin/', views.Signin.as_view()),
]