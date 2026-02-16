from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListAPIView.as_view()),
    path('<int:id>/', views.PostDetailAPIView.as_view()),
    path('<int:id>/comments/', views.CommentListAPIView.as_view())
]