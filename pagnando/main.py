from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = 'Ç&cRet0'
#       mysql://root:jDiXRpxMtwBq0qyfwNvH@containers-us-west-21.railway.app:6681/railway  esse e o servidor do railway
app.config['SQLALCHEMY_DATABASE_URI'] = \
 '{SGBD}://{usuario}:{senha}@{servidor}:{port}/{database}'.format(
    SGBD = 'mysql+mysqlconnector',
    usuario = 'root',
    senha = '12345678',
    servidor = 'localhost',
    port='3306',
    database = 'pagnando'
)

db = SQLAlchemy(app)

class Usuario(db.Model):
    nome = db.Column(db.String(20), nullable=False)
    apelido = db.Column(db.String(10), primary_key=True)
    senha = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name


class Qrcode(db.Model):
    qrcode = db.Column(db.String(4), nullable=False, primary_key=True)
    valor = db.Column(db.DECIMAL(9,2), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name


class Acoes(db.Model):
    id = db.Column(primary_key=True, autoincrement=True)
    apelido = db.Column(db.String(10), nullable=False)
    data = db.Column(db.DateTime, nullable=False)
    acoes = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name
    

from views import *


if __name__ == '__main__':
    app.run(debug=True)

