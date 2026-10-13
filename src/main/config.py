import numpy as np

COUNTRY_NAMES = ['Indonesia', 'Vietnam', 'Thailand', 'Malaysia', 'Philippines', 'Singapore', 
                    'Myanmar', 'Cambodia', 'Laos', 'Brunei', 'Timor-Leste']

COUNTRY_CODES = {COUNTRY_NAMES[i] : i for i in range (len(COUNTRY_NAMES))}

CUSTOM_CMAP =  [
    "#1f77b4",
    "#ff7f0e",
    "#2ca02c",
    "#d62728",
    "#9467bd",
    "#8c564b",
    "#e377c2",
    "#7f7f7f",
    "#bcbd22",
    "#17becf",
    "#332288",
]

# Game configuration
NUM_PLAYERS = 11 # number of players
STEP_SIZE = 0.01
BETA, LAMBD = 1, 4
NEIGH_LIST = [[i for i in range (NUM_PLAYERS)] for _ in range (NUM_PLAYERS)] # each country is connected to all other ones

X_INITIAL_LIST = np.array([
    625, 311, 289, 249, 154,
    53, 49, 16, 7, 7, 1
])

MU_LIST = [66.4, 59.05, 52.35, 55.85, 49,
           57, 22.15, 34.95, 28.45, 32.4, 24.8]