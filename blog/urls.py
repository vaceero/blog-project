from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_posts, name='list_posts'),
    path('post/<int:pk>/', views.detail_post, name='detail_post'),
    path('post/new/', views.new_post, name='new_post'),
    path('post/<int:pk>/edit/', views.edit_post, name='edit_post'),
    path('post/<pk>/delete/', views.delete_post, name='delete_post'),
    path('drafts/', views.list_draft_posts, name='list_draft_posts'),
    path('post/<pk>/publish/', views.publish_post, name='publish_post'),
    path('post/<int:pk>/comment/', views.add_comment, name='add_comment'),
    path('comment/<int:pk>/approve/', views.approve_comment, name='approve_comment'),
    path('comment/<int:pk>/remove/', views.remove_comment, name='remove_comment'),
]