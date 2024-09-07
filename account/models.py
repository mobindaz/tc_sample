from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('student', 'Student'),
        ('staff', 'Staff'),
        ('hod', 'HOD'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')

    def __str__(self):
        return self.username

# Student model inheriting from CustomUser
class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='student_profile')
    full_name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    blood_group = models.CharField(max_length=3, choices=[
        ('A+', 'A+'), ('A-', 'A-'), 
        ('B+', 'B+'), ('B-', 'B-'), 
        ('O+', 'O+'), ('O-', 'O-'), 
        ('AB+', 'AB+'), ('AB-', 'AB-')
    ])
    pnr = models.CharField(max_length=20, unique=True)  # Permanent Register Number
    image = models.ImageField(upload_to='student_images/', default='default_avatar.png')
    parent_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=6, choices=[('male', 'Male'), ('female', 'Female')])
    email = models.EmailField()
    passout_year = models.PositiveIntegerField()
    is_complete = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)  # For admin approval of the student profile

    def __str__(self):
        return self.user.username
