from django.shortcuts import render
from django.http import HttpResponse
import requests 
import random
from .models import *

def home(request):
    return render(request, 'home.html', {
        'title': 'Home Page'
    })

def about(request):
    return render(request, 'about.html', {
        'title': 'About Page'
    })

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
    #         price=round(random.uniform(1.99, 99.99),2),
    #         quantity=random.randint(1, 30),
    #         book_img=item['volumeInfo']['imageLinks']['thumbnail']
    #     )

