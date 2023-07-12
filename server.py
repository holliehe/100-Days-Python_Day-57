from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    blog_url = "https://api.npoint.io/f62a99bbbf505ecdbf4b"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)

@app.route('/blog/<int:number>')
def blog(number):
    blog_url = "https://api.npoint.io/f62a99bbbf505ecdbf4b"
    response = requests.get(blog_url)
    all_posts = response.json()

    return render_template('post.html', post=all_posts[number-1])


if __name__ == "__main__":
    app.run(debug=True)
