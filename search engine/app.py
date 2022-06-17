from flask import Flask, render_template, request
from searchengine import search

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/research', methods=['GET', 'POST'])
def research():
    if request.method == 'POST':
        text = request.form['search']
        return render_template('home.html', len=len(search(text)), data=search(text))

    else:
        return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)















