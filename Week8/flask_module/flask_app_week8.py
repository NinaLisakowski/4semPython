#1. Create a python notebook, and make the proper setup with pandas/numpy & sqlalchemy, to persist all 200 people from the .csv file.
#2. Make a simple flask server with one, get endpoint /flask_app/.
#    1. Make it write Hello World.
#3. Use the Flask extended start code from day 08-2 Web services, and make the following endpoints:
#    1. /api/showAll
#    2. /api/employee/<string: firstName>/<string: lastName>
#    3. /api/employee/add
#    4. /api/employee/delete
#    5. /api/employee/update
#4. Test endpoints in Postman.
#5. Test the class from the .py file in CLI.
from flask import Flask, jsonify, abort, request
from sqlalchemy.types import Integer, Text
import sqlalchemy as s_a
import pandas as pd

app = Flask(__name__)

@app.route('/flask_app/')
def index():
    return 'Hello world! Flask server week 8'


######################### /api/showAll #########################
@app.route('/api/showAll', methods=['GET'])
def showAll():
    SQLALCHEMY_DATABASE_URL = 'mysql+mysqlconnector://root:root@db/db'
    engine = s_a.create_engine(SQLALCHEMY_DATABASE_URL)
    sql_df = pd.read_sql("SELECT * FROM week8PeopleEx",con=engine)
    result = sql_df.to_html()
    return result


######################### /api/employee/<string: firstName>/<string: lastName> #########################
@app.route('/api/employee/<string:firstName>/<string:lastName>', methods=['GET'])
def getEmployeeWithName(firstName, lastName):
    SQLALCHEMY_DATABASE_URL = 'mysql+mysqlconnector://root:root@db/db'
    engine = s_a.create_engine(SQLALCHEMY_DATABASE_URL)
    sql_df = pd.read_sql("SELECT * FROM week8PeopleEx WHERE `First Name`='{}' AND `Last Name`='{}'".format(firstName, lastName), con=engine)
    result = sql_df.to_html()
    if not result:
        abort(404)
    return result


######################### /api/employee/add #########################
@app.route('/api/employee/add', methods=['POST'])
def add_employee():
    if not request.json or not 'First Name' and 'Last Name' in request.json:
        abort(400)
    person = {
        'First Name': request.json['First Name'],
        'Last Name': request.json['Last Name'],
        'Gender': request.json['Gender'],
        'Age': request.json['Age'],
        'Email': request.json['Email'],
        'Phone': request.json['Phone'],
        'Occupation': request.json['Occupation'],
        'Salary': request.json['Salary'], 
    }
    df = pd.json_normalize(person)
    SQLALCHEMY_DATABASE_URL = 'mysql+mysqlconnector://root:root@db/db'
    engine = s_a.create_engine(SQLALCHEMY_DATABASE_URL)
    df.to_sql(
        "week8PeopleEx",
        engine,
        if_exists="append",
        index=False,
        dtype={
            "First Name": Text,
            "Last Name": Text,
            "Gender": Text,
            "Age": Integer,
            "Email": Text,
            "Phone": Text,
            "Occupation": Text,
            "Salary": Integer,
        })
    return jsonify({'Added person': person}), 201


######################### /api/employee/delete #########################
@app.route('/api/employee/delete', methods=['DELETE'])
def delete_employee():
    if not request.json or not 'First Name' and 'Last Name' in request.json:
        abort(400)
    firstName = request.json['First Name']
    lastName = request.json['Last Name']
    sql_query = "DELETE FROM week8PeopleEx WHERE `First Name`='{}' AND `Last Name`='{}'".format(firstName, lastName)
    SQLALCHEMY_DATABASE_URL = 'mysql+mysqlconnector://root:root@db/db'
    engine = s_a.create_engine(SQLALCHEMY_DATABASE_URL)
    conn = engine.connect()
    trans = conn.begin()
    try:
        conn.execute(sql_query)
        trans.commit()
    except:
        trans.rollback()
        raise
    finally:
        conn.close()
    return jsonify({"Deleted person": [firstName, lastName]}), 201 

######################### /api/employee/update #########################
@app.route('/api/employee/update', methods=['PUT'])
def update_employee():
    if not request.json or not 'First Name' and 'Last Name' in request.json:
        abort(400)
    update_person = {
        'First Name': request.json['First Name'],
        'Last Name': request.json['Last Name'],
        'Gender': request.json['Gender'],
        'Age': request.json['Age'],
        'Email': request.json['Email'],
        'Phone': request.json['Phone'],
        'Occupation': request.json['Occupation'],
        'Salary': request.json['Salary'], 
    }

    #First Name and Last Name has to be last in the .format()
    sql_query = "UPDATE week8PeopleEx SET Gender='{}', Age='{}', Email='{}', Phone='{}', Occupation='{}', Salary='{}' WHERE `First Name`='{}' AND `Last Name`='{}'".format(update_person['Gender'], update_person['Age'], update_person['Email'], update_person['Phone'], update_person['Occupation'], update_person['Salary'], update_person['First Name'], update_person['Last Name'])
    SQLALCHEMY_DATABASE_URL = 'mysql+mysqlconnector://root:root@db/db'
    engine = s_a.create_engine(SQLALCHEMY_DATABASE_URL)
    conn = engine.connect()
    trans = conn.begin()
    try:
        conn.execute(sql_query)
        trans.commit()
    except:
        trans.rollback()
        raise
    finally:
        conn.close()
    return jsonify({"Updated person": update_person}), 201 

if __name__ == '__main__':
    app.run(debug=True)
    