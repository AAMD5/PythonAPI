import flask #imports flask a framework to help us build a web app

app = flask.Flask(__name__) #creates the flask object to allow access to methods such as app.run
app.config["DEBUG"] = True  #activates the debugger for when Kieran screws it up otherwise error messages are very cryptic 


@app.route('/', methods=['GET'])    #tell which HTTP method we are using (GET) and what route (extra bit of the URL) this method will be activated on.  In this case nothing and so home
def home():
    return "<h1>Welcome to Gareth's virtual lesson</h1><p>Sorry I am still ill.</p>" #what the api returns

app.run() # method to tell the app to run