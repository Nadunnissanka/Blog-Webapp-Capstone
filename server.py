from flask import Flask, render_template
from post import Post
import requests

BLOG_API_ENDPOINT = 'https://api.npoint.io/4af156202f984d3464c3'

post_objects_list = []
posts = requests.get(url=BLOG_API_ENDPOINT).json()
for post in posts:
    post_obj = Post(post['id'], post['title'], post['subtitle'], post['body'])
    post_objects_list.append(post_obj)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', all_posts=post_objects_list)


@app.route('/post/<int:index>')
def get_post(index):
    requested_post = None
    for s_post in post_objects_list:
        if s_post.id == index:
            requested_post = s_post
    return render_template('post.html', view_post=requested_post)


if __name__ == '__main__':
    app.run(debug=True)
