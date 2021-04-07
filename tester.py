import requests
import json
import datetime

from requests.api import post

BaseUrl = 'http://127.0.0.1:5000/'

def postRecipe(data):
    url = BaseUrl+'postRecipe'
    req = requests.post(url, json=data)
    print(req.text)
    print(req.status_code)

def getRecipe():
    url = BaseUrl + 'getRecipe'
    req = requests.get(url)
    print(req.text)
    print(req.status_code)

def getRecipeByIngredient(data):
    url = BaseUrl + 'getRecipe'
    req = requests.post(url, json=data)
    print(req.text)
    print(req.status_code)

def getRecipeByName(data):
    url = BaseUrl + 'getRecipeByName'
    req = requests.post(url, json=data)
    print(req.text)
    print(req.status_code)

def getRecipeByIngredientName(data):
    url = BaseUrl + 'getRecipeByIngredientName'
    req = requests.post(url, json=data)
    print(req.text)
    print(req.status_code)


def putRecipe(data):
    url = BaseUrl + 'putRecipe'
    req = requests.put(url, json=data)
    print(req.text)
    print(req.status_code)

def deleteRecipe(data):
    url = BaseUrl + 'deleteRecipe'
    req = requests.delete(url, json=data)
    print(req.text)
    print(req.status_code)

def postIngredient(data):
    url = BaseUrl + 'postIngredient'
    req = requests.post(url, json=data)
    print(req.text)
    print(req.status_code)



if __name__ == "__main__":
    

    '''
    mock data for ingredient
    {
            1:'pasta',
            2:'tomato',
            3:'bacon',
            4:'egg',
            5:'salt',
            6:'pepper',
            7:'apple',
            8:'cheese',
            9:'sugar',
            10:'flour'
    } 
    '''


    #standard recipe request(human are not able to know the ingredient id)
    data = {"name":"spagetti","ingredients":["pasta","bacon","tomato","salt","pepper"]}
    

    recipeData = {}
    recipeData["name"] = "beef stew"
    recipeData["ingredients"] = ["beef","tomato","wine"]

    invalidRecipe1 = {"Name":10, "ingredients":[]}
    invalidRecipe2 = {"name":10, "ingredients":["potato"]}
    invalidRecipe3 = {"name":"", "ingredients":["potato"]}

    wine = {}
    wine["name"] = ""
    wine["ingredients"] = ["wine"]

    listIngredient = {"ingredients":["tea","orange","paprika"]}

    existIngredient = {}
    existIngredient["ingredients"] = ["bacon"]
    
    '''
    query for recipe, support query by recipe name, ingredient name
    and ingredients_id.

    Cause we are using dummy hard coded db, so only support single id query 
    which can be easily done by join two tables if we use sql or orm.
    '''
    recipeQuery = {}
    recipeQuery["name"] = "carbonara"
    recipeQuery["ingredients"] = ["pasta"]
    recipeQuery["ingredients_id"] = 0

    '''
    recipe query contains name and ingredients
    
    since I assume human is hard to read ingredients_id
    '''
    existRecipe = {}
    existRecipe["name"] = "spagetti"
    existRecipe["ingredients"] = ["pasta","tomato","bacon","salt","pepper"]
    
    grilledChicken = {"name":"grilled chicken", "ingredients":["chicken", "salt", "pepper", 
                    "butter", "herb", "paprika"]}

    newBeefStew = {"name":"beef stew", "ingredients":["potato","beef","tomato","carrot","wine"]}

    #create spagetti
    postRecipe(data)

    #create beef stew
    postRecipe(recipeData)

    #test invalid input for create Recipe
    postRecipe(invalidRecipe1)
    postRecipe(invalidRecipe2)
    postRecipe(invalidRecipe3)

    #search by valid ingredient 


    #search by invalid ingredient wine
    getRecipeByIngredient(wine)

    #create ingredient wine
    postIngredient(wine)

    #search by exist ingredient wine
    getRecipeByIngredient(wine)

    #create exist ingredient
    postIngredient(existIngredient)

    #create a list of ingredient
    postIngredient(listIngredient)

    #update exist recipe
    putRecipe(existRecipe)

    #update inexist recipe
    putRecipe(grilledChicken)

    #update new beef stew
    putRecipe(newBeefStew)

    #get new beefstew
    getRecipeByName(newBeefStew)

    #delete beefstew

    deleteRecipe(newBeefStew)

    #delete beefstew again
    
    deleteRecipe(newBeefStew)


