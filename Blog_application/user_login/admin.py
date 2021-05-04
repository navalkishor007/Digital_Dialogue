from django.contrib import admin
from .models import contact_model,registered_users
# Register your models here.


class ModelAdmin(admin.ModelAdmin):
    list_display = ['name_of_sender', 'email_of_sender', 'message_of_sender']

class UserAdmin(admin.ModelAdmin):
    list_display = ['user_first_name','email']

admin.site.register(contact_model,ModelAdmin)
admin.site.register(registered_users,UserAdmin)

