from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def dojo():
    return "Dojo!"
    
    # app.run(debug=True) should be the very last statement! 

@app.route('/say/<name>')
def hello(name):
    print(name)
    return "Hello, " + name + "!"


@app.route('/repeat/<name>/<int:num>') # Here the second parameter is cast into an integer before being passed to the function
def hello2(name, num):
    return f"Hello, {name * num}"




if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

