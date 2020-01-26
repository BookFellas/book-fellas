from django.shortcuts import render
from django.http import HttpResponse
import requests

def home(request):
    return render(request, 'home.html', {
        'title': 'Home Page'
    })

def about(request):
    return render(request, 'about.html', {
        'title': 'About Page'
    })

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