from django.urls import path
from . import views

urlpatterns = [
    path('test',views.blog_form_view),
    path('register/',views.register_form_view),
    path('signin/',views.login_form_view),
    path('contact/', views.contact_us_view),
]