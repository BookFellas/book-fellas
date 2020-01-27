from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('books/', views.books_index, name='index'),
    path('books/<int:book_id>/', views.books_detail, name='detail'),
    path('api/', views.api, name='api'),
    path('profiles/', views.profiles_index, name='profiles_index'),
    # path('profiles/<int:profile_id>/', views.profiles_detail, name='detail'),
    # path('profiles/create/', views.profileCreate.as_view(), name='profiles_create'),
    # path('profiles/<int:pk>/update/', views.profileUpdate.as_view(), name='profiles_update'),
    path('accounts/signup', views.signup, name='signup'),
]