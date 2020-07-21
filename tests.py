
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
import visualizations as vs                      # import visualizations functions
import pandas as pd                              # dataframes
pio.renderers.default = "browser"                # render de imagenes para correr en script


# ------------------------------------------------------------------------------- Load Data for Examples -- #

price_data = pd.read_csv('data/USD_MXN.csv')

# ------------------------------------------------------------------------------------------------ Tests -- #

# -- PLOT: 2 Timeseries with 2 Y-Axis -- #

p_x = {'data': price_data['timestamp'], 'x_ticks': 5}
p_y0 = {'data': price_data['close'], 'color': '#ABABAB', 'type': 'dash', 'size': 2.5, 'n_ticks': 5}
p_y1 = {'data': price_data['high'], 'color': '#ABAEEE', 'type': 'dash', 'size': 2.5, 'n_ticks': 5}
p_theme = {'color_1': '#ABABAB', 'color_2': '#ABCDE', 'font_size_1': 12, 'font_size_2': 16}
p_dims = {'width': 1080, 'height': 720}

plot_1 = vs.g_ts_2axis(p_x=p_x, p_y0=p_y0, p_y1=p_y1, p_theme=p_theme, p_dims=p_dims)
plot_1.show()

# -- PLOT: Stacked Horizontal Bars (Test Pending) -- #
