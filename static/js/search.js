
$(document).ready(function () {
    // Handle the form submission
    $('#search-form').on('submit', function (event) {
        event.preventDefault(); // Prevent the form from submitting traditionally

        // Get the search query from the form input field
        var searchQuery = $('[name="search_query"]').val();

        // Send an AJAX request to your Django view
        $.ajax({
            url: '/your-django-view-url/', // Replace with your Django view URL
            type: 'POST', // or 'GET' based on your view
            data: { 'search_query': searchQuery },
            dataType: 'json',
            success: function (data) {
                // Handle the success response and update the HTML
                displaySearchResults(data.books);
            },
            error: function () {
                // Handle errors if necessary
                console.error('Failed to retrieve search results.');
            }
        });
    });

    // Function to display search results in HTML
    function displaySearchResults(books) {
        var resultsContainer = $('#search-results');
        resultsContainer.empty(); // Clear previous results

        if (books.length === 0) {
            resultsContainer.append('<p>No books found.</p>');
        } else {
            var ul = $('<ul>');
            $.each(books, function (index, book) {
                ul.append('<li>' + book.volumeInfo.title + '</li>');
            });
            resultsContainer.append(ul);
        }
    }
});
