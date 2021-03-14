from flask import Flask, request, redirect, url_for, render_template
import re

app = Flask(__name__)


@app.route('/palindrome/<word>')
def is_palindrome(word):
    if word == word[::-1]:
        return f'{word} is a palindrome'
    else:
        return f'{word} is not a palindrome'


@app.route('/reverse/<text>')
def reverse(text):
    return text[::-1]


@app.route('/count/<text>')
def count_words(text):
    return str(len(re.findall(r'\w+', text)))


@app.route('/length/<word>')
def length_string(word):
    return str(len(word))


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        choice = request.form.get('text-choice')

        if choice == 'count':
            return redirect(url_for('count_words', text=request.form.get('user-input')))
        elif choice == 'length':
            return redirect(url_for('length_string', word=request.form.get('user-input')))
        elif choice == 'pdrome':
            return redirect(url_for('is_palindrome', word=request.form.get('user-input')))
        elif choice == 'rv':
            return redirect(url_for('reverse', text=request.form.get('user-input')))
    else:
        return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
