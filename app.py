from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Modelo da Moto
class Moto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    placa = db.Column(db.String(10), unique=True, nullable=False)
    modelo = db.Column(db.String(50), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    defeitos = db.Column(db.String(500), nullable=True)
    pecas_faltando = db.Column(db.String(500), nullable=True)

# Rota principal
@app.route('/')
def index():
    motos = Moto.query.all()
    return render_template('index.html', motos=motos)

# Rota para cadastrar uma nova moto
@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        placa = request.form['placa']
        modelo = request.form['modelo']
        ano = request.form['ano']
        defeitos = request.form['defeitos']
        pecas_faltando = request.form['pecas_faltando']

        nova_moto = Moto(placa=placa, modelo=modelo, ano=ano, defeitos=defeitos, pecas_faltando=pecas_faltando)
        db.session.add(nova_moto)
        db.session.commit()

        return redirect(url_for('index'))
    return render_template('cadastro.html')

# Rota para ver detalhes de uma moto
@app.route('/detalhes/<int:id>')
def detalhes(id):
    moto = Moto.query.get_or_404(id)
    return render_template('detalhes.html', moto=moto)

# Inicialização do banco de dados
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)