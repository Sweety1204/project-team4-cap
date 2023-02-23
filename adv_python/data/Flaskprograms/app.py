from flask import Flask
myapp=Flask(__name__)
@myapp.route('/')
def hello():
    return 'Hello from my app'
@mpapp.route('/hcl')
def index():
    return "hello from hcl developers"
