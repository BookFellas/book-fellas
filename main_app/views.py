from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book
# import requests

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid credentials - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

def home(request):
    return render(request, 'home.html', {
        'title': 'Home Page'
    })

def about(request):
    return render(request, 'about.html', {
        'title': 'About Page'
    })

def books_index(request):
    books = Book.objects.all()
    # books = Book.objects.filter(user = request.user)
    return render(request, 'books/index.html', { 'books': books })

def books_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'books/detail.html', {'book': book })

def api(request):
    resp = requests.get('https://www.googleapis.com/books/v1/volumes?q=isbn:0679775439')
    
    if resp.status_code != 200:
        print('Something went wrong')

    items = resp.json()['items']
        
    return render(request, 'api.html', {
        'title': 'API',
        'bookTitle': items[0]['volumeInfo']['title'],
        'publisher': items[0]['volumeInfo']['publisher'],
        'publishedDate': items[0]['volumeInfo']['publishedDate'],
        'authors': items[0]['volumeInfo']['authors'][0],
        'ISBN': items[0]['volumeInfo']['industryIdentifiers'][0]['identifier'],
        'category': items[0]['volumeInfo']['description'],
        'description': items[0]['volumeInfo']['description'],
        'thumbnail': items[0]['volumeInfo']['imageLinks']['thumbnail']
    })