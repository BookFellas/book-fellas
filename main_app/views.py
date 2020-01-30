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
from django.http import JsonResponse
from django.contrib.staticfiles.templatetags.staticfiles import static

class bookList(APIView):
    def get(self, request):
        query = self.request.GET.get('q')
        books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query) | Q(publisher__icontains=query))
        return render(request, 'search_results.html', {
            'title': 'Results',
            'books': books
        })

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
    return render(request, 'books/index.html', { 'books': books })

def books_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'books/detail.html', {'book': book })

@login_required
def profiles_index(request):
    profiles = Profile.objects.all()
    return render(request, 'profiles/index.html', { 'profiles': profiles })

@login_required
def cart_index(request):
    book = Book.objects.all()
    return render(request, 'cart/index.html', { 'cart': cart }, { 'book': book })

@login_required
def seed(request):
    if request.user.is_superuser:
        return render(request, 'seed.html', {
            'title': 'Seed DB'
        })
    else:
        return redirect('index')

@login_required
def seed_db(request):
    if request.user.is_superuser:
        if request.method == 'GET':
            resp = requests.get(request.GET['link'])

            if resp.status_code != 200:
                print('Something went wrong')
                return JsonResponse({'status': 'nok'})
            else:
                items = resp.json()['items']

                for item in items:
                    if item['volumeInfo'].get('authors') and len(item['volumeInfo'].get('authors')) > 1 :
                        authors = ", ".join(map(str, item['volumeInfo'].get('authors', ['N/A'])))
                    else:
                        authors = item['volumeInfo'].get('authors', ['N/A'])[0]
                    if item['volumeInfo'].get('categories') and len(item['volumeInfo'].get('categories')) > 1:
                        categories = ", ".join(map(str, item['volumeInfo'].get('categories', ['Others'])))
                    else:
                        categories = item['volumeInfo'].get('categories', ['Others'])[0]
                    pages = item['volumeInfo'].get('pageCount', 10)
                    if item['saleInfo']:
                        if (item['saleInfo']['saleability'] == 'FOR_SALE'):
                            price = float(item['saleInfo']['listPrice']['amount'])
                        else:
                            price = round(random.uniform(1.99, 99.99),2)
                    else:
                        price = round(random.uniform(1.99, 99.99),2)
                    industry_identifiers = item['volumeInfo'].get('industryIdentifiers', [])
                    if len(industry_identifiers):
                        isbn = industry_identifiers[0].get('identifier', '123456789123')
                    else:
                        isbn = '123456789123'
                    if item['volumeInfo'].get('imageLinks'):
                        thumbnail = item['volumeInfo']['imageLinks']['thumbnail']
                    else:
                        thumbnail = static('image/no-image.jpg')

                    Book.objects.create(
                        isbn=isbn,
                        title=item['volumeInfo']['title'],
                        year_published=item['volumeInfo'].get('publishedDate', '2011'),
                        author=authors,
                        publisher=item['volumeInfo'].get('publisher', 'N/A'),
                        description=item['volumeInfo'].get('description', 'N/A'),
                        categories=categories,
                        pages=pages,
                        price=price,
                        quantity=random.randint(1, 30),
                        book_img=thumbnail
                    )
                return JsonResponse({'status': 'ok'})
    else:
        return redirect('index')