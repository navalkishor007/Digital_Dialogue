from django.contrib import admin
from .models import contact_model
# Register your models here.


class ModelAdmin(admin.ModelAdmin):
    list_display = ['name_of_sender', 'email_of_sender', 'message_of_sender']

admin.site.register(contact_model,ModelAdmin)
