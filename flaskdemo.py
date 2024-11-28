from flask import Flask, render_template, request, redirect, url_for, session
import wikipedia

app = Flask(__name__)
# Set the secret key. Keep this really secret:
app.secret_key = 'IT@JCUA0Zr98j/3yXa R~XHH!jmN]LWX/,?RT'


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/secret')
def secret():
    text = " ".join(["Hello Lindsay "] * 999)
    return render_template("secret.html", text=text)


@app.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        session['search_term'] = request.form['search']
        return redirect(url_for('results'))
    return render_template("search.html")


@app.route('/results')
def results():
    search_term = session['search_term']
    page = get_page(search_term)
    if type(page) == str:
        return render_template(page)
    return render_template("results.html", page=page)


def get_page(search_term):
    try:
        page = wikipedia.page(search_term, auto_suggest=False)
    except wikipedia.exceptions.PageError:
        page = "no_results.html"
    except wikipedia.exceptions.DisambiguationError:
        page = "too_many_results.html"
    return page


if __name__ == '__main__':
    app.run()
