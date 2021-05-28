from django.shortcuts import render
from .models import Post
from django.views import generic
# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.filter(status = 1).order_by('-created_on')
    template_name = 'index.html'

    #While this view is executing, self.object_list will contain the list of objects (usually,
    #  but not necessarily a queryset) that the view is operating upon.

#The built-in ListViews which is a subclass of generic class-based-views render 
# a list with the objects of the specified model we just need to mention the template, 
# similarly DetailView provides a detailed view for a given object of the model at the provided template.


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
#While this view is executing, self.object will contain the object that the view is operating upon.