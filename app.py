from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
books = [
    {
        'id': 1,
        'title': 'To Kill a Mockingbird',
        'author': 'Harper Lee',
        'publication_year': 1960,
        'genre': 'Southern Gothic'
    },
    {
        'id': 2,
        'title': '1984',
        'author': 'George Orwell',
        'publication_year': 1949,
        'genre': 'Dystopian Fiction'
    },
    {
        'id': 3,
        'title': 'Pride and Prejudice',
        'author': 'Jane Austen',
        'publication_year': 1813,
        'genre': 'Romantic Novel'
    },
    {
        'id': 4,
        'title': 'The Great Gatsby',
        'author': 'F. Scott Fitzgerald',
        'publication_year': 1925,
        'genre': 'American Literature'
    },
    {
        'id': 5,
        'title': 'The Hunger Games',
        'author': 'Suzanne Collins',
        'publication_year': 2008,
        'genre': 'Young Adult Dystopian'
    },
    {
        'id': 6,
        'title': 'The Catcher in the Rye',
        'author': 'J.D. Salinger',
        'publication_year': 1951,
        'genre': 'American Literature'
    },
    {
        'id': 7,
        'title': 'Nineteen Eighty-Four',
        'author': 'George Orwell',
        'publication_year': 1949,
        'genre': 'Dystopian Fiction'
    },
    {
        'id': 8,
        'title': 'Emma',
        'author': 'Jane Austen',
        'publication_year': 1815,
        'genre': 'Romantic Novel'
    },
    {
        'id': 9,
        'title': 'The Road',
        'author': 'Cormac McCarthy',
        'publication_year': 2006,
        'genre': 'Post-Apocalyptic Fiction'
    },
    {
        'id': 10,
        'title': 'Mockingjay',
        'author': 'Suzanne Collins',
        'publication_year': 2010,
        'genre': 'Young Adult Dystopian'
    },
    {
        'id': 11,
        'title': 'Animal Farm',
        'author': 'George Orwell',
        'publication_year': 1945,
        'genre': 'Satire'
    },
    {
        'id': 12,
        'title': 'The Hobbit',
        'author': 'J.R.R. Tolkien',
        'publication_year': 1937,
        'genre': 'Fantasy'
    },
    {
        'id': 13,
        'title': 'Brave New World',
        'author': 'Aldous Huxley',
        'publication_year': 1932,
        'genre': 'Dystopian Fiction'
    }
]

@app.route('/books', methods=['GET'])
def get_books():
    genre_query = request.args.get('genre', default=None, type=str)
    author_query = request.args.get('author', default=None, type=str)
    year_query = request.args.get('publication_year', default=None, type=str)
    title_query = request.args.get('title', default=None, type=str)

    filtered_books = books

    if genre_query:
        filtered_books = [book for book in books if genre_query.lower() in book['genre'].lower()]
    
    if author_query:
        filtered_books = [book for book in books if author_query.lower() in book['author'].lower()]
    
    if year_query:
        filtered_books = [book for book in books if year_query.lower() in book['publication_year'].lower()]
    
    if title_query:
        filtered_books = [book for book in books if title_query.lower() in book['title'].lower()]

    
    return jsonify(books)

if __name__ == '__main__':
    app.run(debug=True)
