from jogoteca import app
from flask import render_template, request, redirect, session, flash, url_for
from models import Usuarios
from helpers import FormUser
from flask_bcrypt import check_password_hash


@app.route('/login')
def login():
    form = FormUser()
    return render_template('login.html', form = form)


@app.route('/autenticar', methods=['POST'])
def autenticar():
    form = FormUser(request.form)
    usuario = Usuarios.query.filter_by(nickname=form.nickname.data).first()
    senha = check_password_hash(usuario.senha, form.senha.data)
    if usuario and senha:
        session['usuario_logado'] = form.nickname.data
        flash(usuario.nickname + " Usuário logado")
        return redirect(url_for('novo'))
    else:
        flash("Usuário não logado")
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash("Logout Realizado com sucesso!")
    return redirect(url_for("index"))
    
