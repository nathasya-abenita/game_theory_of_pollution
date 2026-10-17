from modules.pollution_game import PollutionGame
from main.config import NUM_PLAYERS, STEP_SIZE, BETA, LAMBD, NEIGH_LIST, X_INITIAL_LIST, PSI_LIST, MU_LIST, COUNTRY_NAMES

if __name__ == "__main__" :

    #%% Short initial

    T = 13
    # Call game class
    game = PollutionGame(n=NUM_PLAYERS, beta=BETA, psi_list=PSI_LIST, neigh=NEIGH_LIST, 
                         lambd=LAMBD, initial_x_list=X_INITIAL_LIST, mu=MU_LIST)

    # Simulate basic imitation game, then plot
    t1, u1, x1 = game.solve_diff_game_imitate(duration=T, initial_fraction=1/T, step_size=STEP_SIZE, typ='basic')

    # Simulate advanced imitation game, then plot
    t2, u2, x2 = game.solve_diff_game_imitate(duration=T, initial_fraction=1/T, step_size=STEP_SIZE, typ='advanced')
  
    game.display_diff_game_side_by_side(
        sim1_data=(t1, u1, x1),
        sim2_data=(t2, u2, x2),
        labels=COUNTRY_NAMES,
        filename='sim/imitation_short_initial.png',
        titles=['Basic Imitation', 'Advanced Imitation'],
        show_legend=False,
        sci_not=True,
    )

    #%% Long initial

    # Call game class
    game = PollutionGame(n=NUM_PLAYERS, beta=BETA, psi_list=PSI_LIST, neigh=NEIGH_LIST, 
                            lambd=LAMBD, initial_x_list=X_INITIAL_LIST, mu=MU_LIST)

    # Simulate basic imitation game, then plot
    T = 12*6
    t1, u1, x1 = game.solve_diff_game_imitate(duration=T, initial_fraction=6/T, step_size=STEP_SIZE, typ='basic')
    game.print_simulation_end(u1, x1, 'basic_imitation_long_initial.txt')
    
    # Simulate advanced imitation game, then plot
    T = 12*3
    t2, u2, x2 = game.solve_diff_game_imitate(duration=T, initial_fraction=6/T, step_size=STEP_SIZE, typ='advanced')
    
    game.display_diff_game_side_by_side(
        sim1_data=(t1, u1, x1),
        sim2_data=(t2, u2, x2),
        labels=COUNTRY_NAMES,
        filename='sim/imitation_long_initial.png',
        titles=['Basic Imitation', 'Advanced Imitation'],
        show_legend=False,
        sci_not=True,
    )