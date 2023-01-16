import os
from jogoteca import app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators

class FormJogo(FlaskForm):
    nome = StringField('Nome do jogo', [validators.DataRequired(), validators.Length(min= 1, max = 50)])
    categoria = StringField('Categoria do jogo', [validators.DataRequired(), validators.Length(min=1, max = 40)])
    console = StringField('Console do jogo', [validators.DataRequired(), validators.Length(min=1, max = 20)])
    salvar = SubmitField("Salvar")


class FormUser(FlaskForm):
    nickname = StringField("Nick no usuário", [validators.DataRequired(), validators.Length(min = 1, max = 8)])
    senha = PasswordField("Senha", [validators.DataRequired(), validators.Length(min = 1, max = 100)])
    login = SubmitField("Login")
def recupera_id(id):
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
        if f'capa{id}' in nome_arquivo:
            return nome_arquivo
    
    return 'chield.jpg'


def deleta_arquivo(id):
    arquivo = recupera_id(id)

    if arquivo != 'chield.jpg':
        os.remove(os.path.join(app.config['UPLOAD_PATH'],arquivo))
