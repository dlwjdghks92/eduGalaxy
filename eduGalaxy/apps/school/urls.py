from django.urls import path
from apps.school import views as school_view


app_name = 'school'

urlpatterns = [
    path('', school_view.index, name='index'),
    path('post/', school_view.AdminPostList.as_view(), name='postList')
    path('post/<int:pk>/', views.post_detail, name='post_detail')
]

