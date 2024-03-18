from flask import Flask, render_template, session, redirect, request
from flask_app import app
from flask_app.models.user import User
from flask_app.models import message
from flask import flash

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    valid_user = User.create_valid_user(request.form)

    if not valid_user:
        return redirect("/")
    
    session["user_id"] = valid_user.id
    
    return redirect("/dashboard")

@app.route("/login", methods=["POST"])
def login():
    valid_user = User.authenticated_user_by_input(request.form)
    if not valid_user:
        return redirect("/")

    session["user_id"] = valid_user.id
    return redirect("/dashboard")

@app.route("/dashboard")
def dashboard():
    if 'user_id' not in session:
        return redirect('/')

    user = User.get_by_id(session['user_id'])
    messages = message.Message.get_user_messages(session['user_id'])

    users = User.get_all()
    return render_template("dashboard.html",user=user,users=users,messages=messages)


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")