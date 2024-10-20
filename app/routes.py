# app/routes.py
from flask import render_template, redirect, url_for, flash, request
from .__init__ import app, db
from app.models import Usuario, Artefato

@app.route('/')
def index():
    return render_template('catalog.html', artefatos=Artefato.query.all())

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        user = Usuario.query.filter_by(email=email, senha=senha).first()
        if user:
            return redirect(url_for('index'))
        else:
            flash('Login inválido')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        senha = request.form['senha']
        user = Usuario(nome=nome, email=email, telefone=telefone, senha=senha)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/catalog')
def catalog():
    artefatos = Artefato.query.all()
    return render_template('catalog.html', artefatos=artefatos)
