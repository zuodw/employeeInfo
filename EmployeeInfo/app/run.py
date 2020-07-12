from flask_cors import CORS
from app import app
from app.controller import api
from app.controller import views

if __name__ == '__main__':
    CORS(app, suppors_credentials=True)

    app.run(host='0.0.0.0', debug=True)
