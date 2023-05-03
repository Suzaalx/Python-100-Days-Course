from flask import Flask, render_template
import requests

app = Flask(__name__)
url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(url)
data= response.json()
print(data)

@app.route('/')
def home():
    # read the data from the api

    
    return render_template("index.html", blogs=data)

@app.route('/blog/<id>')
def blog(id):
    return render_template("post.html", blog=data[int(id)-1])

if __name__ == "__main__":
    app.run(debug=True)
