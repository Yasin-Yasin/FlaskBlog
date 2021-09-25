from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

# Instance of Flask Class
app = Flask(__name__)

# To Stop cross site attack etc.
app.config['SECRET_KEY'] = 'e3b9eb85f9f17f1bdbca42e072483abc' # import secrets secrets.token_hex(16) to get random string

posts = [
    {
        'author' :  'Corey Schafer',
        'title' : 'Blog Post 1',
        'content' : 'First Post Content',
        'date_posted' : 'April 20, 2021'

    },
    {
        'author' :  'Jane Doe',
        'title' : 'Blog Post 2',
        'content' : 'Second Post Content',
        'date_posted' : 'August 3, 2021'

    }
]

# Routes

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts) # first posts is variable and we will have access of this variable in our template

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm() # Instance RegisterForm class 
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm() # Instance RegisterForm class 
    return render_template('login.html', title='Login', form=form)

# It will allow to run this like normal python file instead of flask run 
if __name__ == '__main__':
    app.run(debug=True)


# Imports
# Flask CLass
# render_template() function from flask to render html templates
# url_for - For url , location of file in directory
# flask_wtf - registration form etc
# from forms import RegistrationForm, LoginForm -  from forms.py file that we created
# flash - for flash messages
# redirect - redirect user to home page after registration