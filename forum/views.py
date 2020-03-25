from django.shortcuts import render, get_object_or_404
from .models import Topic, Post, Comment
from .forms import PostForm, CommentForm

# topic views
def topic_list(request):
    topics = Topic.published.all()
    return render(request, 
                  'forum/topic/list.html',
                  {'topics': topics})

def topic_detail(request, topic):
    topic = get_object_or_404(Topic, slug=topic,
                                     status='published')
    
    # List of active posts for this topic
    posts = topic.posts.filter(active=True)

    new_post = None

    if request.method == 'POST':
        # A post was posted
        post_form = PostForm(data=request.POST)
        if post_form.is_valid():
            # Create Post object but don't save to DB yet
            new_post = post_form.save(commit=False)
            # Assign current topic to the post
            new_post.topic = topic
            # Save post to DB
            new_post.save()
    else:
        post_form = PostForm()

    return render(request,
                  'forum/topic/detail.html',
                  {'topic': topic,
                   'posts': posts,
                   'new_post': new_post,
                   'post_form': post_form})

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