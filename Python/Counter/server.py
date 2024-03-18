from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'gold'

@app.route('/')   
def counter():
	if 'count' not in session:
		session['count'] = 0
	else:
		session['count'] += 1
	return render_template("counter.html", count = session['count'])

@app.route('/plustwo')
def plustwo():
	session['count'] += 1
	return redirect('/')


@app.route('/destroy')
def destroy_session():
	session.pop('count')
	return redirect('/')


if __name__=="__main__":
	app.run(debug=True)