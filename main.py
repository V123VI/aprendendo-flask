from flask import *
from blueprints.home import home_BP
from blueprints.login import login_bp
app = Flask(__name__)

app.secret_key = ('1')
#blueprintss da home
app.register_blueprint(home_BP)
app.register_blueprint(login_bp)

app.run(debug=True)