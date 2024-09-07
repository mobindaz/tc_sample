from django.contrib import admin
from django.urls import path, include
from account import views as account_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', account_views.login_view, name='login'),  # Redirect root URL to login page
    path('admin/', admin.site.urls),
    path('login/', account_views.login_view, name='login'),
    path('student/dashboard/', account_views.student_dashboard, name='student_dashboard'),
    path('staff/dashboard/', account_views.staff_dashboard, name='staff_dashboard'),
    path('hod/dashboard/', account_views.hod_dashboard, name='hod_dashboard'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('account/', include('account.urls')),
]
