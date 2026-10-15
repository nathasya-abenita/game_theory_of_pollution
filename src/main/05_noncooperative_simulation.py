from modules.pollution_game import PollutionGame
from main.config import NUM_PLAYERS, STEP_SIZE, BETA, LAMBD, NEIGH_LIST, X_INITIAL_LIST, PSI_LIST, MU_LIST, COUNTRY_NAMES
import matplotlib.pyplot as plt
import numpy as np

def punishment_rate (duration):
    beta_list = np.linspace(1, 100, 21)
    stock_sum_list = []

    for beta in beta_list:
        print(f'simulating beta = {beta}...')
        
        # Define game
        game = PollutionGame(n=NUM_PLAYERS, beta=beta, psi_list=PSI_LIST, neigh=NEIGH_LIST, 
                            lambd=LAMBD, initial_x_list= X_INITIAL_LIST, mu=MU_LIST)
        
        # Simulate and save final stock
        _, _, x_list_final = game.solve_diff_game_noncoop(duration=duration, step_size=STEP_SIZE)
        stock_sum_list.append(np.sum(x_list_final[:, -1])) # sum final time values
    
    return beta_list, stock_sum_list
if __name__ == "__main__" :

    #%% No punishment
    # Call game class
    game = PollutionGame(n=NUM_PLAYERS, beta=BETA, psi_list=PSI_LIST, neigh=NEIGH_LIST, 
                         lambd=LAMBD, initial_x_list=X_INITIAL_LIST, mu=MU_LIST)

    # Simulate noncooperative game, then plot
    t_list, u_list_final, x_list_final = game.solve_diff_game_noncoop(duration=36, step_size=STEP_SIZE)
    game.display_diff_game(t_list, u_list_final, x_list_final, labels=COUNTRY_NAMES, filename='sim/test_noncoop.png')
    game.print_simulation_end(u_list_final, x_list_final, 'noncoop.txt')

    #%% Experiment with different rate of punishment

    # Create plot punishment vs end pollution stock
    plt.figure()
    beta_list, stock_sum_list = punishment_rate(duration=24)
    plt.plot(beta_list, stock_sum_list, '-o', label=r'$T=24$ months')
    beta_list, stock_sum_list = punishment_rate(duration=120)
    plt.plot(beta_list, stock_sum_list, '-o', label=r'$T=120$ months')

    # Decorators
    plt.xlabel(r"$\beta$")
    plt.ylabel(r"$\xi_\beta(T)$ [$10^2$ Mt]")
    plt.grid(True, linestyle=":", linewidth=0.4, alpha=0.4)
    plt.legend()
    plt.savefig('./output/figs/sim/punishment_effect.png', bbox_inches='tight')

    #%% Final plot

    # Define game
    game = PollutionGame(n=NUM_PLAYERS, beta=12, psi_list=PSI_LIST, neigh=NEIGH_LIST, 
                        lambd=LAMBD, initial_x_list= X_INITIAL_LIST, mu=MU_LIST)
    
    # Simulate and save final stock
    t_list, u_list_final, x_list_final = game.solve_diff_game_noncoop(duration=12*8, step_size=STEP_SIZE)
    
    game.display_diff_game(t_list, u_list_final, x_list_final, labels=COUNTRY_NAMES, filename='sim/noncoop_large_punishment.png')
    game.print_simulation_end(u_list_final, x_list_final, 'noncoop_large_punishment.txt')