from django import forms
from blog.models import Post


class blog_form_for_user(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class contact_us_form(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'name','name':'name', 'placeholder': 'Enter Your Name',
                                      'autofocus': 'autofocus', 'required': True}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'id': 'email', 'name': 'email', 'placeholder': 'Email'}))
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'text', 'name': 'message', 'placeholder': 'Enter Your message here!'}))