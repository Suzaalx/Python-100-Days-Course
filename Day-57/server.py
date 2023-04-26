from flask import Flask , render_template , request , redirect , url_for , flash , jsonify
import requests
app= Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/guess/<name>')
def guess(name):
    url =f"https://api.genderize.io?name={name}"
    response=requests.get(url)
    data= response.json()
    gender= data["gender"]
    
    return render_template('guess.html' , name=name, gender=gender)

@app.route('/blog')
def blog():
    blog_url= "https://api.npoint.io/c790b4d5cab58020d391"
    response=requests.get(blog_url)
    data= response.json()
    print(data)
    return render_template('blog.html', posts=data)

if __name__ == "__main__":
    app.run(debug=True)
    
    
    
