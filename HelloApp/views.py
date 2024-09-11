from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *


# Create your views here.

#req or request works!
#context is of a dictionary type

def show_index(request):
    #query parameters any thing after a question mark ? to add other you use & to seperate em!
    from random import randint
    random_shii = [randint(1,i) for i in range(1,50)]
    even_random = [item for item in random_shii if item % 2 == 0]

        
        
    first_name = "Adedamola"
    last_name = "Adedamola"
    myname = 'Apex'
    myhome = 'Somewhere...'
    age = 19
    loops = [i ** 2 for i in range(10)]
    context = {
        'name' : myname,
        'address': myhome,
        'firstname' : first_name,
        'lastname' : last_name,
        'age' : age,
        'loop' : loops,
        'random' : random_shii,
        'even_random' : even_random,
    }

    return render(request, 'hello_app/index.html', context)

def show_about(request):

    all_bio = BioData.objects.all()[ : : -1]

    #GET show sensitive data on the url while POST conceals it!
    context = {}
    if request.method == 'POST':
        context = {
            'fname' : request.POST.get('fname'),
            'lname' : request.POST.get('lname'),
            'age' : request.POST.get('age'),
            'gender' : request.POST.get('gender'),
           
        }
        
        fname1 = context['fname']
        lname1 = context['lname']
        age1 = context['age']
        gender1 = context['gender']

        bio = BioData(fname= fname1, lname= lname1, age= age1, gender= gender1)
        bio.save()
    
    context[ 'all_bio'] = all_bio


    return render(request, 'hello_app/about.html', context)

def show_contact(request):
    return render(request, 'hello_app/contact.html')

def show_query(request):
    #sending data from url to django view, processing and returning a response
    #
    context = {
        'fname' : request.GET.get('fname'),
        'lname' : request.GET.get('lname'),
        'age' : request.GET.get('age'),
        #'calc': round(eval(request.GET.get('calc')))
    }
    return render(request, 'hello_app/query.html', context)

def show_search(request):
    
    import requests
    from pprint import pprint
    base_url = 'https://api.dictionaryapi.dev/api/v2/entries/en/'
    user_src = request.GET.get('search', '')
    base_url += user_src
    word_def = []
    word_ex = []

    try:
        print('Definitions: ')
        count = 0
        result = requests.get(base_url).json()
        
        for items in result:
            for meaning in items['meanings']:
                for definitions in meaning['definitions']:
                    count += 1
                    word_def.append(definitions['definition'])
                    #print(f"{count}. {definitions['definition']}")
                    
        
        count = 0
        for items in result:
            for meaning in items['meanings']:
                for examples in meaning['definitions']:
                    if 'example' in examples:
                        count += 1
                        word_ex.append(examples['example'])
                        #print(f"{count}.", examples['example'])

    except:
        print('error occured')
        
    context = {
    'word' : request.GET['search'],
    'word_def' : word_def,
    'word_ex' : word_ex,

        }
    return render(request, 'hello_app/word_search.html', context)

from HelloApp.models import BioData
import random

def show_empty(request, num):
    biodata = BioData.objects.filter(id = num).first()
    # if BioData.objects.filter(id = num).exists():
    #     biodata = BioData.objects.get(id = num)
    # else:
    #     biodata = None
    context = {
            'data' : biodata,
    }
    return render(request, 'hello_app/empty.html',context)

def deletebio(request, id):
    BioData.objects.filter(id = id).delete()
    return redirect('/about-page/')

def update_bio(request, id):
    data = BioData.objects.filter(id = id).first()
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        age = request.POST['age']
        gender = request.POST['gender']

        data.fname = fname
        data.lname = lname
        data.age = age
        data.gender = gender
        data.save()
        return redirect('/about-page/')
        
    context = {
        'data' : data, 
    }
     
    return render(request,'hello_app/update.html', context)

def show_blog(request):
    all_data = BlogData.objects.all()
    context = {
        'all_data' : all_data,
    }
    return render(request, 'hello_app/blog.html', context)

def blog_detail(request, id):
    data = BlogData.objects.filter(id = id).first()
    context = {
        'post' : data,
    }
    return render(request, 'hello_app/blog_detail.html',context)

    

#Model View Controller - Model View Template