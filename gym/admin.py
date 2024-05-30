from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import UserProfile, Trainer, Package, Member, Equipment, Attendance, Feedback, Enquiry

# Define an inline admin descriptor for UserProfile model
# which acts a bit like a singleton
admin.site.register(UserProfile)
admin.site.register(Trainer)
admin.site.register(Package)
admin.site.register(Member)
admin.site.register(Equipment)
admin.site.register(Attendance)
admin.site.register(Feedback)
admin.site.register(Enquiry)
