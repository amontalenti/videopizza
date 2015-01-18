from flask import Flask, render_template, request
from rapid import (top_articles, search_articles, insert_article)

app = Flask(__name__, static_folder="../static", static_url_path="/static")

@app.route('/')
def index():
    articles = top_articles()
    return render_template('index.jinja2.html', 
                           rows=articles)

@app.route('/search/<query>')
def search(query):
    articles = search_articles(query)
    return render_template('index.jinja2.html', 
                           query=query, 
                           articles=articles)

@app.route('/submit/', methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        return do_submit()
    else:
        return render_template('submit.jinja2.html')

def do_submit():
    article = insert_article()
    return render_template("inserted.jinja2.html", article=article)

def run_devserver():
    app.run(debug=True)

if __name__ == "__main__":
    run_devserver()
