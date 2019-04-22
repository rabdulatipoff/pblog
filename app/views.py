from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q

from django.contrib.auth.models import User
from .models import Post

from .forms import PostForm
from .forms import LoginForm

from .wordstat import word_stats

def post_list(request, username = None):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')
    if username:
        posts = posts.filter(author = User.objects.get(username = username))
    return render(request, 'app/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    wordstat = word_stats(post.text)
    return render(request, 'app/post_detail.html', {'post': post, 'wordstat': wordstat})


def search_posts(request):
    if request.method == 'POST':
        query = request.POST.get('postsearch', None)
        posts = Post.objects.all().filter(Q(title__icontains = query) | Q(text__icontains = query))
        return render(request, 'app/post_list.html', {'posts': posts})


@login_required
def post_new(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit = False)
                post.author = request.user
                post.publish()
                return HttpResponseRedirect(reverse('post_detail', args = (post.pk, )))
        else:
            form = PostForm()

    return render(request, 'app/post_edit.html', {'form': form})

