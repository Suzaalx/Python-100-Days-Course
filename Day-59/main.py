from flask import Flask, render_template, request, redirect, url_for, flash
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def receive():
    username = request.form['username']
    password = request.form['password']
    return f" Username: {username} Password: {password}"

if __name__ == "__main__":
    app.run(debug=True)
    
    