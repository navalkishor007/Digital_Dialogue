from django.urls import path
from . import views
from django.conf.urls import url,include

urlpatterns = [
    path('login/',views.blog_form_view),
    path('register/',views.register_form_view),
    path('signin/',views.login_form_view),
    path('contact/', views.contact_us_view),
]