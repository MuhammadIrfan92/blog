from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('categories',views.catcategories,name="categories"),
    path('home',views.home,name="home"),
    path('<str:header>',views.content,name='content'),
    path('categories/<str:header>',views.catlist,name='catlist'),
]
