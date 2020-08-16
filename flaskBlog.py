from flask import Flask, escape, request,render_template, url_for
from forms import RegistrationForm, LogInForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '15c85f2447b9d5d24d0d'

posts = [
    {
      'author' : 'Thandar Khine Aye',
      'title' : 'Blog Post 1',
      'content' : 'First Post Content',
      'date_posted' : 'July 24, 2020'   
    },
    {
      'author' : 'Zarni Aung',
      'title' : 'Blog Post 2',
      'content' : 'First Post Content',
      'date_posted' : 'July 25, 2020'   
    }
]
@app.route('/')
@app.route('/home')
def home(name=None):
    return render_template('home.html', name=name, posts=posts)

@app.route('/about')
def about(name=None):
    return render_template('about.html', name=name, title = 'About')

@app.route('/register')
def register(name=None):
    form = RegistrationForm()
    return render_template('register.html', name=name, title = 'Register', form=form)

@app.route('/login')
def login(name=None):
    form =LogInForm()
    return render_template('login.html', name=name, title = 'Log In', form=form)
if __name__ == '__main__':
    app.run(debug=True)