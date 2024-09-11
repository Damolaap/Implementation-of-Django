from django.shortcuts import render, redirect
from BlogApp.models import *

# Create your views here.

# lookup filters 
# Django template filters

#lt
#gt
#startswith
#endswith 
#contains
#icontains : not case sensitive

def show_index(request):
    
    search = request.GET.get('query')

    if search is not None and len(search.strip()) > 0: 
        blog_data = BlogPost.objects.filter(blog_title__icontains = search)
    
    else:
        blog_data = BlogPost.objects.all()

    context = {
        'blog_data' : blog_data
    }
    return render(request, 'blog_app/index.html', context)

def show_post(request, id):
    post = BlogPost.objects.filter(id = id).first()
    comment = Comments.objects.filter(owner = post)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')

        new_comment = Comments(owner = post, name = name, email = email, comment = comment)
        new_comment.save()
        
        return redirect(f'/post/{id}/')
    context = {
        'comments' : comment,
        'post' : post,
        }
    return render(request, 'blog_app/post.html', context)

def show_contact(request):
    return render(request, 'blog_app/contact.html')

def show_about(request):
    return render(request, 'blog_app/about.html')

def category(request, category):
    post_category = Category.objects.filter(category_name__icontains = category).first()
    blog_data = BlogPost.objects.filter(category = post_category.id)

    context = {
        'blog_data' : blog_data,
    }
    return render(request, 'blog_app/index.html', context)