from flask import Flask, render_template, request, redirect
import json, os

app = Flask(__name__)
POSTS_FILE = 'posts.json'

# Load posts from file
def load_posts():
    if not os.path.exists(POSTS_FILE):
        return []
    with open(POSTS_FILE, 'r') as f:
        return json.load(f)

# Save posts to file
def save_posts(posts):
    with open(POSTS_FILE, 'w') as f:
        json.dump(posts, f, indent=4)

# Home page: show all posts
@app.route('/')
def index():
    posts = load_posts()
    return render_template('index.html', posts=posts)

# New post page: form to create post
@app.route('/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        posts = load_posts()
        posts.append({'title': title, 'content': content})
        save_posts(posts)
        return redirect('/')
    return render_template('new.html')

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use Render port or default 5000 locally
    app.run(host="0.0.0.0", port=port, debug=True)


