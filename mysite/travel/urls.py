from django.urls import path, include
from django.contrib import admin
from users import views as user_views
from . import views #.is local directory
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserListView




urlpatterns = [
    path('', PostListView.as_view(), name='Travel-home'), #views.home looks for function home in views progam
    path('user/<str:username>/',UserListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='Travel-about'), #views.about looks for function about in views program

]


#<app>/model>_<viewtype>.html
# path('', views.home, name='Travel-home'), #views.home looks for function home in views progam
# path('about/', views.about, name='Travel-about'), #views.about looks for function about in views program