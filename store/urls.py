from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog', views.blog, name='blog'),
    path('blog/blogentry/<int:id>', views.blogentry, name='blogentry'),
    path('contact/', views.contact, name='contact'),
    path('gallery', views.gallery, name='gallery'),
    path('success', views.success, name='success'),
]
