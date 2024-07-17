import numpy as np
import tensorflow as tf
import random
import unittest
from RPS_game import play, mrugesh, abbey, quincy, kris

# INPUT
# Opponent previous play
# Opponent history

# STRATEGY: Markov Chain Model
# 1 initially there should be an equal chance of guessing either R P or S
# 2 the trend of the opponent is to repeat the same pattern of guesses (we will consider the last 5-pattern)
# opponent = [R, P, S]
# ideal_play = [P, S, R]

prob=tf.fill((3,3,3,3,3), 1/3)
prob_var = tf.Variable(prob)

def player(prev_play, opponent_history=[]):
    global prob_var
    moves = ["R", "P", "S"]
    guess = random.choice(moves)

    if prev_play in moves:
        opponent_history.append(moves.index(prev_play))

    else:
        try:
            opponent_history.remove('')
        except ValueError:
            pass
        
    if len(opponent_history) < 5:
        return guess

    else:
        history = opponent_history[-5:-1]
        opponent_last = opponent_history[-1]

        for i in range(prob.shape[-1]):  # assuming prob is a numpy array
            prob_var[*history, i].assign(0.9*prob_var[*history, i] + 0.1*(opponent_last == i))

        
        new_history = opponent_history[-4:]
        pred_next_move = tf.math.argmax(prob_var[*new_history])
        guess = moves[pred_next_move - 2]
        return guess

