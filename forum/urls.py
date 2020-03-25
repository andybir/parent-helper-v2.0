from django.urls import path
from . import views

app_name = 'forum'

urlpatterns = [
    # topic views
    path('', views.topic_list, name='topic_list'),
    path('<slug:topic>/', views.topic_detail, name='topic_detail'),

    # post views
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>',
         views.post_detail, name='post_detail'),
]