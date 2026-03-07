from flask import Blueprint, request, redirect, url_for, render_template, session
from database.db import db
from models_db.user_model import User
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # check if user already exists
        existing_user = User.query.filter_by(username=username).first()

        if existing_user:
            return "Username already exists. Please choose another."
        hashed_password = generate_password_hash(password)
        user = User(username=username, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("auth.login"))
    return render_template("register.html")

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session["user"] = username
            return redirect("/dashboard")
        return "Invalid credentials"
    return render_template("login.html")