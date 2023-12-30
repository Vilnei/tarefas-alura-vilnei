from flask import render_template, redirect, url_for, request, flash, session
from main import app, Usuario
from manusear_bd import ler_qrcode, modificar_qrcode


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/autenticar', methods=['GET', 'POST'])
def autenticar():
    usuario = Usuario.query.filter_by(apelido=request.form['usuario']).first()
    if usuario:
            if request.form['senha'] == usuario.senha:
                session['usuario_logado'] = usuario.apelido
                flash(usuario.apelido + ', Logado com sucesso!!!')
                return redirect(url_for('editar'))
            else:
                flash('A senha esta errada GUERREIRO!')
                return redirect(url_for('login'))
    else:
        flash('Xiiiiiiiii deu certo não, tenta de novo')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Usuario Deslogado com sucesso!!!')
    return redirect(url_for('login'))



@app.route('/editar', methods=['GET', 'POST'])
def editar():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        flash('Usuario sem acesso para pagina de EDIÇÃO, por favor fazer LOGIN')
        return redirect('/login?proxima=editar')
    
    else:        
        qrcodes = ler_qrcode()

        if request.method == 'POST':
            qr = request.form.get('qr')
            valorqrcode = request.form.get('valorqrcode_' + qr)

            if valorqrcode is not None and qr is not None:
                modificar_qrcode(qr, valorqrcode)
                qrcodes = ler_qrcode()

        return render_template('editar.html', qrcodes=qrcodes)

@app.route('/tabela')
def tabela():
    return render_template('tabela.html')


@app.route('/<qrcode>', methods=['GET', 'POST'])
def usuario(qrcode):
    valor = ler_qrcode()[qrcode]
    valor_aplicado = request.form.get('valoraplicado')

    if valor_aplicado == None:
        return render_template('usuario.html', qrcode=qrcode, valor=valor)

    else:
        modificar_qrcode(qrcode, valor_aplicado)
        valor = ler_qrcode()[qrcode]
        return render_template('usuario.html', qrcode=qrcode, valor=valor)

