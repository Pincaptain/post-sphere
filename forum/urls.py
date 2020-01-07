from django.urls import path

from .views import (
    CategoryListView,
    CategoryDetailView,
    ThreadDetailView,
    PostDetailView,
    RuleDetailView,
    ThreadCreateView,
    PostCreateView,
    CommentCreateView,
    ThreadDeleteView,
    PostDeleteView,
    CommentDeleteView,
    ThreadUpdateView,
    PostUpdateView,
    CommentUpdateView,
)

urlpatterns = [
    path('', CategoryListView.as_view(), name='forum_category_list'),
    path('categories/<pk>/', CategoryDetailView.as_view(), name='forum_category_detail'),
    path('threads/<pk>/update/', ThreadUpdateView.as_view(), name='forum_thread_update'),
    path('threads/<pk>/delete/', ThreadDeleteView.as_view(), name='forum_thread_delete'),
    path('threads/<pk>/create/', ThreadCreateView.as_view(), name='forum_thread_create'),
    path('threads/<pk>/', ThreadDetailView.as_view(), name='forum_thread_detail'),
    path('posts/<pk>/update/', PostUpdateView.as_view(), name='forum_post_update'),
    path('posts/<pk>/delete/', PostDeleteView.as_view(), name='forum_post_delete'),
    path('posts/<pk>/create/', PostCreateView.as_view(), name='forum_post_create'),
    path('posts/<pk>/', PostDetailView.as_view(), name='forum_post_detail'),
    path('comments/<pk>/update/', CommentUpdateView.as_view(), name='forum_comment_update'),
    path('comments/<pk>/delete/', CommentDeleteView.as_view(), name='forum_comment_delete'),
    path('comments/<pk>/create/', CommentCreateView.as_view(), name='forum_comment_create'),
    path('rules/<pk>/', RuleDetailView.as_view(), name='forum_rule_detail'),
]
