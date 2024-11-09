from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_farmer, name='register_farmer'),
    path('display_farmer_id/<str:farmer_id>/', views.display_farmer_id, name='display_farmer_id'),
    path('farmer_dashboard/<str:farmer_id>/', views.farmer_dashboard, name='farmer_dashboard'),
    path('report_issue/<str:farmer_id>/', views.report_issue, name='report_issue'),
    path('report_harvest/<str:farmer_id>/', views.report_harvest, name='report_harvest'),
    path('report_planting/<str:farmer_id>/', views.report_planting, name='report_planting'),
    path('view_harvests/<str:farmer_id>/', views.view_harvests, name='view_harvests'),
    path('view_plantings/<str:farmer_id>/', views.view_planting_reports, name='view_planting_reports'),
    path('upcoming_events/', views.upcoming_events, name='upcoming_events'),
]
