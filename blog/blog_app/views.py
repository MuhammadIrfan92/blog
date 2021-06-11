from django.db.models.fields.related import create_many_to_many_intermediary_model
from django.shortcuts import render
from .models import Post
from django.views import generic
from django.http import HttpResponse
# Create your views here.


def catcategories(request):
    data = Post.objects.all()
    return render(request,"categories.html",{'data':data})


def catlist(request, header):
    data = Post.objects.filter(category=header)
    return render(request,'catlist.html',{'data':data})

def content(request,header):
    data = Post.objects.filter(title=header)
    if (data):
        return render(request,'content.html',{'data':data,"header":header})
    else:
        return render(request,'home.html')



def create_blog(request):

    return render(request,'create_blog.html')

def create(request):
    if request.method == 'POST':
        
        title = request.POST['title']
        content = request.POST['content']
        author = request.POST['author']
        category = request.POST['category']

        Post.objects.create(title=title,content=content,author=author,category=category)    
        #data = Post.objects.all()
        #return render(request,"categories.html",{'data':data})  
        return HttpResponse('')
    else:
        data = Post.objects.all()
        return render(request,"categories.html",{'data':data})


def delete(request, header):
    del_post = Post.objects.get(title = header)
    del_post.delete()
    data = Post.objects.all()
    return render(request,"categories.html",{'data':data})

def update(request,header):
    data = Post.objects.filter(title=header)
    if (data):
        return render(request,"update.html",{'data':data,'header':header})
    else:
        return render(request,'home.html')


def update_blog(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        author = request.POST['author']
        category = request.POST['category']
        old = Post.objects.filter(title=title)
        old.delete()
        Post.objects.create(title=title,content=content,author=author,category=category)    
        data = Post.objects.all()
        return render(request,"categories.html",{'data':data})    
    else:
        data = Post.objects.all()
        return render(request,"categories.html",{'data':data})

def home(request):
    sports = Post.objects.filter(category='sports')
    politics = Post.objects.filter(category='politics')
    geography = Post.objects.filter(category='geography')
    fashion = Post.objects.filter(category="fashion")
    content = {
        'politics':politics,
        'sports':sports,
        'fashion':fashion,
        'geography':geography,
    }
    return render(request,"home.html",content)




class PostList(generic.ListView):
    queryset = Post.objects.filter(status = 1).order_by('-created_on')
    template_name = 'main.html'

    #While this view is executing, self.object_list will contain the list of objects (usually,
    #  but not necessarily a queryset) that the view is operating upon.

#The built-in ListViews which is a subclass of generic class-based-views render 
# a list with the objects of the specified model we just need to mention the template, 
# similarly DetailView provides a detailed view for a given object of the model at the provided template.


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
#While this view is executing, self.object will contain the object that the view is operating upon.