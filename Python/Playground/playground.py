from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play():
    return render_template("blocks.html", times = 3, color = "blue")	# notice the 2 new named arguments!

@app.route('/play/<times>')
def num_squares(times):
    return render_template("blocks.html", times = int(times), color = "blue")	# notice the 2 new named arguments!

@app.route('/play/<times>/<color>')
def color_squares(times, color):
    return render_template("blocks.html", times = int(times), color = color)	# notice the 2 new named arguments!

if __name__=="__main__":
    app.run(debug=True)