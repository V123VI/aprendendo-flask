from flask import *
from flask_sqlalchemy import SQLAlchemy
from blueprints.home import home_BP
from sqlalchemy.orm import Mapped, mapped_column
from blueprints.login import login_bp
import mysql
from pymysql import *

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # modificação do banco de dados em tempo real = true se não alse)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:29232016@localhost/cadastro3'

db = SQLAlchemy(app)
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(100))
    idade = db.Column(db.Integer)

# with app.app_context():
#     db.create_all()


#selecionar tudo
@app.route('/usuarios',methods=['GET'])
def selecionar_usuarios():
    usuarios_classe = Usuario.query.all()
    print(usuarios_classe)

    return Response()
#selecionar um 
#cadastrar 
#atualizar
#deletar


app.secret_key = ('1')
#blueprintss da home
app.register_blueprint(home_BP)
app.register_blueprint(login_bp)

app.run(debug=True)