from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .form import BlogPostModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.utils import timezone


# Create your views here.


def blog_list_view(request):
    now = timezone.now()
    qs = BlogPost.objects.published().order_by('-publish_date')

    # if user is authenticated will show all blogs even published or not
    if request.user.is_authenticated:
        qs = BlogPost.objects.filter(user=request.user)
    context = {'blog_list': qs}
    return render(request, 'blog/blog_list.html', context)


@staff_member_required
@login_required
def blog_create_view(request):
    form = BlogPostModelForm(request.POST or None)
    if form.is_valid():
        # when you want to change something
        obj = form.save(commit=False)
        obj.title = form.cleaned_data['title'] + '--'
        obj.save()
        form = BlogPostModelForm()
    context = {'form': form}
    return render(request, 'blog/form.html', context)


def blog_detail_view(request, slug):
    blog = get_object_or_404(BlogPost, slug=slug)
    context = {'blog_detail': blog}
    return render(request, 'blog/blog_detail.html', context)


@staff_member_required()
def blog_update_view(request, slug):
    blog = get_object_or_404(BlogPost, slug=slug)
    # instance is used to get the item on form to edit
    form = BlogPostModelForm(request.POST or None, instance=blog)
    if form.is_valid():
        form.save()
    context = {'form': form, 'title': f'Update title{blog.title}'}
    return render(request, 'form.html', context)


@staff_member_required()
def blog_delete_view(request, slug):
    blog = get_object_or_404(BlogPost, slug=slug)
    if request.method == "POST":
        blog.delete()
        return redirect("blog/list")

    context = {'blog': blog}
    return render(request, 'blog/blog_delete.html', context)


def all_users(request):
    # user = User.objects.all()

    user = {'a', 'b', 'c'}
    context = {'users': user}
    return render(request, 'navbar.html', context)
