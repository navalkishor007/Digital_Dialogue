from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .models import Comment
from taggit.models import Tag
from .forms import CommentForm
from .models import Post
# Create your views here.

def post_list_view(request,tag_slug=None):
    post_list = Post.objects.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        post_list = post_list.filter(tags__in=[tag])
    paginator = Paginator(post_list, 4)
    page_number = request.GET.get('page')
    try:
        post_list = paginator.page(page_number)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_page)
    return render(request, 'blog/post_list.html', {'post_list': post_list})


def post_detail_view(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day = day)
    comments = post.comments.filter(active=True)
    csubmit = False
    if request.method== 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            # name = form.name()
            # print(name)
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            csubmit = True

    else:
        form = CommentForm()
    return render(request, 'blog/post_detail.html', {'post': post, 'form': form, 'comments': comments, 'csubmit': csubmit})


# sending mail functionality
from django.core.mail import send_mail
from .forms import EmailSendForm


def mail_send_view(request, id):
    post = get_object_or_404(Post, id=id, status='published')
    sent = False
    if request.method =='POST':
        form = EmailSendForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject ='{}({}) recommends you to read"{}"'.format(cd['name'], cd['email'], post.title)
            post_url = request.build_absolute_uri(post.get_absolute_url())
            message = 'Read Post At:\n {} \n\n{}\'s comments:\n{}'.format(post_url, cd['name'], cd['comments'])

            send_mail(subject, message, 'durga@blog.com', [cd['to']])
            sent = True
    else:
        form = EmailSendForm()
    return render(request, 'blog/shrebymail.html', {'form': form, 'post': post, 'sent': sent})

