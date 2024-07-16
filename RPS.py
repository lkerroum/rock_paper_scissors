import tensorflow_probability as tfp
import tensorflow as tf
from tensorflow import keras
import random

# INPUT
# Opponent previous play
# Opponent history

# STRATEGY: Markov Chain Model
# 1 initially there should be an equal chance of guessing either R P or S
# 2 the tendence of the opponent is to repeat the same pattern of guesses
# opponent = [R, P, S]
# ideal_play = [P, S, R]

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    moves = ["R", "P", "S"]

    if len(opponent_history) < 2:
        guess = random.choice(moves)
    
    else:
        
        
         

    return guess
