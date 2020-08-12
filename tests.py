
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: data visualization codes for python                                                        -- #
# -- file: tests.py / tests for the data visualization functions                                         -- #
# -- author: FranciscoME                                                                                 -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository: https://github.com/IFFranciscoME/p_data_visualization                                   -- #
# -- --------------------------------------------------------------------------------------------------- -- #

import visualizations as vs                      # import visualizations functions

import plotly.graph_objs as go                   # objetos de imagenes para funcion principal
import plotly.io as pio                          # renderizador para visualizar imagenes
import numpy as np                               # funciones numericas
import pandas as pd                              # dataframes
pio.renderers.default = "browser"                # render de imagenes para correr en script


# ------------------------------------------------------------------------------- Load Data for Examples -- #

price_data = pd.read_csv('data/ohlc_data.csv')
panel_data = pd.read_csv('data/panel_data.csv')
optim_data = pd.read_csv('data/optimization_data.csv')

# ------------------------------------------------------------------------------------------------ Tests -- #

# -- PLOT: 2 Timeseries with 2 Y-Axis -- #

# p_x = {'data': price_data['timestamp'], 'x_ticks': 5}
# p_y0 = {'data': price_data['close'], 'color': '#ABABAB', 'type': 'dash', 'size': 2.5, 'n_ticks': 5}
# p_y1 = {'data': price_data['high'], 'color': '#ABAEEE', 'type': 'dash', 'size': 2.5, 'n_ticks': 5}
# p_theme = {'color_1': '#ABABAB', 'color_2': '#ABCDE', 'font_size_1': 12, 'font_size_2': 16}
# p_dims = {'width': 1080, 'height': 720}
#
# plot_1 = vs.g_ts_2axis(p_x=p_x, p_y0=p_y0, p_y1=p_y1, p_theme=p_theme, p_dims=p_dims)
# plot_1.show()

# -- PLOT: Stacked Horizontal Bars -- #
#
# p_y0 = {'data': panel_data['dd'], 'color': 'blue', 'type': 'dash', 'size': 2.5, 'n_ticks': 5}
# p_y1 = {'data': panel_data['profit'], 'color': 'red', 'type': 'dash', 'size': 2.5, 'n_ticks': 5}
# p_theme = {'color_1': '#ABABAB', 'color_2': 'white', 'color_3': 'grey', 'font_color_1': '#ABABAB',
#            'font_size_1': 12, 'font_size_2': 16}
# p_dims = {'width': 1080, 'height': 720}
#
# plot_2 = vs.g_relative_bars(p_y0=p_y0, p_y1=p_y1, p_theme=p_theme, p_dims=p_dims)
# plot_2.show()

# -- PLOT: OHLC Price Chart -- #

p_ohlc = price_data.iloc[3:32, :].reset_index(drop=True)
p_theme = {'color_1': '#ABABAB', 'color_2': '#ABCDED', 'font_size_1': 12, 'font_size_2': 16}
p_dims = {'width': 1080, 'height': 720}

plot_3 = vs.g_ohlc(p_ohlc=p_ohlc, p_theme=p_theme, p_dims=p_dims, p_trades={})
plot_3.show()

# -- PLOT: (Pending) 4D Surface with trace points -- #

# lists with unique values for x and y
# variable_x = 'TakeProfit'
# variable_y = 'Layer_Multiplier'
# variable_w = 'MaxTrades'
# variable_z1 = 'Profit'
# variable_z2 = 'Drawdown $'
# search_space = optim_data[[variable_z1, variable_x, variable_y, variable_w]]
# search_space.columns = ['z', 'x', 'y', 'w']

# x_l = sorted(set(vals[variable_x]))
# y_l = sorted(set(vals[variable_y]))
# df_ss = pd.DataFrame(np.zeros((len(x_l), len(y_l))))
# df_ss.columns = x_l
# df_ss.index = y_l
#
# # find the resulting value of each x and y combination
# i = 0
# j = 0
#
# df_ss.loc[list(df_ss.columns).index(x_l[i])] = 1
# nuevo_vals = vals[vals[variable_y] == vals[variable_y][j]]
#
# fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='markers')])
# fig.show()
