from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def jinja_test():
    a = 'this is a string'
    l = ['a','b','c','d', 1,2,3,4]
    return render_template('home.html', a=a, l=l)

@app.route('/about')
def about_page():
    a = 'this is the about page'
    l = ['about us', 'among us', 'join us', 'aaaaaaabbbout']
    return render_template('about.html', a=a, l=l)

app.run()
