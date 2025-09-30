from django.urls import path
from . import views

urlpatterns = [
    # Add your URL patterns here later
    # Example: path('', views.index, name='index'),
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('assets/', views.assets, name='assets'),
    path('requests/', views.requests, name='requests'),
    path('review-queue/', views.review_queue, name='review_queue'),
]