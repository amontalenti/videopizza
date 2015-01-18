from flask import Flask, render_template, request, redirect, abort
from flask.ext.script import Manager
from filters import human_date

app = Flask(__name__, static_folder="../static", static_url_path="/static")
app.debug = True
app.add_template_filter(human_date)


@app.route('/')
def index():
    articles = []
    return render_template('index.jinja2.html',
                           rows=articles,
                           page_links="active")


manager = Manager(app)

if __name__ == "__main__":
    manager.run()
