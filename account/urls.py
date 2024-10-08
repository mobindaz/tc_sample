# In account/urls.py

from django.urls import path
from .views import AdminDashboardView  # Ensure this import is correct
from . import views
urlpatterns = [
    path('admin_dashboard/', AdminDashboardView.as_view(), name='admin_dashboard'),
    # Other URL patterns for this app
    path('create_student/',views.create_student,name="create_student")
]
