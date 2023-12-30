import mysql.connector



def conetar_bd():
    conexao = mysql.connector.connect(
            host='127.0.0.1',
            port='3306',
            user='root',
            password='12345678',
            database='pagnando'
      )
    return conexao

def criar_qrcode(qrcode,valor):
    conexao = conetar_bd()
    cursor = conexao.cursor()
    comando = f'INSERT INTO qrcode (qrcode, valor) VALUES ("{qrcode}", {valor})'
    cursor.execute(comando)
    conexao.commit()
    cursor.close()
    conexao.close()


def criar_usuario(nome, apelido, senha):
    conexao = conetar_bd()
    cursor = conexao.cursor()
    comando = f'INSERT INTO qrcode (nome, apelido, senha) VALUES ("{nome}", "{apelido}", "{senha}")'
    cursor.execute(comando)
    conexao.commit()
    cursor.close()
    conexao.close()


def ler_qrcode():
    conexao = conetar_bd()
    cursor = conexao.cursor()
    comando = f'SELECT * FROM qrcode'
    cursor.execute(comando)
    resultado = cursor.fetchall()#?---------------------- esse valor vem em uma lista(tuplas)
    dicionario = dict((x, y) for x, y in resultado)#?-----aqui transformamos ele de lista(tuplas) > dicionario{key:valor}
    return dicionario


def ler_usuario():
    conexao = conetar_bd()
    cursor = conexao.cursor()
    comando = f'SELECT * FROM usuarios'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    return resultado


def modificar_qrcode(qrcode,valor):
    conexao = conetar_bd()
    cursor = conexao.cursor()
    comando = f'UPDATE qrcode SET valor = {valor} WHERE qrcode = "{qrcode}"'
    cursor.execute(comando)
    conexao.commit()
    cursor.close()
    conexao.close()


def modificar_senha_usuario(apelido, senha):
    conexao = conetar_bd()
    cursor = conexao.cursor()
    comando = f'UPDATE vendas SET senha = {senha} WHERE apelido = "{apelido}"'
    cursor.execute(comando)
    conexao.commit()
    cursor.close()
    conexao.close()


def deletar_qrcode(qrcode):
    conexao = conetar_bd()
    cursor = conexao.cursor()
    comando = f'DELETE FROM vendas WHERE qrcode = "{qrcode}"'
    cursor.execute(comando)
    conexao.commit()
    cursor.close()
    conexao.close()


def deletar_usuario(apelido):
    conexao = conetar_bd()
    cursor = conexao.cursor()
    comando = f'DELETE FROM vendas WHERE qrcode = "{apelido}"'
    cursor.execute(comando)
    conexao.commit()
    cursor.close()
    conexao.close()
