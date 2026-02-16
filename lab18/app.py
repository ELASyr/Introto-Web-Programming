from flask import Flask, render_template, abort
from markupsafe import escape

app = Flask(__name__)

# Sample data (list of dictionaries)
BOOKS = [
    {"id": 1, "title": "1984", "author": "George Orwell", "year": 1949},
    {"id": 2, "title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937},
    {"id": 3, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
]

@app.route("/")
def index():
    return render_template("index.html", title="Book List", books=BOOKS)

# Optional: dynamic route for book details
@app.route("/book/<int:book_id>")
def book_detail(book_id):
    for book in BOOKS:
        if book["id"] == book_id:
            # escape not strictly needed for these hardcoded values,
            # but shown here to demonstrate safe output usage
            safe_book = {
                "id": book["id"],
                "title": escape(book["title"]),
                "author": escape(book["author"]),
                "year": book["year"],
            }
            return render_template("book.html", title="Book Details", book=safe_book)
    abort(404)

if __name__ == "__main__":
    app.run(debug=True)
