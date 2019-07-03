from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Post
from django.shortcuts import get_object_or_404


class PostListView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class PostDetailView(DetailView):
    template_name = 'pages/post-detail.html'

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Post, id = id_)


def contact(request, *args, **kwargs):
    return render(request, 'pages/contact-us.html')


def about(request, *args, **kwargs):
    return render(request, 'pages/about-us.html')


def fullNews(request, *args, **kwargs):
    return render(request, 'pages/full-news.html')
