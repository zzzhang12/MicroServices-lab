from flask import Flask, jsonify

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
    }
]

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

if __name__ == '__main__':
    app.run(debug=True)
