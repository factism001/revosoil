from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('soildata/', views.soil_data, name='soil_data'),
    path('analysis/', views.soil_properties_analysis, name='soil_properties_analysis'),
    path('chat/', views.chat_view, name='chat_view'),
]
