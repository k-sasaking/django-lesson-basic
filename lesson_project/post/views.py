from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import PostCreateForm, PostUpdateForm
from .models import Post


def index(request):

    template_name = "post_list.html"
    context = {}
    return render(request, template_name, context)


def create(request):

    template_name = "post_form.html"
    context = {}
    return render(request, template_name, context)


# CreateViewの書き方
class PostCreateView(CreateView):
    form_class = PostCreateForm
    template_name = 'post_form.html'
    success_url = reverse_lazy('post:post_list')


# ListViewの書き方
class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'


# DetailViewの書き方
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'









# ListViewの書き方
class PostAdminListView(ListView):
    model = Post
    template_name = 'post_admin_list.html'


# ここにUpadateView
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostUpdateForm
    template_name = 'post_update_form.html'
    success_url = reverse_lazy('post:post_admin_list')

# ここにDeleteView
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete_confirm.html'
    success_url = reverse_lazy('post:post_admin_list')
