from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config import *






'''
for real sql connection

db = SQLAlchemy()

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = sqlAlchemyTrack
app.config['SQLALCHEMY_DATABASE_URI'] = sql_uri

db.init_app(app)
'''

app = Flask(__name__)

@app.route('/')
def index():

    sql_cmd = """
    CREATE TABLE Product (
        ProductID int AUTO_INCREMENT PRIMARY KEY,
        ProductName varchar(255) not NULL,
        Catagory varchar(255),
        CatagoryID int,
        CreateOn TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """

    query_data = db.engine.execute(sql_cmd)
    print(query_data)
    return 'ok'


if __name__ == "__main__":
    app.run()