from django.db import models
from django.contrib.auth.models import User
import uuid

class Parcel(models.Model):
    TRACKING_STATUS = [
        ('PENDING', 'Pending'),
        ('IN_TRANSIT', 'In Transit'),
        ('DELIVERED', 'Delivered'),
        ('CANCELED', 'Canceled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # parcel_id = models.CharField(max_length=100, unique=True)
    parcel_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    sender_name = models.CharField(max_length=100)
    receiver_name = models.CharField(max_length=100)
    receiver_address = models.TextField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)  # For parcel weight
    status = models.CharField(max_length=20, choices=TRACKING_STATUS, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.parcel_id} - {self.receiver_name}"

class StatusUpdate(models.Model):
    parcel = models.ForeignKey(Parcel, related_name="status_updates", on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=Parcel.TRACKING_STATUS)
    location = models.CharField(max_length=100)
    update_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.parcel.parcel_id} - {self.status} at {self.location}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"
