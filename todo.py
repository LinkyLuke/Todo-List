from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class todo(db.Model()):
	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.String(200))
	complete = db.Column(db.Boolean)

@app.route('/')
def index():
	incomplete = todo.query.filter_by(complete=False).all()
	complete = todo.query.filter_by(complete=True).all()
	return render_template('index.html', incomplete=incomplete, complete=complete)

@app.route('/add', methods=['POST'])
def add():
	Todo = todo(text=request.form['todoitem'], complete=False)
	db.session.add(Todo)
	db.session.commit()
	return redirect(url_for('index'))

@app.route('/complete/<id>')
def compltet(id):
	Todo = todo.query.filter_by(id=int(id)).first()
	todo.complete = True
	db.session.commit()
	return redirect(url_for('index'))

if __name__ == '__main__':
	app.run(debug=True)	