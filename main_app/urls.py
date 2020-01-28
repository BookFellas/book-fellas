from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('books/', views.books_index, name='index'),
    path('books/<int:book_id>/', views.books_detail, name='detail'),
    path('api/', views.api, name='api'),
    path('profiles/', views.profiles_index, name='profiles_index'),
    path('profiles/<int:pk>/update/', views.ProfileUpdate.as_view(), name='profiles_update'),
    path('cart/', views.cart_index, name='cart_index'),
    path('accounts/signup', views.signup, name='signup'),
]