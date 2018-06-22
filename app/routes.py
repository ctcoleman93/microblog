from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel' }
    posts = [
        {
            'author':{'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Anon'},
            
            'body': 'Who likes cock in their a$$?!'
        },
        {
            'author': {'username': 'browntown43'},
            'body': 'Shit cock porn! .10/gig! Today only!'
        },
        {
            'author': {'username': 'admin'},
            'body': 'All inappropriate comments will be rewarded!'
        }
    ]
    return render_template('index.html', title='Home', user = user, posts=posts)
