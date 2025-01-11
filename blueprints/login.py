from flask import *

login_bp = Blueprint('login',__name__,template_folder='templates')

@login_bp.route('/',methods=['GET','POST'])
def login():
    if request.method =='POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')
        print(usuario)
        print(senha)
        session['username'] = usuario
        return redirect(url_for('home.home'))
    
    return render_template('login/Login.html')