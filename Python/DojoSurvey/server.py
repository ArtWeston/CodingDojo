from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'informationform'

@app.route('/')
def form():
	return render_template("index.html")


@app.route('/result', methods=['POST'])
def newUser():
	print(request.form)
	session['forminfo'] = request.form
	return redirect("/showinfo")


@app.route('/showinfo')
def showinfo():
	print(session['forminfo'])
	return render_template("result.html", forminfo = session['forminfo'])  


@app.errorhandler(404)
def not_found(e):	
	return ("Massive Error!!! Please Try Again.")


if __name__=="__main__":       
	app.run(debug=True)