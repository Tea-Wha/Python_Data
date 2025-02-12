from flask import Flask
from flask_cors import CORS
from data_analysis import gender_data


app = Flask(__name__)
CORS(app, origins=['http://localhost:3000'])

app.add_url_rule('/api/gender/<region>', 'gender_data', gender_data, methods=['GET'])


if __name__ == '__main__':
    app.run(debug=True)