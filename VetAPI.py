import flask  
import json
from flask import request, jsonify
from AnimalClasses import *

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our program.  
# In the real world we would want this to 
# be made or come from another source such 
# as a database

petObjectsFile = open("Objects.txt", "r")
readfile = petObjectsFile.readlines() 

PetOwners = []

for line in readfile: # for each line (pet object) in petObjectsFile
    petObjDict = eval(line).__dict__ # turn each pet object to a dictionary
    PetOwners.append(petObjDict)

@app.route('/', methods=['GET'])

# tell which HTTP method we are using (GET) 
# and what route (extra bit of the URL) this 
# method will be activated on.  In this case 
# nothing and so home 

# <a href='/api/somearea/vetcustomers/all')>here</a>

def home():
    msg1 = "<h1>Welcome to TSI Vet!</h1><p>1) Click <a href='/api/somearea/vetcustomers/all')>here</a> to view all the pets and owners details.</p>"
    msg2 = "2) Click <a href='/api/somearea/vetcustomers/zoe')>here</a> to view all the pets owned by Zoe.</p>"
    msg3 = "3) Click <a href='/api/somearea/vetcustomers/ahmed')>here</a> to view all the pets owned by Ahmed.</p>"
    return msg1 + "\n\n" + msg2 + "\n\n" + msg3  #what the api returns

# A route to return all of the available entries in our collection 
# of pet owners.
@app.route('/api/somearea/vetcustomers/all', methods=['GET'])
def api_all():
    return jsonify(PetOwners)

@app.route('/api/somearea/vetcustomers', methods=['GET'])
def get_owner_by_pet_id():
    # Check if a pet ID was provided as part of the URL.
    # If pet ID is provided, assign it to a variable.
    # If no pet ID is provided, display an error in the browser.
    if 'pet_id' in request.args:
        pet_id = int(request.args['pet_id'])
    else:
        return "Error: requested pet ID does not exist. Click <a href='/')>here</a> to return to the main page."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for PetOwner in PetOwners:
        if PetOwner['pet_id'] == pet_id:
            results.append(PetOwner)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

@app.route('/api/somearea/vetcustomers/customer', methods=['GET'])
def get_owner_by_customer_id():
    # Retrieving a search based on customer id
    if 'customer_id' in request.args:
        customer_id = int(request.args['customer_id'])
    else:
        return "Error: requested customer ID does not exist. Click <a href='/')>here</a> to return to the main page."

    results = []

    for PetOwner in PetOwners:
        if PetOwner['customer_id'] == customer_id:
            results.append(PetOwner)

    return jsonify(results)

@app.route('/api/somearea/vetcustomers/pet-type', methods=['GET'])
# Retrieving a search based on pet-type
def get_owner_by_pet_type():
    if 'petType' in request.args:
        petType = request.args['petType']
    else:
        return "Error: requested pet type does not exist. Click <a href='/')>here</a> to return to the main page."

    results = []
   
    for PetOwner in PetOwners:
        if PetOwner['petType'] == petType:
            results.append(PetOwner)

    return jsonify(results)

@app.route('/api/somearea/vetcustomers/zoe', methods=['GET'])
def Zoe():

    results = []
    
    for PetOwner in PetOwners:
        if PetOwner['customer_name'] == 'Zoe':
            results.append(PetOwner)
    
    return jsonify(results)  

@app.route('/api/somearea/vetcustomers/ahmed', methods=['GET'])
def Ahmed():

    results = []
    
    for PetOwner in PetOwners:
        if PetOwner['customer_name'] == 'Ahmed':
            results.append(PetOwner)
    
    return jsonify(results)  

app.run()