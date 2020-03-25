from django.shortcuts import render, get_object_or_404
from .models import Topic, Post, Comment

# topic views
def topic_list(request):
    topics = Topic.published.all()
    return render(request, 
                  'forum/topic/list.html',
                  {'topics': topics})

def topic_detail(request, topic):
    topic = get_object_or_404(Topic, slug=topic,
                                     status='published')
    posts = topic.posts.filter(active=True)
    return render(request,
                  'forum/topic/detail.html',
                  {'topic': topic,
                   'posts': posts})

# post views
def post_list(request):
    posts = Post.published.all()
    return render(request,
                  'forum/post/list.html',
                  {'posts': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    return render(request,
                  'forum/post/detail.html',
                  {'post': post})