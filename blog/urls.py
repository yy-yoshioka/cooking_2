from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('<int:post_id>/', views.blogDetail, name='blog-single'),
    path('create-blog/', views.createBlog, name='create-blog'),

]
