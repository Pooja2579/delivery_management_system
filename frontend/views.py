# from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Parcel, StatusUpdate, Profile
from .forms import ParcelForm, StatusUpdateForm  # Create forms for these models
import pandas as pd
import numpy as np
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def home(request):
    parcels = Parcel.objects.all()
    
    # Example data processing for dashboard
    total_parcels = parcels.count()
    pending_parcels = parcels.filter(status='PENDING').count()
    delivered_parcels = parcels.filter(status='DELIVERED').count()
    in_transit_parcels = parcels.filter(status='IN_TRANSIT').count()
    
    # Create data for charts (example)
    status_counts = {
        'Pending': pending_parcels,
        'Delivered': delivered_parcels,
        'In Transit': in_transit_parcels,
        'Canceled': parcels.filter(status='CANCELED').count()
    }

    return render(request, 'frontend/index.html', {
        'total_parcels': total_parcels,
        'status_counts': status_counts
    })

@login_required
def add_parcel(request):
    if request.method == 'POST':
        form = ParcelForm(request.POST)
        if form.is_valid():
            parcel = form.save(commit=False)
            parcel.user = request.user  # Assign the current user
            parcel.save()
            return redirect('home')
    else:
        form = ParcelForm()
    return render(request, 'frontend/add_parcel.html', {'form': form})

@login_required
def track_parcel(request):
    parcel = None
    status_updates = []
    if request.method == 'POST':
        parcel_id = request.POST.get('parcel_id')
        if parcel_id:
            try:
                parcel = Parcel.objects.get(parcel_id=parcel_id)
                status_updates = parcel.status_updates.all()
            except Parcel.DoesNotExist:
                messages.error(request, 'Parcel not found.')
        else:
            messages.error(request, 'Please enter a Parcel ID.')
    return render(request, 'frontend/track_parcel.html', {'parcel': parcel, 'status_updates': status_updates})


@login_required
def generate_report(request):
    # Fetch data from the database
    parcels = Parcel.objects.all().values('parcel_id', 'sender_name', 'receiver_name', 'receiver_address', 'weight', 'status', 'created_at', 'updated_at')
    # use pandas
    df = pd.DataFrame(list(parcels)) 

    # Generate CSV response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="parcel_report.csv"'
    
    df.to_csv(response, index=False)

    return response

@login_required
def list_parcels(request):
    parcels = Parcel.objects.all()
    return render(request, 'frontend/list_parcels.html', {'parcels': parcels})

@login_required
def update_parcel(request, parcel_id):
    parcel = get_object_or_404(Parcel, parcel_id=parcel_id)
    if request.method == 'POST':
        form = ParcelForm(request.POST, instance=parcel)
        if form.is_valid():
            form.save()
            return redirect('list_parcels')
    else:
        form = ParcelForm(instance=parcel)
    return render(request, 'frontend/update_parcel.html', {'form': form, 'parcel': parcel})


@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'frontend/profile.html', {'profile': profile})


