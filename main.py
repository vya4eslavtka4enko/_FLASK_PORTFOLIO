from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/project.html')
def projects():
    return render_template('project.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

app.run()