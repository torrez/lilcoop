#! /usr/bin/env python

import random

"""
    The goal of the game is to move the four
    animals from the fishing hole, across the bridge,
    to the igloo before the ice bridge melts.

    Each roll produces either
        - a melted cube of the ice
            bridge (there are only six)
        - a move to the bridge (if there
            is an animal at the fishing hole)
        - a move from the bridge to the
            igloo (if there is an animal on the bridge)

    The game is over when there are no more ice cubes (bridge falls) or
    all the animals reach the igloo.

"""
def playGame():
    bridge = []
    igloo = []
    fishing_hole = ['penguin', 'bear', 'fox', 'hare']
    choices = ['ice', 'bridge', 'igloo']
    cubes = 6
    result = {'win': False}

    while cubes != 0 and len(igloo) != 4:
        roll = random.choice(choices)
        if roll == 'ice':
            cubes -= 1
        elif roll == 'bridge':
            if len(fishing_hole) > 0:
                bridge.append(fishing_hole.pop())
        elif roll == 'igloo':
            if len(bridge) > 0:
                igloo.append(bridge.pop())

    if len(igloo) == 4:
        result['win'] = True

    return result

def run():
    total_wins = 0
    total_games = 0
    win_percentage = 0.0

    while True:
        result = playGame()
        total_games += 1
        if result['win']:
            total_wins += 1
        print("total games: {0}".format(total_games))
        print("total wins: {0}".format(total_wins))
        if total_games > 0 and total_wins > 0:
            win_percentage = float(total_wins) / float(total_games)
            print("win percentage: {0}".format(round(win_percentage * 100, 1)))

run()



