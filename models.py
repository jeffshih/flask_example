from sqlalchemy.sql.sqltypes import String
from flask_sqlalchemy import SQLAlchemy
import time
import os
import json 



class ingredients(object):

    def __init__(self):
        self.__db = {
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

        self.__reverse = {
            'pasta':1,
            'tomato':2,
            'bacon':3,
            'egg':4,
            'salt':5,
            'pepper':6,
            'apple':7,
            'cheese':8,
            'sugar':9,
            'flour':10
        }
        self.__serialID = 10

    def getIngredientByID(self, id:int):
        try:
            return self.__db[id]
        except KeyError as ex:
            return ("No such key: '%s'" % ex) 
    
    def getIngredientIDByName(self, name:String):
        try:
            return self.__reverse[name]
        except KeyError as ex:
            return ("No such key error: '%s'" % name)

    def checkIngredientExist(self, name):
        try:
            return self.__reverse.get(name) != None
        except KeyError as ex:
            return ("No such key error: '%s'" % name)

    def createIngredient(self, name:String):
        try:        
            if name in self.__reverse:
                raise KeyError
        except KeyError as ex:
            return ("Duplicate key error: '%s'" % name)
        
        self.__serialID += 1
        self.__db[self.__serialID] = name
        self.__reverse[name] = self.__serialID
        return json.dumps({self.__serialID:name})

    def deleteIngredient(self, name:String):
        try:
            rev = self.__reverse[name]
            del self.__db[name]
            del self.__reverse[rev]
            return "delete {} success".format(name)
        except KeyError as ex:
            return ("No such key: '%s'" % ex)

    def getAllIngredient(self):
        return self.__db

class recipe(object):

    '''
    recipe schema:
    id int PK auto_increment /* primary key */
    name varchar(255) /* name of the cusine */
    ingredients 
    create_at
    '''

    def __init__(self):
        self.__db = {
            1:{'pid':1,'name':'spagetti','ingredients':[1,2,3,5,6],'create_at':1617745195,'update_at':int(time.time())},
            2:{'pid':2,'name':'apple pie','ingredients':[7,9,10,4],'create_at':1617745195,'update_at':int(time.time())},
            3:{'pid':3,'name':'carbonara','ingredients':[1,3,4,5,6,8],'create_at':1617745195,'update_at':int(time.time())}
        }

        self.__ingredient = ingredients()
        self.__serialID = 3

    def getRecipeByIngredientID(self, id:int):
        res = []
        try:
            if isinstance(id, str):
                raise ValueError
            for k, v in self.__db.items():
                if id in v['ingredients']:
                    res.append(v)
        except ValueError as e:
            return "Invalid ingredient error id {}".format(id)
        return res


    def getIngredientIDByName(self, ingredientName):
        try:
            id = self.__ingredient.getIngredientIDByName(ingredientName)
        except ValueError as e:
            return "Invalid ingredient"
        return id

    def copyIngredients(self)->ingredients:
        return self.__ingredient

    def getRecipeByKey(self, key):
        return self.__db[key]

    def checkRecipeExist(self, name):
        try:
            for k, v in self.__db.items():
                if name == v["name"]:
                    return True
        except KeyError:
            print("Recipe DB is empty")
            return False
        return False

    def getRecipeKey(self, name):
        for k, v in self.__db.items():
            if name == v["name"]:
                return k
        return 0
        
    def CreateRecipe(self, data):
        try:
            name = data.get('name')
            ingredients = data.get('ingredients')

            #if we use orm or real sql, we can easily do type checking,
            #so here I just do basic checking

            if name == None or ingredients == None:
                raise IndexError
            elif name == "" or len(ingredients) == 0:
                raise ValueError
            for sourceIngredient in ingredients:
                if not self.__ingredient.checkIngredientExist(sourceIngredient):
                    self.__ingredient.createIngredient(sourceIngredient)
            ingredientsID = list(map(self.getIngredientIDByName,ingredients))
        except KeyError as e:
            return "Invalid ingredient '%s'"%e
        except IndexError as e:
            return "Invalid request form '%s'" %e
        except ValueError:
            return "Invalid name or ingredient format"
        self.__serialID +=1
        row = {'pid':self.__serialID,'name':name, 'ingredients':ingredientsID, 'create_at':int(time.time()),'update_at':int(time.time())}
        self.__db[self.__serialID] = row
        return row
        
    def createIngredient(self, name):
        return list(map(self.__ingredient.createIngredient,name))


    def updateRecipe(self, data, key):
        cusine = data["name"]
        self.__db[key]["name"] = cusine
        newIngredients = data["ingredients"]
        try:
            for sourceIngredient in newIngredients:
                if not self.__ingredient.checkIngredientExist(sourceIngredient):
                    self.__ingredient.createIngredient(sourceIngredient)
            ingredientsID = list(map(self.getIngredientIDByName,newIngredients))
        except KeyError as e:
            return "Invalid ingredient '%s'"%e 
        self.__db[key]["ingredients"] = ingredientsID
        self.__db[key]["update_at"] = int(time.time())
        return self.__db[key]

    def deleteRecipe(self, data, key):
        try:
            name = data["name"]
            if self.__db.get(key) == None:
                raise KeyError
        except KeyError as e:
            return "Invalid recipe error {}".format(name)
        del self.__db[key]
        return "Delete {} successfully".format(name)


    def getAllRecipes(self):
        return self.__db

recipes = recipe()
ingredient = recipes.copyIngredients()

if __name__ == "__main__":

    recipeData = {}
    recipeData["name"] = "beef stew"
    recipeData["ingredients"] = ["beef","tomato","wine"]

    ingredientData = {}
    ingredientData["name"] = "wine"
    
    existRecipe = {}
    existRecipe["name"] = "spagetti"
    existRecipe["ingredients"] = ["pasta","tomato","bacon","salt","pepper"]
    print(recipes.checkRecipeExist(existRecipe["name"]))
    tomatoID = recipes.getIngredientIDByName("tomato")
    print(tomatoID)
    print(recipes.getRecipeByIngredientID(tomatoID))
    print(recipes.CreateRecipe(existRecipe))
    print(recipes.CreateRecipe(recipeData))
