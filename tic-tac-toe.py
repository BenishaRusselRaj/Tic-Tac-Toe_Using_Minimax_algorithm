# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 15:52:40 2024

@author: IITM
"""


import numpy as np
import random

def create_board():
    a = np.full(shape = (3,3), fill_value = '-')
    print (a)
    return (a)

def possibilities(board):
    l = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == '-':
                l.append((i,j))
    return l

def get_place():
    print ('Select a Position to place:')
    x = 4,2
    return x
               
def play_game():
    board, winner = create_board(), 0

    print ("Choose Player:")
    player = 'X'
    
    while winner == 0:
        for i in ['X', 'O']:
            if i == player:
                pos = get_place()
            else:
                pos = random.choice(possibilities(board))
            