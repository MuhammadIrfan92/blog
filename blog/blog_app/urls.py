from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('categories',views.catcategories,name="categories"),
    path('home',views.home,name="home"),
    path('create_blog',views.create_blog,name='create_blog'),
    path('create',views.create,name = 'create'),
    path('update/update_blog',views.update_blog,name='update_blog'),
    path('delete/<str:header>',views.delete,name = 'delete'),
    path('update/<str:header>',views.update,name = 'update'),
    path('home/<str:header>',views.content,name='content'),
    path('categories/<str:header>',views.catlist,name='catlist'),
    
]
