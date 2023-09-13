from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, JsonResponse  
import requests, random
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

api_key = 'AIzaSyDVJwXpB5u0nTh1QiLo-p7yPAipj0lSrS0'
# Create your views here.

class SignUpView(TemplateView):
    template_name = 'signup.html'
class SignInView(TemplateView):
    template_name = 'signin.html'

#login user session
def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)#pass in the request
            return redirect('home')  # Redirect to the 'base' URL pattern
    return render(request, 'signin')

#logout user session
def logoutPage(request):
    logout(request)
    return redirect('signin')

#search book session
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
            return render(request, 'bytes/book_list.html', {'books': books})
        else:
            # Handle API request error
            return JsonResponse({'error': 'Failed to retrieve book data from the API.'}, status=500)
    else:
        return JsonResponse({'error': 'This view is for handling POST requests only.'}, status=400)

# retrieve fiction books
def best_selling_books(request):
    api_url = f'https://www.googleapis.com/books/v1/volumes?q=subject:Fiction&key={api_key}&maxResults=40'
    # Make a request to the Google Books API to fetch best-selling books
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        books = data.get('items', [])

        # Generate a random starting index
        num_books = len(books)
        if num_books > 0:
            random_start_index = random.randint(0, num_books - 1)
            # Select 12 books starting from the random index
            selected_books = books[random_start_index:random_start_index + 12]
        else:
            selected_books = []
    else:
        # Handle API request error
        selected_books = []

    return render(request, 'bytes/home.html', {'books': selected_books})

#retrieve mystery books
def mystery(request):
      # Retrieve url
    api_url = f'https://www.googleapis.com/books/v1/volumes?q=subject:Mystery&key={api_key}&maxResults=40'
    # Make a request to the Google Books API to fetch best-selling books
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        books = data.get('items', [])

        # Generate a random starting index
        num_books = len(books)
        if num_books > 0:
            random_start_index = random.randint(0, num_books - 1)
            # Select 12 books starting from the random index
            selected_books = books[random_start_index:random_start_index + 12]
        else:
            selected_books = []
    else:
        # Handle API request error
        selected_books = []

    return render(request, 'bytes/home.html', {'books': selected_books})

#retrieve romance books
def romance(request):
      # Retrieve url
    api_url = f'https://www.googleapis.com/books/v1/volumes?q=subject:Romance&key={api_key}&maxResults=40'
    # Make a request to the Google Books API to fetch best-selling books
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        books = data.get('items', [])

        # Generate a random starting index
        num_books = len(books)
        if num_books > 0:
            random_start_index = random.randint(0, num_books - 1)
            # Select 12 books starting from the random index
            selected_books = books[random_start_index:random_start_index + 12]
        else:
            selected_books = []
    else:
        # Handle API request error
        selected_books = []

    return render(request, 'bytes/home.html', {'books': selected_books})

#retrieve fantasy books
def fantasy(request):
    # Retrieve url
    api_url = f'https://www.googleapis.com/books/v1/volumes?q=subject:Fantasy&key={api_key}&maxResults=40'
    # Make a request to the Google Books API to fetch best-selling books
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        books = data.get('items', [])

        # Generate a random starting index
        num_books = len(books)
        if num_books > 0:
            random_start_index = random.randint(0, num_books - 1)
            # Select 12 books starting from the random index
            selected_books = books[random_start_index:random_start_index + 12]
        else:
            selected_books = []
    else:
        # Handle API request error
        selected_books = []

    return render(request, 'bytes/home.html', {'books': selected_books})

#retrieve comic books
#retrieve fantasy books
def comic(request):
    # Retrieve url
    api_url = f'https://www.googleapis.com/books/v1/volumes?q=subject:Anime&key={api_key}&maxResults=40'
    # Make a request to the Google Books API to fetch best-selling books
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        books = data.get('items', [])

        # Generate a random starting index
        num_books = len(books)
        if num_books > 0:
            random_start_index = random.randint(0, num_books - 1)
            # Select 12 books starting from the random index
            selected_books = books[random_start_index:random_start_index + 12]
        else:
            selected_books = []
    else:
        # Handle API request error
        selected_books = []

    return render(request, 'bytes/home.html', {'books': selected_books})

#register new user
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
