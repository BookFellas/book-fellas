from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from .forms import ProfileForm, UserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import requests
import random
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . serializers import bookSerializer
from django.db.models import Q

class bookList(APIView):
    def get(self, request):
        query = self.request.GET.get('q')
        books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
        return render(request, 'search_results.html', {
            'title': 'Results',
            'books': books
        })
        # serializer = bookSerializer(books, many=True)
        # return Response(serializer.data)

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

class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['phone', 'address', 'postal_code', 'city', 'country', 'birthday']

def home(request):
    books = Book.objects.all()
    return render(request, 'home.html', {
        'title': 'Home Page',
        'books': books
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

@login_required
def profiles_index(request):
    profiles = Profile.objects.all()
    # profiles = profile.objects.filter(user = request.user)
    return render(request, 'profiles/index.html', { 'profiles': profiles })

@login_required
def cart_index(request):
    #cart = User.objects.filter(products)
    book = Book.objects.all()
    return render(request, 'cart/index.html', { 'cart': cart }, { 'book': book })

def api(request):
    #resp = requests.get('https://www.googleapis.com/books/v1/volumes?q=subject:fiction')

    # if resp.status_code != 200:
    #     print('Something went wrong')

    # items = resp.json()['items']

    return render(request, 'api.html', { 'items': Book.objects.all()
    # gettign data from api to front end
        # 'title': 'API',
        # 'bookTitle': items[2]['volumeInfo']['title'],
        # 'publisher': items[2]['volumeInfo']['publisher'],
        # 'publishedDate': items[2]['volumeInfo']['publishedDate'],
        # 'authors': items[2]['volumeInfo']['authors'][0],
        # 'ISBN': items[2]['volumeInfo']['industryIdentifiers'][0]['identifier'],
        # 'category': items[2]['volumeInfo']['description'],
        # 'description': items[2]['volumeInfo']['description'],
        # 'thumbnail': items[2]['volumeInfo']['imageLinks']['thumbnail']
    })


    #adding data to the database through the console
    # from main_app.models import *
    # import requests
    # import random
    # resp = requests.get('https://www.googleapis.com/books/v1/volumes?q=subject:fiction')
    # items = resp.json()['items']

    # from main_app.models import *
    # import requests
    # import random

    # resp = requests.get('https://www.googleapis.com/books/v1/volumes?q=subject:fiction')
    # items = resp.json()['items']

    # for item in items:
    #     industry_identifiers = item['volumeInfo'].get('industryIdentifiers', [])
    #     if len(industry_identifiers):
    #         isbn = industry_identifiers[0].get('identifier', '123456789123')
    #     else:
    #         isbn = '123456789123'

    #     Book.objects.create(
    #         isbn=isbn,
    #         title=item['volumeInfo']['title'],
    #         year_published=item['volumeInfo'].get('publishedDate', '2011'),
    #         author=item['volumeInfo']['authors'][0],
    #         publisher=item['volumeInfo']['publisher'],
    #         description=item['volumeInfo']['description'],
    #         price=round(random.uniform(1.99, 99.99),2),
    #         quantity=random.randint(1, 30),
    #         book_img=item['volumeInfo']['imageLinks']['thumbnail']
    #     )