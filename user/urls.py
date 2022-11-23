from django.urls import path
from . import views
app_name = "user"

urlpatterns = [
    path('signup/', views.Signup.as_view()),
    path('signin/', views.Signin.as_view()),
    path('logout/', views.Logout.as_view()),
    path('checkid/', views.Checkid.as_view()),
    path('modifydpi/', views.ModifyDpi.as_view()),
]