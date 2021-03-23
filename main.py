from flask import Flask, request, redirect, url_for, render_template
import re

app = Flask(__name__)


@app.route('/palindrome/<text>')
def is_palindrome(text):
    stripped = ''.join(re.findall(r'\w+', text)).lower()

    if stripped == stripped[::-1]:
        return f'{text} is a palindrome'
    else:
        return f'{text} is not a palindrome'


@app.route('/reverse/<text>')
def reverse(text):
    return text[::-1]


@app.route('/count/<text>')
def count_words(text):
    return str(len(re.findall(r"(?=\S*['-])([a-zA-Z'-]+)|\w+", text)))


@app.route('/length/<text>')
def length_string(text):
    return str(len(text))


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    elif request.method == 'POST':
        choice = request.form.get('text-choice')

        if choice == 'count':
            return redirect(url_for('count_words', text=request.form.get('user-input')))
        elif choice == 'length':
            return redirect(url_for('length_string', text=request.form.get('user-input')))
        elif choice == 'pdrome':
            return redirect(url_for('is_palindrome', text=request.form.get('user-input')))
        elif choice == 'rv':
            return redirect(url_for('reverse', text=request.form.get('user-input')))


if __name__ == '__main__':
    app.run(debug=True)
