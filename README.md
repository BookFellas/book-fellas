# BookFellas

## Implementation

## Links

* [Trello Board](https://trello.com/invite/b/6kHiq3Ox/ebeed5878b3999e5ca4831551aff3f23/bookfellas)
* [ERD](https://www.lucidchart.com/documents/edit/a13a5ccf-2e0b-4f4f-b553-a4a373618dcc/0_0?shared=true)

```python
    #adding data to the database through the console
    from main_app.models import *
    import requests
    import random
    resp = requests.get('https://www.googleapis.com/books/v1/volumes?q=subject:fiction')
    items = resp.json()['items']

    from main_app.models import *
    import requests
    import random

    resp = requests.get('https://www.googleapis.com/books/v1/volumes?q=subject:fiction')
    items = resp.json()['items']

    for item in items:
        industry_identifiers = item['volumeInfo'].get('industryIdentifiers', [])
        if len(industry_identifiers):
            isbn = industry_identifiers[0].get('identifier', '123456789123')
        else:
            isbn = '123456789123'

        Book.objects.create(
            isbn=isbn,
            title=item['volumeInfo']['title'],
            year_published=item['volumeInfo'].get('publishedDate', '2011'),
            author=item['volumeInfo']['authors'][0],
            publisher=item['volumeInfo']['publisher'],
            description=item['volumeInfo']['description'],
            price=round(random.uniform(1.99, 99.99),2),
            quantity=random.randint(1, 30),
            book_img=item['volumeInfo']['imageLinks']['thumbnail']
        )
```