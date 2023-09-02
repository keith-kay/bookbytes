from django.shortcuts import render
from django.http import HttpResponse
import requests 

# Create your views here.
myname = "keith"
def index(request):
    return HttpResponse("Hello World")

def book_list(request):
    # API URL for fetching book data (replace with actual API endpoint)
    api_url = "https://www.googleapis.com/books/v1/volumes?q=python"

    # Make a GET request to the API
    response = requests.get(api_url)
    data = response.json()

    # Extract book items from the API response
    books = []
    for item in data.get("items", []):
        volume_info = item.get("volumeInfo", {})
        title = volume_info.get("title", "Unknown Title")
        authors = ", ".join(volume_info.get("authors", ["Unknown Author"]))
        cover_image = volume_info.get("imageLinks", {}).get("thumbnail", "")
        books.append({"title": title, "authors": authors, "cover_image": cover_image})

    return render(request, 'bytes/book_list.html', {'books': books})