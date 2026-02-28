from flask import Flask, render_template, request
import datetime

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    age = None
    current_year = datetime.datetime.now().year

    if request.method == 'POST':
        try:
            birth_year = int(request.form['birth_year'])
            age = current_year - birth_year
        except (ValueError, KeyError):
            age = "Fadlan gali nambar sax ah."

    return render_template('index.html', age=age)


if __name__ == '__main__':
    app.run(debug=True)
