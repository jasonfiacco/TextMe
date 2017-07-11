from flask import Flask

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('TEXTME_SETTINGS', silent=True)

from TextMe.views import *

if __name__ == '__main__':
    app.run()
