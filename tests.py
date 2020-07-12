
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: data visualization codes for python                                                        -- #
# -- file: tests.py / tests for the data visualization functions                                         -- #
# -- author: FranciscoME                                                                                 -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository: https://github.com/IFFranciscoME/p_data_visualization                                   -- #
# -- --------------------------------------------------------------------------------------------------- -- #

import plotly.graph_objs as go                   # objetos de imagenes para funcion principal
import plotly.io as pio                          # renderizador para visualizar imagenes
import numpy as np                               # funciones numericas
from functions import g_ts_2axis as fig_1

pio.renderers.default = "browser"                # render de imagenes para correr en script

# ------------------------------------------------------------------------------- generic data for tests -- #

# Define parameters for the walk
dims = 1
step_n = 1000
step_set = [-1, 0, 1]
origin = np.zeros((1, dims))

# Simulate steps in 1D
step_shape = (step_n, dims)
steps = np.random.choice(a=step_set, size=step_shape)
path = np.concatenate([origin, steps]).cumsum(0)

# ------------------------------------------------------------------------------------------------ Tests -- #
# -- Double time series with separate y-axis

figure = fig_1(p_x=0, p_y0=0, p_y1=0, p_theme=0, p_dims=0)
