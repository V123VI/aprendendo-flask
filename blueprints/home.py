from flask import *
from funcs.hr import obter_hora

home_BP = Blueprint('home', __name__,template_folder='templates')

@home_BP.route('/home',methods=['GET','POST'])
def home():
    username = session.get('username')
    hora_atual = obter_hora()
    return render_template('/home/home.html',username=username)