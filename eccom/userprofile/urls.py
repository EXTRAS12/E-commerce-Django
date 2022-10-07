from django.contrib.auth import views as auth_views
from django.urls import path

from . import views


urlpatterns = [
    path('myaccount/', views.myaccount, name='myaccount'),
    path('login/', auth_views.LoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('vendors/<int:pk>/', views.vendor_detail, name='vendor_detail'),
]