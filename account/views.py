from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import CustomLoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class AdminDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'admin_dashboard.html'
    
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
