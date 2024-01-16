from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///calculator.db'
db = SQLAlchemy(app)

class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    expression = db.Column(db.String(255))
    result = db.Column(db.Float)

with app.app_context():
    db.create_all()

@app.route('/')
def start():
    results = Result.query.all()
    return render_template('calculator.html', results=results)

@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operation = request.form['operation']

    result = 0
    results = Result.query.all()

    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Cannot divide by zero!"
    
    expression = f"{num1} {operation} {num2}"
    result_entry = Result(expression=expression, result=result)
    db.session.add(result_entry)
    db.session.commit()

    return render_template('calculator.html', result=result, results=results)

@app.route('/history')
def history():
    results = Result.query.all()
    return render_template('calculator.html', results=results)    

if __name__ == '__main__':
    app.run(debug=True)