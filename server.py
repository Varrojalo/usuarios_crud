from flask_app import app
from flask_app.controllers.usuarios import *


# Server execution
if __name__=='__main__':
    app.run(debug=True)