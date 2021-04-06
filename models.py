from sqlalchemy.sql.sqltypes import String
from flask_sqlalchemy import SQLAlchemy
import time
import os
import json 

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
            0:{"pid":0,"name":"spagetti","ingredients":[0,1,2,4,5],"create_at":1617745195,"update_at":int(time.time())},
            1:{"pid":1,"name":"apple pie","ingredients":[6,8,9,3],"create_at":1617745195,"update_at":int(time.time())},
            2:{"pid":2,"name":"carbonara","ingredients":[0,2,3,4,5,7],"create_at":1617745195,"update_at":int(time.time())}
        }

        self.__ingredient = ingredients()


    def getRecipeByIngredient(self, id:int):
        res = {}
        for k, v in self.__db.items():
            if id in v['ingredients']:
                res[k] = v
        return json.dumps(res)


    def getIngredientID(self, data):
        ingredients = data['ingredients']
        res = []
        for v in ingredients:
            if self.__ingredient.checkIngredientExist(v): 
                id = self.__ingredient.getIngredientIDByName(v)
                res.append(id)
            

        
    def CreateRecipe(self, data):
        name = data['name']
        ingredients = data['ingredients']
        if name in self.__db['name']:
            return "{} already exist".format(name)
        
    
    def updateRecipe(self, data):
        pass

    def deleteRecipe(self, data):
        pass

    def getAllRecipes(self):
        return self.__db


class ingredients(object):

    def __init__(self):
        self.__db = {
            0:"pasta",
            1:"tomato",
            2:"bacon",
            3:"egg",
            4:"salt",
            5:"pepper",
            6:"apple",
            7:"cheese",
            8:"sugar",
            9:"flour"
        } 

        self.__reverse = {
            "pasta":0,
            "tomato":1,
            "bacon":2,
            "egg":3,
            "salt":4,
            "pepper":5,
            "apple":6,
            "cheese":7,
            "sugar":8,
            "flour":9
        }
        self.__elements = 10

    def getIngredientByID(self, id:int):
        try:
            return self.__db[id]
        except KeyError as ex:
            return ("No such key: '%s'" % ex.message) 
    
    def getIngredientIDByName(self, name:String):
        try:
            return self.__reverse[name]
        except KeyError as ex:
            return ("No such key: '%s'" % ex.message)

    def checkIngredientExist(self, name):
        try:
            return self.__db.get(name) != None
        except KeyError as ex:
            return ("No such key: '%s'" % ex.message)

    def createIngredient(self, name:String):

        try:        
            if name in self.__db:
                raise KeyError
        except KeyError as ex:
            print("Duplicate key: '%s'" % ex.message)
        
        self.__elements += 1
        self.__db[self.__elements] = name
        self.__reverse[name] = self.__elements

    def deleteIngredient(self, name:String):
        try:
            rev = self.__reverse[name]
            del self.__db[name]
            del self.__reverse[rev]
        except KeyError as ex:
            print("No such key: '%s'" % ex.message)
 
recipes = recipe()
