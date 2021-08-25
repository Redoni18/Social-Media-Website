from django.urls import path
from .views import (
	homepage,
    PostListView, 
	postDetailView, 
	post_search,
	CreatePostView, 
	UpdatePostView, DeletePostView, 
	UserPostListView, 
	like,
    comment,
    DeleteCommentView,
    UpdateCommentView,
    get_likes
)

urlpatterns = [
    path('',PostListView.as_view(), name='home'),
    path('detail/<int:pk>/', postDetailView.as_view(), name='post-detail'),
    path('search/', post_search, name='search-posts'),
    path('create/', CreatePostView.as_view(template_name='blogi/post_create.html'), name='create-post'),
    path('comment/<int:pk>/', comment, name='create-comment'),
    path('update/<int:pk>/', UpdatePostView.as_view(template_name='blogi/post_create.html'), name='update-post'),
    path('delete/<int:pk>/', DeletePostView.as_view(template_name='blogi/confirm_delete.html'), name='delete-post'),
    path('delete-comment/<int:pk>/', DeleteCommentView.as_view(template_name='blogi/confirm_delete_comment.html'), name='delete-comment'),
    path('update-comment/<int:pk>/', UpdateCommentView.as_view(template_name='blogi/comments.html'), name='update-comment'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('like/<int:pk>/', like, name="likes"),
    path('post-likes/<int:pk>/', get_likes, name="get_likes")

]