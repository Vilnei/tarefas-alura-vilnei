from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, DecimalField, DateTimeField, validators


class Formularios(FlaskForm):
    nome = StringField('Nome', [validators.InputRequired(), validators.Length(min=1, max=20)])
    apelido = StringField('Apelido', [validators.InputRequired(), validators.Length(min=1, max=10)])
    qrcode = IntegerField('Qrcode', [validators.InputRequired(), validators.Length(min=4, max=4)])
    valor = DecimalField('Valor', [validators.InputRequired(), validators.Length(min=3,max=11)], places=2)
    data = DateTimeField(format='%d-%m-%Y %H:%M')
    acoes = StringField()
    senha = PasswordField('Senha', [validators.InputRequired(), validators.EqualTo('confirma', 'A senha devem ser iguais')])
    confirma = PasswordField('Repita a Senha')
    salvar = SubmitField('Salvar')
