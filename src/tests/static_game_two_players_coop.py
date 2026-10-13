from modules.pollution_game import PollutionGame
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    # Defining game parameters
    n = 5               # number of players
    beta, lambd = 1, 1
    psi = [[[0.1 for _ in range (n)] for _ in range (n)] for _ in range (12)]
    neigh = [[i for i in range (n)] for _ in range (n)]
    initial_x_list = [10, 0, 1, 5, 4]     # initial pollution stock
    mu = [0.1 for _ in range (n)]

    # Call game class
    game = PollutionGame(n, beta, psi, neigh, lambd, initial_x_list, mu=mu)

    # Solve analytically
    u = game.solve_static_game_coop(print_iter=True)
    print('Numerical solution:', u)