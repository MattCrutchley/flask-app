 # import the app object from the ./application/__init__.py
from application import app
from application.models import Posts, Users
 # define routes for / & /home, this function will be called when these are accessed
from flask import render_template, redirect, url_for, request
from application import app, db, bcrypt
from application.models import Posts
from application.forms import PostForm, RegistrationForm, LoginForm, UpdateAccountForm
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/post', methods=['GET', 'POST'])
@login_required
def post():
    form = PostForm()
    if form.validate_on_submit():
        postData = Posts(
            title = form.title.data,
            content = form.content.data,
            author=current_user
        )

        db.session.add(postData)
        db.session.commit()

        return redirect(url_for('home'))

    else:
        print(form.errors)

    return render_template('post.html', title='Post', form=form)

@app.route('/')
@app.route('/home')
def home():
    if current_user.is_authenticated:
        postData = Posts.query.all()
        return render_template('home.html', title='Home',posts = postData)
    else:
        return redirect(url_for('register'))

@app.route('/register',methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_pw = bcrypt.generate_password_hash(form.password.data)

        user = Users(email=form.email.data,first_name = form.first_name.data,last_name = form.last_name.data, password=hash_pw)

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('post'))
    
    return render_template('register.html', title ='Register',form=form)

@app.route('/about')
def about():
    return render_template('about.html', title ='About')

@app.route('/login', methods = ['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user=Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.email.data = current_user.email
    return render_template('account.html', title='Account', form=form)


@app.route("/account/delete", methods=["GET", "POST"])
@login_required
def account_delete():
    user = current_user.id
    account = Users.query.filter_by(id=user).first()
    logout_user()
    user_posts = Posts.query.filter_by(user_id=user).all()
    for post in user_posts:
        db.session.delete(post)
    db.session.delete(account)
    db.session.commit()
    return redirect(url_for('register'))
