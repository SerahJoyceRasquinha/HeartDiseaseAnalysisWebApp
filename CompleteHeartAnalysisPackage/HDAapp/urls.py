from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),  # Home page
    path('intro/', views.intro_page, name='intro'),
    path('analysis_exang/', views.exang, name='exang'),
    path('analysis_fastbs/', views.fastbs, name='fastbs'),
    path('analysis_chestpain/', views.chestpain, name='chestpain'),
    path('analysis_ecg/', views.restingelectro, name='restingelectro'),
    path('analysis_slope/', views.slope, name='slope'),
    path('analysis_bloodv/', views.bloodves, name='bloodves'),
    path('analysis_restingbp/', views.restingBP, name='restingBP'),
    
]
