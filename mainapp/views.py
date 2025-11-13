from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def add_new_issue(request):
    return render(request, 'main/add-issue.html')