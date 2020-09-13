from django.urls import path

from . import views


app_name = 'search'
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('<int:pk>/exec/',views.exec_ajax, name='exec'),
    path('exec/',views.exec_ajax, name='exec'),
    path('comment/',views.CommentCreateView.as_view(), name='comment'),
    path('comment_list/',views.comment_list, name='comment_list'),
    path('post_comment/',views.post_comment, name='post_comment'),

  ]

