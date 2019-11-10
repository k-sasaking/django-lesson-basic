from django.urls import path

from . import views

app_name = 'post'
urlpatterns = [
    path('', views.index, name='index'),
    path('regist/', views.create, name='post_regist'),

    path('list/', views.PostListView.as_view(), name='post_list'),

    path('create/', views.PostCreateView.as_view(), name='post_create'),
    path('admin/list/', views.PostAdminListView.as_view(), name='post_admin_list'),
    path('detail/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('update/<int:pk>', views.PostUpdateView.as_view(), name='post_update'),
    path('delete/<int:pk>', views.PostDeleteView.as_view(), name='post_delete'),
]