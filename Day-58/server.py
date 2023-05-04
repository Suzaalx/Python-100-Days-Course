from flask import Flask, render_template
import requests

app = Flask(__name__)
blogs= requests.get("https://api.npoint.io/7b43b457431b91bdd0c4")
data= blogs.json()
for blog in data:
    print(blog["title"])


@app.route("/")
def home():
    return render_template("main.html", blogs=data)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    
    return render_template("contact.html")

@app.route("/blogs/<int:id>")
def blogs(id):
    for blog in data:
        if blog["id"]==id:
            return render_template("blogs.html", blog=blog)
    

if __name__ == "__main__":
    app.run(debug=True)