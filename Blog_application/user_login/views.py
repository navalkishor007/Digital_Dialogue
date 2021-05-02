from django.shortcuts import render,redirect
from django.http import HttpResponse
from . forms import blog_form_for_user,contact_us_form
from blog.models import Post
from .models import contact_model
# Create your views here.


def blog_form_view(request):
    obj = Post()
    form = blog_form_for_user
    if request.method == 'POST':
        form = blog_form_for_user(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print('submited')
    return render(request,'blog/blog_form.html',{'form':form})

def register_form_view(request):
    return render(request, 'blog/register.html')

def login_form_view(request):
    return render(request, 'blog/login.html')

def contact_us_view(request):
    obj = contact_us_form()
    if request.method == 'POST':
        # m_obj = contact_model
        obj = contact_us_form(request.POST)
        if obj.is_valid():
            m_obj = contact_model()
            m_obj.name_of_sender = obj.cleaned_data['name']
            m_obj.email_of_sender = obj.cleaned_data['email']
            m_obj.message_of_sender = obj.cleaned_data['message']
            m_obj.save()
            return redirect('/')
    return render(request, 'blog/contact_us.html', {'obj': obj})