from TextMe import app
import os
from .models import db

db.init_app(app)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'
