from django.shortcuts import render, get_object_or_404
from .models import Topic, Post, Comment
from .forms import PostForm, CommentForm

# topic views
def topic_list(request):
    topics = Topic.published.all()
    return render(request, 
                  'forum/topic/list.html',
                  {'section': 'topic_list',
                  'topics': topics})

def topic_detail(request, topic):
    topic = get_object_or_404(Topic, slug=topic,
                                     status='published')
                                     #publish__year=year,
                                     #publish__month=month,
                                     #publish__day=day)
    
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
                  {'section': 'topic_list',
                  'topic': topic,
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

    # List of active comments for this post
    comments = post.comments.filter(active=True)

    new_comment = None

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to DB yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save comment to DB
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request,
                  'forum/post/detail.html',
                  {'section': 'topic_list',
                   'post': post,
                   'comments': comments,
                   'new_comment': new_comment,
                   'comment_form': comment_form})