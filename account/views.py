from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import CustomLoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class AdminDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'admin/admin_dashboard.html'
    
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_superuser:  # Admin user check
                return redirect('admin_dashboard')
            elif user.role == 'student':
                return redirect('student_dashboard')
            elif user.role == 'staff':
                return redirect('staff_dashboard')
            # Add other role checks as necessary
    else:
        form = AuthenticationForm()

    return render(request, 'account/login.html', {'form': form})



@login_required
def student_dashboard(request):
    return render(request, 'student_dashboard.html')

@login_required
def staff_dashboard(request):
    return render(request, 'staff_dashboard.html')

@login_required
def hod_dashboard(request):
    return render(request, 'hod_dashboard.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import CustomUser  # assuming you're using this model
from django.db import IntegrityError

@login_required
def create_student(request):
    if request.method == 'POST':
        # Get form data
        username = request.POST['username']
        password = request.POST['password']
        full_name = request.POST['full_name']
        department = request.POST['department']
        email = request.POST['email']
        phone = request.POST['phone']
        blood_group = request.POST['blood_group']
        gender = request.POST['gender']

        try:
            # Create new student user
            student = CustomUser.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=full_name.split(' ')[0],  # First name (splitting full name)
                last_name=' '.join(full_name.split(' ')[1:]),  # Last name
                role='student'
            )
            student.department = department
            student.phone = phone
            student.blood_group = blood_group
            student.gender = gender
            student.save()

            messages.success(request, "Student created successfully!")
            return redirect('student_list')  # Adjust to your student listing view

        except IntegrityError:
            messages.error(request, "Username already exists.")
    
    return render(request, 'create/create_student.html')
