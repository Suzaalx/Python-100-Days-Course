from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy


# db = sqlite3.connect("books-collection.db")
app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False, unique=True)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


    def __repr__(self):
        return f"<Book {self.title}>"

db.create_all()

# new_book = Book( title="Harrgghtrterterthfcvcgyew Potter", author="J. K. Rowling", rating=9.3)
# db.session.add(new_book)
# db.session.commit()

# add all books to database

all_books=[]




@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        try:
            new_book = Book(
                title=request.form["title"],
                author=request.form["author"],
                rating=request.form["rating"]
            )
            
            db.session.add(new_book)
            db.session.commit()
        except:
            return "There was an issue adding your book.Make sure you fill out all the fields correctly."
        return redirect(url_for("home"))
    
    return render_template("add.html" )

@app.route("/delete/<int:id>")
def delete(id):
    book_to_delete = Book.query.get(id)
    try:
        db.session.delete(book_to_delete)
        db.session.commit()
        return redirect(url_for("home"))
    except:
        return "There was a problem deleting that book. "

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    book_to_edit = Book.query.get(id)
    try:
        if request.method == "POST":
            new_rating = request.form["rating"]
            book_to_edit.rating = new_rating
            db.session.commit()
            return redirect(url_for("home"))
    except:
        return "There was a problem editing that book. Make sure you fill out all the fields correctly."

    else:
        return render_template("edit.html", book=book_to_edit)
    


if __name__ == "__main__":
    app.run(debug=False)

