import flask  
import json
from flask import request, jsonify
from AnimalClasses import *

###########id, cutomer_name, pet_name, color, age, speed, weight
Garfield = Cat(0, "Ahmed", "Garfield", "Brown", 5, 20, 20)
PandaBear = Panda(1, "Jack", "Kung Fu Panda", "Black and white", 3, 10, 60)
Parrot = Bird(2, "Alice", "Parrot", "Blue", 7, 30, 2)
Sparky = Dog(3, "Zoe", "Sparky", "Black", 6, 15, 50)

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our program.  
# In the real world we would want this to 
# be made or come from another source such 
# as a database

GarfieldJSON = Garfield.__dict__
PandaBearJSON = PandaBear.__dict__
ParrotJSON = Parrot.__dict__
SparkyJSON = Sparky.__dict__

PetOwners = [GarfieldJSON, PandaBearJSON, ParrotJSON, SparkyJSON]
print(PetOwners)
# txtfile = open("rawJSON.txt", "r")
# PetOwners = txtfile.read()

@app.route('/', methods=['GET'])    #tell which HTTP method we are using (GET) and what route (extra bit of the URL) this method will be activated on.  In this case nothing and so home
def home():
    return "<h1>Welcome to Gareth's virtual lesson</h1><p>Sorry I am still ill.</p>" #what the api returns


# A route to return all of the available entries in our collection of pet owners.
@app.route('/api/somearea/vetcustomers/all', methods=['GET'])
def api_all():
    return jsonify(PetOwners)

@app.route('/api/somearea/vetcustomers', methods=['GET'])
def get_owner_by_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: You are an idiot."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for PetOwner in PetOwners:
        if PetOwner['id'] == id:
            results.append(PetOwner)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

@app.route('/api/somearea/vetcustomers/pet-type', methods=['GET'])
def get_owner_by_type():
    # Check if a pet type was provided as part of the URL.
    # If a pet type is provided, assign it to a variable.
    # If no pet type is provided, display an error in the browser.
    if 'petType' in request.args:
        petType = request.args['petType']
    else:
        return "Error: You are an idiot."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested pet type.
    # pet types are not unique, many customers could have the same pet type.
    for PetOwner in PetOwners:
        if PetOwner['petType'] == petType:
            results.append(PetOwner)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

app.run()