from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask import jsonify
from flask import request
from config import *
from models import *




'''
for real sql connection
'''
'''
db = SQLAlchemy()

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = sqlAlchemyTrack
app.config['SQLALCHEMY_DATABASE_URI'] = sql_uri

db.init_app(app)
'''
app = Flask(__name__)
#api = Api(app)


@app.route('/')
def index():    
    return 'ok'

@app.route('/getRecipe', methods=['GET','POST'])
def getRecipe():
    if request.method == 'POST':
        data = request.get_json()
        res = recipes.getRecipeByIngredient(data)
        return jsonify(res)
    return jsonify(recipes.getAllRecipes())

@app.route('/postRecipe', methods=['POST'])
def postRecipe():
    data = request.get_json()

    


if __name__ == "__main__":
    app.run()