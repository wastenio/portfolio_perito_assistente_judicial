from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'

# Configurações do Flask-Mail (exemplo Gmail)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'wastenio.silva@gmail.com'        # seu e-mail
app.config['MAIL_PASSWORD'] = 'fikagrandeporra'        # sua senha ou app password
app.config['MAIL_DEFAULT_SENDER'] = ('Portfólio Perito', app.config['MAIL_USERNAME'])

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/servicos')
def servicos():
    return render_template('servicos.html')

@app.route('/quesitos')
def quesitos():
    return render_template('quesitos.html')

@app.route('/estudos')
def estudos():
    return render_template('estudos.html')

@app.route('/laudos')
def laudos():
    laudos = [
        {
            'titulo': 'Laudo Grafotécnico – Confronto de Assinaturas',
            'descricao': 'Análise comparativa entre assinaturas duvidosas e padrões autênticos para verificação de autenticidade.',
            'arquivo': None
        },
        {
            'titulo': 'Identificação de Falsificação por Imitação',
            'descricao': 'Laudo técnico que identifica tentativa de falsificação por imitação lenta ou traçado forçado.',
            'arquivo': None
        },
        {
            'titulo': 'Análise de Padrão Caligráfico',
            'descricao': 'Estudo detalhado do padrão gráfico de um indivíduo, com base em elementos como pressão, inclinação, espaçamento e ritmo da escrita.',
            'arquivo': None
        }
    ]
    return render_template('laudos.html', laudos=laudos)


@app.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        mensagem = request.form.get('mensagem')

        if not nome or not email or not mensagem:
            flash('Por favor, preencha todos os campos.', 'danger')
            return redirect(url_for('contato'))

        try:
            corpo_email = f'''
            Nova mensagem de contato no site:

            Nome: {nome}
            Email: {email}
            Mensagem:
            {mensagem}
            '''

            msg = Message(subject='Contato pelo site - Portfólio Perito',
                          body=corpo_email,
                          recipients=[app.config['MAIL_USERNAME']])
            mail.send(msg)
            flash('Mensagem enviada com sucesso! Entrarei em contato em breve.', 'success')
        except Exception as e:
            print(f'Erro ao enviar e-mail: {e}')
            flash('Erro ao enviar mensagem. Tente novamente mais tarde.', 'danger')

        return redirect(url_for('contato'))

    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)
