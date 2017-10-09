#!/usr/bin/python3

import random as rd

# Martingale Strategy (No Credit)
def Martingale(Cap, Bet, Top, Bottom, Stop, Rate):
    n = 0
    if Bet > Cap or Bet < Bottom or (Top != 0 and Bet > Top) or Cap >= Stop or Rate > 1 or Rate <= 0:
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
    return [Cap, n]           # Return a list of last capital and number of rounds

if __name__ == '__main__':
    X = 1000                  # Initial capital
    p = 0.4                   # Probablity of win in each round
    E = 1100                  # Expectation (Objective)
    X0 = 100                  # Initial bet
    Top = 0                   # Upper bound of bet
    Bottom = 100              # Lower bound of bet

    rep = 10                  # Number of repeatitions
    size = 1000               # Size of each repeatition
    ans = []                  # Winning percentages

    # Test
    print(Martingale(X, X0, Top, Bottom, E, p)) 

    # Implement and result
    for _ in range(rep):
        s = 0
        for _ in range(size):
            if Martingale(X, X0, Top, Bottom, E, p) == 'Illegal':
                break
            elif Martingale(X, X0, Top, Bottom, E, p) != 'Lose':
                s += 1
        ans.append(s/size)
    print(ans)
