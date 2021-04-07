from models import *


def getRecipeByIngredient(data):
    '''
    here if using real sql or orm, we can easily join a table 
    for querying a list of ingredient and return the recipe contains 
    the ingredient
    '''

    try:
        sourceIngredientName = data["ingredients"][0]
        ingredientID = recipes.getIngredientIDByName(sourceIngredientName)
        if isinstance(ingredientID, str):
            raise ValueError
    except KeyError as e:
        return "Invalid ingredient format or key value '%s'" % e, False
    except ValueError as e:
        return "Ingredient does not exist '%s'" % e, False
    return recipes.getRecipeByIngredientID(ingredientID), True

def getRecipeByIngredientID(data):

    '''
    Same here, we can join recipe table with ingredient table using 
    ingredients_id as foreign key.

    Another implementation is creating the third table to keep the 
    recipe_ingredient mapping, like

    r_id, i_id
    1,      1
    1,      2
    1,      3
    1,      5

    this table will grow very fast but enable faster bi-directional lookup

    '''
    try:
        ingredientsID = data["ingredients_id"][0]
        res = recipes.getRecipeByIngredientID(ingredientsID)
        if "error" in res:
            raise ValueError
    except KeyError:
        return "Invalid argument, no ingredients_id", False
    except ValueError as e:
        return "Ingredient does not exist '%s'" % e, False 
    return res, True

def getRecipeByCusineName(data):
    if checkRecipeExist(data):
        key = recipes.getRecipeKey(data['name'])
        return recipes.getRecipeByKey(key), True
    return "Invalid recipe names", False


def getAllRecipes():
    return recipes.getAllRecipes(), True

def checkRecipeExist(data):
    try:
        recipeName = data["name"]
    except KeyError as e:
        print("Invalid data input")
        return False
    return recipes.checkRecipeExist(recipeName)

def createRecipe(data):
    return ("Recipe already exist", False) if checkRecipeExist(data) else (recipes.CreateRecipe(data), True)

def createIngredient(data):
    res = recipes.createIngredient(data["ingredients"])
    return (res, False) if "error" in res else (res, True)

def updateRecipe(data):
    if checkRecipeExist(data):
        key = recipes.getRecipeKey(data["name"])
        res = recipes.updateRecipe(data,key)
        return res, True
    return "Recipe doesn't exist, update failed", False

def delRecipe(data):
    if checkRecipeExist(data):
        key = recipes.getRecipeKey(data["name"])
        res = recipes.deleteRecipe(data,key)
        return res, True 

    return "Recipe doesn't exist, delete failed", False


def getAllIngredient():
    return ingredient.getAllIngredient(), True

if __name__ == "__main__":
    recipeData = {}
    recipeData["name"] = "beef stew"
    recipeData["ingredients"] = ["beef","tomato","wine"]

    ingredientData = {}
    ingredientData["ingredients"] = ["wine","tea","paprika"]

    existIngredient = {}
    existIngredient["ingredients"] = ["bacon"]
    
    recipeQuery = {}
    recipeQuery["name"] = "carbonara"
    recipeQuery["ingredients"] = ["pasta"]
    recipeQuery["ingredients_id"] = [0]

    existRecipe = {}
    existRecipe["name"] = "spagetti"
    existRecipe["ingredients"] = ["pasta","tomato","bacon","salt","pepper"]
    
    
    print(getRecipeByIngredient(recipeQuery))
    print(getRecipeByIngredientID(recipeQuery))
    print(getRecipeByCusineName(recipeQuery))
    
    print(checkRecipeExist(existRecipe))
    print(checkRecipeExist(recipeData))
    print(createRecipe(existRecipe))
    #print(createRecipe(recipeData))
    print(createIngredient(existIngredient))
    print(updateRecipe(recipeData))
    print(updateRecipe(existRecipe))
    print(deleteRecipe(recipeData))
    print(deleteRecipe(recipeData))
    print(deleteRecipe(existRecipe))
    print(deleteRecipe(existRecipe))
    
    #print(createIngredient(ingredientData))