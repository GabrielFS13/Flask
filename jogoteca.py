from flask import Flask, render_template, request, redirect, session, flash, url_for


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha

jogo1 = Jogo("GOW", "Ação", "Ps4")
jogo2 = Jogo("Fortnite", "Battle Royale", "XBOX/PS4/PC")
jogo3 = Jogo("The Last of Us", "Ação Drama", "PS3-PS4")

user1 = Usuario("Gabriel", 'FalcãoSZ', '123')
user2 = Usuario('Vitor', 'VTC', 'senha')

usuarios = { user1.nickname: user1,
             user2.nickname: user2,
           }

lista = [jogo1,jogo2,jogo3]

app = Flask(__name__)
app.secret_key = 'chavesupersecreta'

@app.route('/')
def index():
    return render_template("lista.html", titulo = "Jogassso", lista = lista)


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo = 'Cadastre um novo Jogo')


@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect(url_for('index'))


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/autenticar', methods=['POST'])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = request.form['usuario']
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
    
    
app.run(debug=True)