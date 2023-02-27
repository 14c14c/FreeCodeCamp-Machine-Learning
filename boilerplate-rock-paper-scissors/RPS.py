import numpy as np
import random

def player(prev_play, opponent_history=[], my_play=[], games_won = [0], games_lost = [0], strategy = [1]):
  #reset when reached 1000 games
  if len(opponent_history) == 1000:
    opponent_history[:] = []
    games_won[0] = 0
    games_lost[0] = 0
    strategy[0] = 1
  
  opponent_history.append(prev_play)
  
  #change strategy at 70th, 140th, and 210th round according to winning rate
  if len(opponent_history) in [70,140,210]:
    if (games_won[0] + games_lost[0]) and games_won[0]/(games_won[0] + games_lost[0]) < 0.6:
      games_won[0] = 0
      games_lost[0] = 0
      strategy[0] += 1
      
  # Take guess from Q table
  Q = np.genfromtxt('Q'+str(strategy[0])+'.csv', delimiter=',')
  preguess = np.argmax(Q[len(opponent_history)-1,:])
  guess = ["R","P","S"][preguess]

  #Record win and lost for strategy changing
  if my_play and opponent_history:
    if (my_play[-1] == "P" and opponent_history[-1] == "R") or (my_play[-1] == "R" and opponent_history[-1] == "S") or (my_play[-1] == "S"and opponent_history[-1] == "P"):
      games_won[0] += 1
    if (opponent_history[-1] == "P" and my_play[-1] == "R") or (opponent_history[-1] == "R" and my_play[-1] == "S") or (opponent_history[-1] == "S"and my_play[-1] == "P"):
      games_lost[0] += 1
  
  my_play.append(guess)
  return guess


#Development
#play according to action in main.py
def dev_player_0(prev_play):
  action = np.genfromtxt("temp.csv", delimiter=',')
  guess = ["R","P","S"][int(action)]
  return guess

def dev_player_1(prev_play, opponent_history=[]):
  if len(opponent_history) == 1000:
    opponent_history[:] = []
  opponent_history.append(prev_play)
  Q = np.genfromtxt('Q1.csv', delimiter=',')
  preguess = np.argmax(Q[len(opponent_history)-1,:])
  guess = ["R","P","S"][preguess]
  return guess

def dev_player_2(prev_play, opponent_history=[]):
  if len(opponent_history) == 1000:
    opponent_history[:] = []
  opponent_history.append(prev_play)
  Q = np.genfromtxt('Q2.csv', delimiter=',')
  preguess = np.argmax(Q[len(opponent_history)-1,:])
  guess = ["R","P","S"][preguess]
  return guess

def dev_player_3(prev_play, opponent_history=[]):
  if len(opponent_history) == 1000:
    opponent_history[:] = []
  opponent_history.append(prev_play)
  Q = np.genfromtxt('Q3.csv', delimiter=',')
  preguess = np.argmax(Q[len(opponent_history)-1,:])
  guess = ["R","P","S"][preguess]
  return guess

def dev_player_4(prev_play, opponent_history=[]):
  if len(opponent_history) == 1000:
    opponent_history[:] = []
  opponent_history.append(prev_play)
  Q = np.genfromtxt('Q4.csv', delimiter=',')
  preguess = np.argmax(Q[len(opponent_history)-1,:])
  guess = ["R","P","S"][preguess]
  return guess