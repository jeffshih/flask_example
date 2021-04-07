 ## Simple flask api

 ## Run server
 Python version == 3.8.6

 ### Using Docker
 ```shell
 #clone the repo
 $ docker built -t flask_api ./
 $ docker run -d --name apiserver -p 5000:5000 flask_api:latest
 ```

 ### Using virtual env
 ```shell
 #clone the repo
 $ python3 -m venv flask
 $ source flask/bin/activate
 $ pip install -r requirements.txt
 $ python main.py
 ```

 ### Testing
 I have basic unit test in models.py, dbAdaptor.py  
 tester.py is basic testing using python request library.  


 ### Implementation details
 I use mock data to create recipes and ingredients table. 
 If using real sql, my schema will be like

 #### recipes
ID | name | ingredients_id | create_at | update_at
------------ | -------------|------|----|---
1|Spegatti| "[1,2,3,5,6]" | 1617745195 | 1617820049|

ingredients_id will be in json type

 #### ingredients
PID | name | create_at | update_at
------------ | ------|----|---
1|pasta| 1617745195 | 1617820049| 

Use PID as PK and join with recipes.  

