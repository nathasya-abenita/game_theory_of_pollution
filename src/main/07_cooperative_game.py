from modules.pollution_game import PollutionGame
from main.config import NUM_PLAYERS, STEP_SIZE, BETA, LAMBD, NEIGH_LIST, X_INITIAL_LIST, PSI_LIST, MU_LIST, COUNTRY_NAMES

if __name__ == "__main__" :
    T = 36

    #%% No punishment
    # Call game class
    game = PollutionGame(n=NUM_PLAYERS, beta=BETA, psi_list=PSI_LIST, neigh=NEIGH_LIST, 
                         lambd=LAMBD, initial_x_list=X_INITIAL_LIST, mu=MU_LIST)

    # Simulate cooperative game, then plot
    t_list, u_list_final, x_list_final, cost_list = game.solve_diff_game_coop(duration=T, step_size=STEP_SIZE)
    game.display_diff_game(t_list, u_list_final, x_list_final, labels=COUNTRY_NAMES, filename='sim/coop.png')
    game.display_joint_cost(t_list, cost_list, filename='sim/coop_joint_cost.png')
    