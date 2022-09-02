from django.urls import path
from .views import PostList, PostDetail, PostListDetailfilter


app_name = 'blog_api'

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
    path('', PostList.as_view(), name='listcreate'),
    path('search/', PostListDetailfilter.as_view(), name='postsearch'),
]

