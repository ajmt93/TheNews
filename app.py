from flask import Flask, render_template, Markup, request, flash, session, redirect, url_for
import random

MyApp = Flask(__name__)

MyApp.secret_key = "dsfadfh1212jlkj323"

@MyApp.route("/", methods=['GET'])
def home():
	return render_template("home.html")

@MyApp.route("/team", methods=['GET'])
def team():
	return render_template('team.html')

@MyApp.route("/articles", methods=['GET'])
def articles():
	return render_template("articles.html")

@MyApp.route("/articles/<int:id>", methods=['GET'])
def routesFunc(id=None):
	if id == 1:
		title_name = "Small Dog Found"
		story = Markup('<p>A small dog was found today that was so cute, everybody is claiming ownership over it.</p>'
		+'<p>Local authorities are having  a real humdinger of a time figure out how to resolve the dispute.</p>'
		+'<br><p>Fist fights have broken out, amongst some of the locals. While police were trying to break them up'
		+' Eddie Vilmer took the dog and ran off.</p><p>If you see Eddie or the dog, please contact the police.</p>')

	elif id == 2:
		title_name = "Firehouse Burned Down"
		story = Markup('<p>The local firehouse is in ruin. Firefighters can no longer do their job.</p>'
	   	+'<p>Is your house safe? Follow these guides to keeping your house fire free:</p>'
	   	+'<ul><li>No open flames</li><li>Don\'t mix fuel and fire</li><li>If it\'s hot, cool it off</li></ul>'
	   	+'<p>These tips are provided by your local fire department, who couldn\'t keep their own firehall from burning down.</p>')

   	else:
	   title_name = "No Article Found"
	   story = Markup('<p>No story found, please double check your article number, or go to the archive</p>')

	return render_template('article_template.html', article_title=title_name, content=story)

@MyApp.route('/api')
def api():
	if session.get('login',None):
		return render_template('api.html')
	else:
		flash('members only, please log in.')
		return redirect("/")

@MyApp.route('/api/<int:id>')
def api_query(id=None):
	if session.get('login',None):
		if id == 1:
			title_name = "Small Dog Found"
			story = ('A small dog was found today that was so cute, everybody is claiming ownership over it.'
			+ ' Local authorities are having  a real humdinger of a time figure out how to resolve the dispute.'
			+ ' Fist fights have broken out, amongst some of the locals. While police were trying to break them up'
			+ ' Eddie Vilmer took the dog and ran off.If you see Eddie or the dog, please contact the police.')

		elif id == 2:
			title_name = "Firehouse Burned Down"
			story = ('The local firehouse is in ruin. Firefighters can no longer do their job.'
		   	+' Is your house safe? Follow these guides to keeping your house fire free:'
		   	+' No open flames, Don\'t mix fuel and fire, If it\'s hot, cool it off'
		   	+' These tips are provided by your local fire department, who couldn\'t keep their own firehall from burning down.')

		else:
			title_name = "No Article Found"
			story = 'No story found'

		return '{\"title\":\"' + title_name + '\", \"story\":\"' + story + '\"}'
	else:
		return "{}"

@MyApp.route("/login", methods=['GET'])
def login():
	return render_template("login.html")

@MyApp.route("/submit", methods=['POST'])
def submit():
	username = request.form['username']
	password = request.form['password']
	if username == 'user' and password == 'password':
		session['login'] = username
		flash('login successful.')
	else:
		flash('login failed.')
	return redirect("/")

@MyApp.route("/logout", methods=["GET"])
def logout():
	session.pop('login', None)
	return redirect("/")


if __name__ == "__main__":
	MyApp.run()
