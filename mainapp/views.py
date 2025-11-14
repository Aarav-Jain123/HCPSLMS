from django.shortcuts import render
from .forms import BookForm, AuthorForm, PublicationForm, IssueForm


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def add_book(request):
    f = None

    # POST request: bind data
    if request.method == "POST":
        # Optionally: save if valid
        if f.is_valid():
            f.save()
    
    # GET request or if form not bound
    if f is None:
            f = BookForm()
    return render(request, 'main/add-content.html', {"form": f})  


def add_author(request):
    f = None

    # POST request: bind data
    if request.method == "POST":
        # Optionally: save if valid
        if f.is_valid():
            f.save()
    
    # GET request or if form not bound
    if f is None:
            f = AuthorForm()
    return render(request, 'main/add-content.html', {"form": f}) 


def add_publication(request):
    f = None

    # POST request: bind data
    if request.method == "POST":
        # Optionally: save if valid
        if f.is_valid():
            f.save()
    
    # GET request or if form not bound
    if f is None:
            f = PublicationForm()
    return render(request, 'main/add-content.html', {"form": f})


def add_issue(request):
    f = None

    # POST request: bind data
    if request.method == "POST":
        # Optionally: save if valid
        if f.is_valid():
            f.save()
    
    # GET request or if form not bound
    if f is None:
            f = IssueForm()
    return render(request, 'main/add-content.html', {"form": f}) 


def view_content(request):
    return render(request, 'main/view-content.html')
