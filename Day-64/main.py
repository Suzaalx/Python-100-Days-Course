from flask import Flask, render_template, redirect, url_for, request
from imdb import Cinemagoer
from flask_sqlalchemy import SQLAlchemy
from pprint import pprint

imdb = Cinemagoer()
app = Flask(__name__)
app.app_context().push()
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# database table
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(250), nullable=False)
    image= db.Column(db.String(250), nullable=False)
    
    
    def __repr__(self):
        return f"<Movie {self.title}>"

db.create_all()


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.ranking).all()
    return render_template("index.html", movies=all_movies)



@app.route('/select')
def select():
    return render_template('select.html')
    

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        movie= request.form['title']
        data= imdb.search_movie(movie)
        return render_template("select.html", movies=data)
    else:
        return render_template("add.html")


@app.route('/find/<id>')
def find(id):
    total_movies = Movie.query.count()
    try:
        movie=imdb.get_movie(id)
        # add movie to database 
        movie = Movie(
            title=movie.data['title'],
            year=movie.data['year'],
            description=movie.data['plot outline'],
            rating=movie.data['rating'],
            ranking=total_movies+1,
            review="",
            image=movie.data['cover url'],
            
        )
        db.session.add(movie)
        db.session.commit()
    except:
        return "Movie not found"
    
    return redirect(url_for('edit', id=movie.id))


@app.route("/edit/<id>", methods=["GET", "POST"])
def edit(id):
    movie_to_update = Movie.query.get(id)
    if request.method == "POST":
        if request.form['ranking'] != '':
            movie_to_update.ranking = request.form["ranking"]
        
        if request.form['review'] != '':
                movie_to_update.review = request.form["review"]

        db.session.commit()
        return redirect(url_for("home"))
    else:
        return render_template("edit.html", movie=movie_to_update)


@app.route("/delete/<int:id>")
def delete(id):
    movie_to_delete = Movie.query.get(id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
