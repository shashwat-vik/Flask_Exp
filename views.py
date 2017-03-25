from flask import render_template, request, redirect, url_for
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from app import app
from models import *

@app.route("/", methods=['POST', 'GET'])
def homepage():
    if request.method == 'POST':
        name = request.form['name']
        number = request.form['number']
        if not session.query(Customer).filter_by(name=name).all():
            cs = Customer(name=name, number=number)
            session.add(cs)
            session.commit()
        return redirect(url_for('customers'))
    else:
        return render_template("user_input.html")

@app.route("/customers")
def customers():
    users = session.query(Customer).all()
    return render_template("display_users.html", users=users)
