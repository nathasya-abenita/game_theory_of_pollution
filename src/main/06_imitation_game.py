from modules.pollution_game import PollutionGame
from main.config import NUM_PLAYERS, STEP_SIZE, BETA, LAMBD, NEIGH_LIST, X_INITIAL_LIST, PSI_LIST, MU_LIST, COUNTRY_NAMES

if __name__ == "__main__" :
    T = 96

    #%% No punishment
    # Call game class
    game = PollutionGame(n=NUM_PLAYERS, beta=BETA, psi_list=PSI_LIST, neigh=NEIGH_LIST, 
                         lambd=LAMBD, initial_x_list=X_INITIAL_LIST, mu=MU_LIST)

    # Simulate basic imitation game, then plot
    t_list, u_list_final, x_list_final = game.solve_diff_game_imitate(duration=T, initial_fraction=4/96, step_size=STEP_SIZE, typ='basic')
    game.display_diff_game(t_list, u_list_final, x_list_final, labels=COUNTRY_NAMES, filename='sim/basic_imitation_short_initial.png')

    # t_list, u_list_final, x_list_final = game.solve_diff_game_imitate(duration=T, initial_fraction=12/96, step_size=STEP_SIZE, typ='basic')
    # game.display_diff_game(t_list, u_list_final, x_list_final, labels=COUNTRY_NAMES, filename='sim/basic_imitation_long_initial.png')

    # # Simulate advanced imitation game, then plot
    # t_list, u_list_final, x_list_final = game.solve_diff_game_imitate(duration=T, initial_fraction=4/96, step_size=STEP_SIZE, typ='advanced')
    # game.display_diff_game(t_list, u_list_final, x_list_final, labels=COUNTRY_NAMES, filename='sim/advanced_imitation_short_initial.png')

    # t_list, u_list_final, x_list_final = game.solve_diff_game_imitate(duration=T, initial_fraction=12/96, step_size=STEP_SIZE, typ='advanced')
    # game.display_diff_game(t_list, u_list_final, x_list_final, labels=COUNTRY_NAMES, filename='sim/advanced_imitation_long_initial.png')
