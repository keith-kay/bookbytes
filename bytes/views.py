from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, JsonResponse  
import requests 
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

# Create your views here.

class SignUpView(TemplateView):
    template_name = 'signup.html'

class SignInView(TemplateView):
    template_name = 'signin.html'

#create user login session
def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)#pass in the request
            return redirect('base')  # Redirect to the 'base' URL pattern
    return render(request, 'signin')

#logout user session
def logoutPage(request):
    logout(request)
    return redirect('signin')
            

def book_search(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query')
        
        # Your Google Books API key
        api_key = 'AIzaSyDVJwXpB5u0nTh1QiLo-p7yPAipj0lSrS0'
        
        # Construct the API URL
        api_url = f'https://www.googleapis.com/books/v1/volumes?q={search_query}&key={api_key}'
        
        # Send a GET request to the API
        response = requests.get(api_url)
        
        if response.status_code == 200:
            data = response.json()
            books = data.get('items', [])
            return render(request, 'result.html', {'books': books})
        else:
            # Handle API request error
            return JsonResponse({'error': 'Failed to retrieve book data from the API.'}, status=500)
    else:
        return JsonResponse({'error': 'This view is for handling POST requests only.'}, status=400)

# def book_list(request):
#     # API URL for fetching book data (replace with actual API endpoint)
#     api_url = "https://www.googleapis.com/books/v1/volumes?q=python"

#     # Make a GET request to the API
#     response = requests.get(api_url)
#     data = response.json()

#     # Extract book items from the API response
#     books = []
#     for item in data.get("items", []):
#         volume_info = item.get("volumeInfo", {})
#         title = volume_info.get("title", "Unknown Title")
#         authors = ", ".join(volume_info.get("authors", ["Unknown Author"]))
#         cover_image = volume_info.get("imageLinks", {}).get("thumbnail", "")
#         books.append({"title": title, "authors": authors, "cover_image": cover_image})

#     return render(request, 'bytes/book_list.html', {'books': books})

@login_required(login_url='signin')
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to the homepage after registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})