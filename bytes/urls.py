from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('books', views.book_list, name='book_list'),
    # path('',views.index, name='home'),
    path('base/', TemplateView.as_view(template_name='bytes/base.html'), name='base'),
    path('', TemplateView.as_view(template_name='bytes/index.html'), name='index'),
    path('signin/', TemplateView.as_view(template_name='bytes/signin.html'), name='signin'),
    path('signup/', TemplateView.as_view(template_name='bytes/signup.html'), name='signup'),
]