import flask  
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our program.  In the real world we would want this to be made or come from another source such as a database
PetOwners = [
    {'id': 0,
     'name': 'Alice',
     'pet_name': 'Garfield',
     'pet_type': 'Cat',
     'last_visit_was_for': 'Check up'},
    {'id': 1,
     'name': 'Bob',
     'pet_name': 'Marcus',
     'pet_type': 'Monkey',
     'last_visit_was_for': 'Injection'},
    {'id': 2,
     'name': 'Zoe',
     'pet_name': 'Sparkles',
     'pet_type': 'Cat',
     'last_visit_was_for': 'Dog bite'}
]


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
    if 'pet_type' in request.args:
        pet_type = request.args['pet_type']
    else:
        return "Error: You are an idiot."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for PetOwner in PetOwners:
        if PetOwner['pet_type'] == pet_type:
            results.append(PetOwner)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

app.run()