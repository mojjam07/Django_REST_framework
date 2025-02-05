from django.urls import path
from . import views

urlpatterns = [
    path('homepage', views.homepage, name='homepage'),
    path("", views.PostListCreateView.as_view, name="list_posts"),
    path("<int:post_id>", views.post_detail, name="post_detail"),
    path('update/<int:post_id>/', views.update_post, name='update_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post')
]