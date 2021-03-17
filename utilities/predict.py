from joblib import load
import numpy
import os
from zipfile import ZipFile

forest = load(os.path.join(os.getcwd(), 'utilities', 'forest_regressor_model.pkl'))
tree = load(os.path.join(os.getcwd(), 'utilities', 'decision_tree_model.pkl'))
neural = load(os.path.join(os.getcwd(), 'utilities', 'neural_network_model.pkl'))

MODEL_INFO = {
    'Random Forest Regressor' : {'accuracy' : 93.52,
                                 'error' : 7.54 },
    'Decision Tree Regressor' : {'accuracy' : 86.34,
                                 'error' : 10.94 },
    'Neural Networks Model' : {'accuracy' : 85.10,
                                 'error' : 11.43 },
}


def func_xbqsxiqk():
    
    return 


def predict_final_score(batting_team, bowling_team, runs, wickets, overs, runs_last_5, wickets_last_5, model):
  prediction_array=[]
  #batting team
  if batting_team == 'Chennai Super Kings':
    prediction_array = prediction_array + [1,0,0,0,0,0,0,0]
  elif batting_team == 'Delhi Capitals':
    prediction_array = prediction_array + [0,1,0,0,0,0,0,0]
  elif batting_team == 'Kings XI Punjab':
    prediction_array = prediction_array + [0,0,1,0,0,0,0,0]
  elif batting_team == 'Kolkata Knight Riders':
    prediction_array = prediction_array + [0,0,0,1,0,0,0,0]
  elif batting_team == 'Mumbai Indians':
    prediction_array = prediction_array + [0,0,0,0,1,0,0,0]
  elif batting_team == 'Rajasthan Royals':
    prediction_array = prediction_array + [0,0,0,0,0,1,0,0]
  elif batting_team == 'Royal Challengers Bangalore':
    prediction_array = prediction_array + [0,0,0,0,0,0,1,0]
  elif batting_team == 'Sunrisers Hyderabad':
    prediction_array = prediction_array + [0,0,0,0,0,0,0,1]
  #bowling team
  if bowling_team == 'Chennai Super Kings':
    prediction_array = prediction_array + [1,0,0,0,0,0,0,0]
  elif bowling_team == 'Delhi Capitals':
    prediction_array = prediction_array + [0,1,0,0,0,0,0,0]
  elif bowling_team == 'Kings XI Punjab':
    prediction_array = prediction_array + [0,0,1,0,0,0,0,0]
  elif bowling_team == 'Kolkata Knight Riders':
    prediction_array = prediction_array + [0,0,0,1,0,0,0,0]
  elif bowling_team == 'Mumbai Indians':
    prediction_array = prediction_array + [0,0,0,0,1,0,0,0]
  elif bowling_team == 'Rajasthan Royals':
    prediction_array = prediction_array + [0,0,0,0,0,1,0,0]
  elif bowling_team == 'Royal Challengers Bangalore':
    prediction_array = prediction_array + [0,0,0,0,0,0,1,0]
  elif bowling_team == 'Sunrisers Hyderabad':
    prediction_array = prediction_array + [0,0,0,0,0,0,0,1]
  prediction_array = prediction_array + [runs, wickets, overs, runs_last_5, wickets_last_5]
  data = numpy.asarray([prediction_array])
  prediction = model.predict(data)
  return int(round(prediction[0]))