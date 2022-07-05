from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import Course
from django.contrib.auth.models import User
from accounts.models import Course,Post,Replie,Document
from .forms import CreateUserForm
from .forms import EnrollForm
from django.contrib.auth import authenticate,login,logout
from django.http import FileResponse
#from tensorflow import Tokenizer
import os
# from rest_framework import viewsets 
# from rest_framework.decorators import api_view 
from django.core import serializers 
# from rest_framework.response import Response 
# from rest_framework import status 
# from django.http import JsonResponse 
# from rest_framework.parsers import JSONParser 
from .models import Student 
# from .serializer import StudentSerializers 

import pickle
import json 
import pandas as pd 
#from django.shortcuts import render, redirect 
#from django.contrib import messages 

def home(request):
    Courses = Course.objects.all()

    return render(request, "accounts/mycourse.html", {'Courses': Courses})


def redirecthome(request):
    return render(request,'accounts/home_lr.html')
def logouttohome(request):
    return render(request,'accounts/home_lr.html')


def loginpage(request):
    if request.method == 'POST':
       username= request.POST.get('username')
       password=request.POST.get('password')
       user = authenticate(request, username=username,password=password)
       if user is not None:
           login(request,user)
           return redirect('home')
    context ={}
    return render(request,'accounts/login.html',context)

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account was created for '+ user)
            return redirect('login')
    context = {'form':form}
    return render(request,'accounts/register.html',context)
def logoutUser(request):
    logout(request)
    return redirect('login')

def javacourseview(request):
    if request.user.is_authenticated:
        return render(request,'accounts/java_course.html')
    else:
        return redirect('login')
def cppcourseview(request):
    if request.user.is_authenticated:
        return render(request,'accounts/cpp_course.html')
    else:
        return redirect('login')

def pythoncourseview(request):
    if request.user.is_authenticated:
        return render(request,'accounts/python_course.html')
    else:
        return redirect('login')
def aboutview(request):
    if request.user.is_authenticated:
        return render(request,'accounts/about.html')
    else:
        return redirect('login')

def quizjavaview(request):
    if request.user.is_authenticated:
        return render(request,'accounts/quiz_java.html')
    else:
        return redirect('login')
def quizpythonview(request):
    if request.user.is_authenticated:
        return render(request,'accounts/quiz_python.html')
    else:
        return redirect('login')
def quizcppview(request):
    if request.user.is_authenticated:
        return render(request,'accounts/quiz_cpp.html')
    else:
        return redirect('login')

def availcourseview(request):
    if request.user.is_authenticated:
        Courses = Course.objects.all()
        return render(request, "accounts/availablecourses.html", {'Courses': Courses})
        #return render(request,'accounts/availablecourses.html')
    else:
        return redirect('login')
def viewbookspage(request):
    if request.user.is_authenticated:
        Courses = Course.objects.all()
        return render(request, "accounts/viewbooks.html", {'Courses': Courses})
    else:
        return redirect('login')
def javabookview(request):
    if request.user.is_authenticated:
        filepath = os.path.join('static', 'javabook.pdf')
        return FileResponse(open(filepath, 'rb'), content_type = 'application/pdf')
        #return render(request,'accounts/viewbooks.html')
    else:
        return redirect('login')
def pythonbookview(request):
    if request.user.is_authenticated:
        filepath = os.path.join('static', 'pythonbook.pdf')
        return FileResponse(open(filepath, 'rb'), content_type = 'application/pdf')
        #return render(request,'accounts/viewbooks.html')
    else:
        return redirect('login')
def cppbookview(request):
    if request.user.is_authenticated:
        filepath = os.path.join('static', 'Cppbook.pdf')
        return FileResponse(open(filepath, 'rb'), content_type = 'application/pdf')
        #return render(request,'accounts/viewbooks.html')
    else:
        return redirect('login')
def viewenrollpage(request):
    if request.user.is_authenticated:
        form = EnrollForm(request.POST or None)
        if request.method == 'POST':
                form = EnrollForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('home')
        return render(request,'accounts/enrollcourse.html', {'form':form})
    else:
        return redirect('login')
def discussionforum(request):
    if request.user.is_authenticated:
        if request.method=="POST":   
            user = request.user
            content = request.POST.get('content','')
            post = Post(user1=user,post_content=content)
            post.save()
            alert = True
            return render(request, "accounts/discussionforum.html", {'alert':alert})
        posts = Post.objects.all()
        return render(request, "accounts/discussionforum.html", {'posts':posts})
    else:
        return redirect('login')
    
def replyforum(request,myid):
    if request.user.is_authenticated:
        post = Post.objects.filter(id=myid).first()
        replies = Replie.objects.filter(post=post)
        if request.method=="POST":
            user = request.user
            desc = request.POST.get('desc','')
            post_id =request.POST.get('post_id','')
            reply = Replie(user = user, reply_content = desc, post=post)
            reply.save()
            alert = True
            return render(request, "accounts/replyforum.html", {'alert':alert})
        return render(request, "accounts/replyforum.html", {'post':post, 'replies':replies})
    else:
        return redirect('login')

def editorview(request):
    if request.user.is_authenticated:
        docid = int(request.GET.get('docid', 0))
        documents = Document.objects.all()

        if request.method == 'POST':
            docid = int(request.POST.get('docid', 0))
            title = request.POST.get('title')
            content = request.POST.get('content', '')
            user=request.user

            if docid > 0:
                document = Document.objects.get(pk=docid)
                document.user=user
                document.title = title
                document.content = content
                document.save()

                return redirect('/editor/?docid=%i' % docid)
            else:
                document = Document.objects.create(user=user,title=title, content=content)

            return redirect('/editor/?docid=%i' % document.id)

        if docid > 0:
            document = Document.objects.get(pk=docid)
        else:
            document = ''

        context = {
        
        'docid': docid,
        'documents': documents,
        'document': document
        }

        return render(request, 'accounts/editor.html', context)
        
    else:
        return redirect('login')


def delete_document(request, docid):
    document = Document.objects.get(pk=docid)
    document.delete()

    return redirect('/editor/?docid=0')



def FormView(request):
    if request.user.is_authenticated:
        return redirect('http://127.0.0.1:7860/')
        #return redirect('https://43279.gradio.app')
    else:
        return redirect('login')
        




  
