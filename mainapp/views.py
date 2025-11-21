from django.shortcuts import render, redirect
from .forms import BookForm, AuthorForm, PublicationForm, IssueForm
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def add_book(request):
    f = BookForm()
    if request.method == "POST":
        if f.is_valid():
            f.save()
            messages.success("Operation done successfully!", request)
            return redirect('view-book/')
        
    return render(request, 'main/add-content.html', {"form": f})  


def add_author(request):
    f = AuthorForm()
    if request.method == "POST":
        if f.is_valid():
            f.save()
            messages.success("Operation done successfully!", request)
            return redirect('view-author/')
    
            
    return render(request, 'main/add-content.html', {"form": f}) 


def add_publication(request):
    f = PublicationForm()
    if request.method == "POST":
        if f.is_valid():
            f.save()
            messages.success("Operation done successfully!", request)
            return redirect('view-publication/')
        
    return render(request, 'main/add-content.html', {"form": f})


def add_issue(request):
    f = IssueForm()
    if request.method == "POST":
        if f.is_valid():
            f.save()
            messages.success("Operation done successfully!", request)
            return redirect('/')
    return render(request, 'main/add-content.html', {"form": f}) 


def view_book(request):
    return render(request, 'main/view-content.html')


def view_author(request):
    return render(request, 'main/view-content.html')


def view_publication(request):
    return render(request, 'main/view-content.html')


def view_issue(request):
    return render(request, 'main/view-content.html')
