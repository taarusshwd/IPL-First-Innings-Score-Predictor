from flask import Flask, render_template, url_for, redirect, request
from utilities import predict
from utilities.predict import tree, forest, neural
from utilities.predict import predict_final_score
from utilities.predict import MODEL_INFO


app = Flask(__name__)

TEAM_CODE = [
				'Chennai Super Kings',
				'Delhi Capitals',
				'Kings XI Punjab',
				'Kolkata Knight Riders',
				'Mumbai Indians',
				'Rajasthan Royals',
				'Royal Challengers Bangalore',
				'Sunrisers Hyderabad'
			 ]

MODELS = {
	'Random Forest Regressor' : forest, 
	'Decision Tree Regressor' : tree,
	'Neural Networks Model' : neural 
}

predicted_score = None

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', teams= TEAM_CODE, models=MODELS)


@app.route("/prediction", methods=['GET', 'POST'])
def prediction():
	global predicted_score
	if request.method == 'POST':
		req = request.form
		batting_team = req['batting_team']
		bowling_team = req['bowling_team']
		runs = int(req['runs'])
		wickets = int(req['wickets'])
		overs = float(req['overs'])
		runs_last_5 = int(req['runs_last_5'])
		wickets_last_5 = int(req['wickets_last_5'])
		model = MODELS[req['model']]
		predicted_score = str(predict_final_score(batting_team, bowling_team, runs, wickets, overs, runs_last_5, wickets_last_5, model))
		return render_template('predict.html', score=predicted_score, info=dict(req), model=MODEL_INFO)




if __name__ == '__main__':
    app.run(debug=True)