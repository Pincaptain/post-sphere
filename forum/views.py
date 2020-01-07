from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse

from .models import Category, Thread, Post, Rule, Comment
from .forms import ThreadForm, PostForm, CommentForm


class CategoryListView(ListView):
    model = Category


class CategoryDetailView(DetailView):
    model = Category


class ThreadDetailView(DetailView):
    model = Thread


class ThreadCreateView(LoginRequiredMixin, CreateView):
    model = Thread
    form_class = ThreadForm
    login_url = reverse_lazy('accounts_login')

    def form_valid(self, form):
        form.instance.admin = self.request.user
        form.instance.category = get_object_or_404(Category, pk=self.kwargs['pk'])

        return super(ThreadCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('forum_thread_detail', kwargs={'pk': self.object.pk})


class ThreadUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Thread
    form_class = ThreadForm
    login_url = reverse_lazy('accounts_login')

    def test_func(self):
        return self.request.user == self.get_object().admin

    def get_success_url(self):
        return reverse('forum_thread_detail', kwargs={'pk': self.object.pk})


class ThreadDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Thread
    login_url = reverse_lazy('accounts_login')

    def test_func(self):
        return self.request.user == self.get_object().admin

    def get_success_url(self):
        return reverse('forum_category_detail', kwargs={'pk': self.get_object().category.pk})


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    login_url = reverse_lazy('accounts_login')

    def form_valid(self, form):
        form.instance.op = self.request.user
        form.instance.thread = get_object_or_404(Thread, pk=self.kwargs['pk'])

        return super(PostCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('forum_post_detail', kwargs={'pk': self.object.pk})


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    login_url = reverse_lazy('accounts_login')

    def test_func(self):
        return self.request.user == self.get_object().op

    def get_success_url(self):
        return reverse('forum_post_detail', kwargs={'pk': self.object.pk})


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    login_url = reverse_lazy('accounts_login')

    def test_func(self):
        return self.request.user == self.get_object().op

    def get_success_url(self):
        return reverse('forum_thread_detail', kwargs={'pk': self.get_object().thread.pk})


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    login_url = reverse_lazy('accounts_login')

    def form_valid(self, form):
        form.instance.commenter = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['pk'])

        return super(CommentCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('forum_post_detail', kwargs={'pk': self.object.post.pk})


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    login_url = reverse_lazy('accounts_login')

    def test_func(self):
        return self.request.user == self.get_object().commenter

    def get_success_url(self):
        return reverse('forum_post_detail', kwargs={'pk': self.object.post.pk})


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    login_url = reverse_lazy('accounts_login')

    def test_func(self):
        return self.request.user == self.get_object().commenter

    def get_success_url(self):
        return reverse('forum_post_detail', kwargs={'pk': self.get_object().post.pk})


class RuleDetailView(DetailView):
    model = Rule
