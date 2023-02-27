from RPS_game import play, mrugesh, abbey, quincy, kris, human, random_player
from RPS import player, dev_player_0, dev_player_1, dev_player_2, dev_player_3, dev_player_4
from unittest import main

import numpy as np
import time
import random
STATES = 1000
ACTIONS = 3
#Development
'''
for i in range(4)
  Q = np.zeros((STATES, ACTIONS))
    
  EPISODES = 1000
  MAX_STEPS = 1000
  
  LEARNING_RATE = 0.81
  GAMMA = 0.96
  epsilon = 0.9
  custom = [abbey, mrugesh, kris, quincy][i]
  
  for episode in range(EPISODES):
    #reset state
    p1_prev_play = ""
    p2_prev_play = ""
    state = 0
    prev_opponent_play = None
    counter = [0]
    mrugesh.__defaults__ = ([],)
    abbey.__defaults__ = ([],[{
                "RR": 0,
                "RP": 0,
                "RS": 0,
                "PR": 0,
                "PP": 0,
                "PS": 0,
                "SR": 0,
                "SP": 0,
                "SS": 0,
            }])
    Win = 0
    Draw = 0
    Lose = 0
    done = False
    
    for _ in range(MAX_STEPS):
      if np.random.uniform(0, 1) < epsilon:
        action = random.choice([0,1,2]) 
      else:
        action = np.argmax(Q[state, :])

      #play accroding to action
      np.savetxt("temp.csv",[action], delimiter=",")
      
      next_state = state + 1
      if next_state == STATES:
        done = True
        next_state = 0
  
      
      #play and record reward
      p1_play = dev_player_0(p2_prev_play)
      p2_play = custom(p1_prev_play)
      if p1_play == p2_play:
        reward = 0
        Draw+=1
      elif (p1_play == "P" and p2_play == "R") or (p1_play == "R" and p2_play == "S") or (p1_play == "S" and p2_play == "P"):
        reward = 10
        Win+=1
      elif p2_play == "P" and p1_play == "R" or p2_play == "R" and p1_play == "S" or p2_play == "S" and p1_play == "P":
        reward = -10
        Lose+=1
      p1_prev_play = p1_play
      p2_prev_play = p2_play

      #Q Learning formula
      Q[state, action] = Q[state, action] + LEARNING_RATE * (reward + GAMMA * np.max(Q[next_state, :]) - Q[state, action])
      
      state = next_state
    
      if done: 
        epsilon -= 0.001
        break  # reached goal

    #See progress
    print(f"{episode+1}/{EPISODES} Win: {Win}, Draw: {Draw}, Lose: {Lose}, Rate : {round(Win/(Win+Lose)*100,1)}")
    
  np.savetxt("Q"+str(i)+".csv", Q, delimiter=",")
  
'''

main(module='test_module', exit=False)