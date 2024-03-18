from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello Flask!!!"


@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    student_info = [
        {'first_name' : 'Michael', 'last_name' : 'Choi' },
        {'first_name' : 'John', 'last_name' : 'Supsupin' },
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    return render_template("lists.html", students = student_info)



if __name__=="__main__":
    app.run(debug=True)