from django.urls import path, include
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    url(r'^books/$', views.books_index, name='index'),
    path('books/<int:book_id>/', views.books_detail, name='detail'),
    path('profiles/', views.profiles_index, name='profiles_index'),
    path('profiles/<int:pk>/update/', views.ProfileUpdate.as_view(), name='profiles_update'),
    path('cart/', views.cart_index, name='cart_index'),
    path('accounts/signup/', views.signup, name='signup'),
    url(r'^search/$', views.bookList.as_view(), name='search'),
    url(r'^seed_db/$', views.seed_db, name='seed_db'),
    path('seed/', views.seed, name='seed'),
    path('books/<int:book_id>/add_product_item', views.add_product_item, name='add_product_item'),
    path('categories_api/', views.categories_api, name='categories_api'),
    url(r'categories/$', views.categoriesList.as_view(), name='categories'),
    path('books/<int:book_id>/add_product_item_index', views.add_product_item_index, name='add_product_item_index'),
    path('cart/<int:product_item_id>/delete_product_item/', views.delete_product_item, name='delete_product_item'),
]