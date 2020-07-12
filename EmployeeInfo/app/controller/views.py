from app import app
from flask import render_template


# 所有路由都跳转到index.html
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')
