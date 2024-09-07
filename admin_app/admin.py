import csv
from django.contrib import admin
from django import forms
from django.urls import path
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from account.models import CustomUser  # Import CustomUser

# Form to upload the CSV file
class CSVImportForm(forms.Form):
    csv_file = forms.FileField()

@admin.register(CustomUser)  # Register CustomUser instead of User
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'role', 'is_active')

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('import-csv/', self.admin_site.admin_view(self.import_csv), name='import-csv'),
        ]
        return custom_urls + urls

    def import_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]
            reader = csv.reader(csv_file)
            for row in reader:
                username, email, role = row[0], row[1], row[2]
                # Create user using the imported data
                CustomUser.objects.create(
                    username=username,
                    email=email,
                    password=make_password('defaultpassword'),  # Set default password
                    role=role
                )
            self.message_user(request, "Users imported successfully!")
            return HttpResponseRedirect("../")
        
        # Render the CSV upload form
        form = CSVImportForm()
        return render(request, "admin/csv_form.html", {"form": form})
