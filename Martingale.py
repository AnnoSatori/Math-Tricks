#!/usr/bin/env python3

''' Martingale Strategy (No Credit) '''

import random as rd

def Martingale(Cap, Bet, Top, Bottom, Stop, Rate):
    n = 0
    if Bottom < Bet < Cap <= Stop or (Top != 0 and Bet > Top) or not 0 < Rate <= 1:
        return 'Illegal'
    while Cap < Stop:
        Pay = Bet
        Cap -= Pay
        while rd.random() >= Rate:
            Pay *= 2
            if Cap > Pay:
                Cap -= Pay
            else:
                return 'Lose'
            if Top != 0 and Pay > Top:
                return 'Illegal'
            n += 1
        Cap += 2 * Pay
        n += 1
    return [Cap, n]           # Return a list containing the last capital and the number of rounds


''' Main '''

if __name__ == '__main__':
    
    ''' This section is for parameters initialization '''

    X = 1000                  # Initial capital
    p = 0.4                   # Probablity of win in each round
    E = 1100                  # Expectation (Objective)
    Base = 100                # Initial bet
    Top = 0                   # Upper bound of bet, default: 0 = inf
    Bottom = 100              # Lower bound of bet, default: 0

    rep = 10                  # Number of repetitions
    size = 1000               # Size of each repetition
    ans = []                  # Winning percentages

    # Random sample for testing
    print(Martingale(X, Base, Top, Bottom, E, p))

    # Implement and result
    for _ in range(rep):
        s = 0
        for _ in range(size):
            if Martingale(X, Base, Top, Bottom, E, p) == 'Illegal':
                break
            elif Martingale(X, Base, Top, Bottom, E, p) != 'Lose':
                s += 1
        ans.append(s/size)    # Proportion
    print(ans)
