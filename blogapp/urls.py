from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('register/', views.UserRegister.as_view(), name='register'),
    # path('register/', views.user_register,  name='register'),
    # path('login/', views.user_login, name='login'),
    # path('logout/', views.user_logout, name='logout'),
    path('post_blog/', views.PostCreate.as_view(), name='post_blog'),
    path('blog_detail/<int:pk>/', views.Blog_Detail.as_view(), name='blog_detail'),
    path('delete/<int:pk>/', views.Delete.as_view(), name="delete"),
    # path('delete/<int:id>/', views.delete, name='delete'),
    path('edit/<int:pk>/', views.Edit.as_view(), name="edit"),
    # path('edit/<int:id>/', views.edit, name='edit'),
    path('comment/<int:pk>/', views.AddCommentView.as_view(), name="comment"),
    path('editcomment/<int:pk>/', views.EditCommentView.as_view(), name="editcomment"),
    path('dashboard/', views.DashBoardView.as_view(), name="dashboard"),
    path('dashboard/user_list/', views.User_ListView.as_view(), name="user_list"),
    path('showposts/<int:pk>/', views.ShowPostsView.as_view(), name="showposts"),
    path('publish/<int:pk>/', views. PublishView.as_view(), name="publish"),
]