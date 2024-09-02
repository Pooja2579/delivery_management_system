from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_parcel, name='add_parcel'),
    path('track/', views.track_parcel, name='track_parcel'),
    path('generate_report/', views.generate_report, name='generate_report'),
    path('list/', views.list_parcels, name='list_parcels'),  # New path for listing parcels
    path('update/<uuid:parcel_id>/', views.update_parcel, name='update_parcel'),  # New path for updating parcels
    path('profile/', views.profile_view, name='profile'),
    

    
]

