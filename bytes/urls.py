from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    # path('books', views.book_list, name='book_list'),
    path('dashboard/', TemplateView.as_view(template_name='bytes/home.html'), name='home'),
    path('', TemplateView.as_view(template_name='bytes/index.html'), name='index'),
    path('signin/', TemplateView.as_view(template_name='bytes/signin.html'), name='signin'),
    path('signup/', TemplateView.as_view(template_name='bytes/signup.html'), name='signup'),
    path('login/', views.loginPage, name="loginPage"),
    path('logout/',views.logoutPage, name="logout"),
    path('search/', views.book_search, name='book_search'),
]