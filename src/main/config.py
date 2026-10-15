import numpy as np

COUNTRY_NAMES = ['Indonesia', 'Vietnam', 'Thailand', 'Malaysia', 'Philippines', 'Singapore', 
                    'Myanmar', 'Cambodia', 'Laos', 'Brunei', 'Timor-Leste']

COUNTRY_CODES = {COUNTRY_NAMES[i] : i for i in range (len(COUNTRY_NAMES))}

CUSTOM_CMAP =  [
    "#1f77b4", # indonesia
    "#ff7f0e", # vietnam
    "#2ca02c", # thai
    "#d62728", # malaysia
    "#9467bd", # philippines
    "#8c564b", # singapore
    "#e377c2", # myanmar
    "#7f7f7f", # cambodia
    "#bcbd22", # laos
    "#17becf", # brunei
    "#332288", # timor-leste
]

# Game configuration

# Updated values with Timor-Leste
NUM_PLAYERS = 11 # number of players
X_INITIAL_LIST = np.array([
    625, 311, 289, 249, 154,
    53, 49, 16, 7, 7, 1
]) / 100 # unit of 1000 Mt

dipl_inf = np.array([66.4, 59.05, 52.35, 55.85, 49,
           57, 22.15, 34.95, 28.45, 32.4, 24.8])
MU_LIST = dipl_inf / np.sum(dipl_inf)

# Without Timor-Leste (previous work)
# NUM_PLAYERS = 10 # number of players
# X_INITIAL_LIST = np.array([
#     625, 311, 289, 249, 154,
#     53, 49, 16, 7, 7
# ]) / 100 # unit of 1e3 Mt

# dipl_inf = [66.4, 59.05, 52.35, 55.85, 49,
#            57, 22.15, 34.95, 28.45, 32.4]
# MU_LIST = dipl_inf / np.sum(dipl_inf)

PSI_LIST = np.load("./output/vars/psi_list.npy")
STEP_SIZE = 0.01
BETA = 1 
LAMBD = 10
NEIGH_LIST = [[i for i in range (NUM_PLAYERS)] for _ in range (NUM_PLAYERS)] # each country is connected to all other ones
