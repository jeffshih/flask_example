from flask.wrappers import Response
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask import jsonify
from flask import request
from config import *
from dbAdaptor import *




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

'''
Get all recipe and search recipe by ingredient_id
'''
@app.route('/getRecipe', methods=['GET','POST'])
def getRecipe():
    response = {}
    if request.method == 'POST':
        data = request.get_json()
        response['msg'],response['status'] = getRecipeByIngredientID(data)
    response["msg"] ,response['status'] = getAllRecipes()
    return jsonify(response)

'''
Directly get recipe by recipe name
'''
@app.route('/getRecipeByName', methods=['POST'])
def getRecipeByName():
    data = request.get_json()
    response = {}
    response['msg'], response['status'] = getRecipeByCusineName(data)
    return jsonify(response)

'''
Get recipes by ingredients name
'''

@app.route('/getRecipeByIngredientName', methods=['POST'])
def getRecipeByIN():
    data = request.get_json()
    response = {}
    response['msg'], response['status'] = getRecipeByIngredient(data)
    return jsonify(response)
    

'''
create recipe

sending a request like

{
    "name" : "grilled chicken",
    "ingredients" : ["chicken", "salt", "pepper", "parsley"]
}

'''

@app.route('/postRecipe', methods=['POST'])
def postRecipe():
    data = request.get_json()
    response = {}
    #check whether recipe exist
    response['msg'], response['status'] = createRecipe(data)
    #check ingredient exist, if all exist, create recipe with ingredient
    #if not, create ingredient
    return jsonify(response)



@app.route('/postIngredient', methods=['POST'])
def postIngredient():
    data = request.get_json()
    response = {}
    response['msg'],response['status'] = createIngredient(data)
    return jsonify(response)

'''
Currently only support update by name indexing(using fake data)
For future update, if we keep a author column then we can 
have duplicate recipe with same/different ingredients.

request will be like this

{
    "name" : "grilled chicken",
    "ingredients" : ["chicken", "apple", "salt", "pepper"]
}

'''
@app.route('/putRecipe', methods=['PUT'])
def putRecipe():
    data = request.get_json()
    response = {}
    response['msg'],response['status'] = updateRecipe(data)
    return jsonify(response)

'''
Same with update, currently can only retrieve the recipe table
by recipe name, it is very easy to add author column for the user 
only be able to delete the recipe create by him self.

Or other operation like add a catagory column to the recipe,
and will be able to delete like all the Japanese Cusine or some operation like this.
'''

@app.route('/deleteRecipe', methods=['DELETE'])
def deleteRecipe():
    data = request.get_json()
    response = {}
    response['msg'], response['status'] = delRecipe(data)
    return jsonify(response)

'''
testing api for checking update and create and delete
'''
@app.route('/getIngredient',methods=['GET'])
def getAllIngredient():
    response = {}
    response['msg'], response['status'] = getAllIngredient()
    return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)