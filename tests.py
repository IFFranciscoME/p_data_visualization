
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
# ------------------------------------------------------------------------------- ---------------------- -- #

price_data = pd.read_csv('data/ohlc_data.csv')
panel_data = pd.read_csv('data/panel_data.csv')
optim_data = pd.read_csv('data/optimization_data.csv')

# ------------------------------------------------------------------------------------------------ Tests -- #
# ------------------------------------------------------------------------------------------------ ----- -- #

# -- ------------------------------------------------------------------ PLOT: 2 Timeseries with 2 Y-Axis -- #

# p_x = {'data': price_data['timestamp'], 'x_ticks': 5}
# p_y0 = {'data': price_data['close'], 'color': '#ABABAB', 'type': 'dash', 'size': 2.5, 'n_ticks': 5}
# p_y1 = {'data': price_data['high'], 'color': '#ABAEEE', 'type': 'dash', 'size': 2.5, 'n_ticks': 5}
# p_theme = {'color_1': '#ABABAB', 'color_2': '#ABCDE', 'font_size_1': 12, 'font_size_2': 16}
# p_dims = {'width': 1080, 'height': 720}
#
# plot_1 = vs.g_ts_2axis(p_x=p_x, p_y0=p_y0, p_y1=p_y1, p_theme=p_theme, p_dims=p_dims)
# plot_1.show()

# -- --------------------------------------------------------------------- PLOT: Stacked Horizontal Bars -- #

# p_y0 = {'data': panel_data['dd'], 'color': 'blue', 'type': 'dash', 'size': 2.5, 'n_ticks': 5}
# p_y1 = {'data': panel_data['profit'], 'color': 'red', 'type': 'dash', 'size': 2.5, 'n_ticks': 5}
# p_theme = {'color_1': '#ABABAB', 'color_2': 'white', 'color_3': 'grey', 'font_color_1': '#ABABAB',
#            'font_size_1': 12, 'font_size_2': 16}
# p_dims = {'width': 1080, 'height': 720}
#
# plot_2 = vs.g_relative_bars(p_y0=p_y0, p_y1=p_y1, p_theme=p_theme, p_dims=p_dims)
# plot_2.show()

# -- -------------------------------------------------------- PLOT: OHLC Price Chart with vertical lines -- #

# p_ohlc = price_data.iloc[3:32, :].reset_index(drop=True)
# p_theme = {'color_1': '#ABABAB', 'color_2': '#ABCDED', 'font_size_1': 12, 'font_size_2': 16}
# p_dims = {'width': 1080, 'height': 720}
# p_vlines = [pd.to_datetime('2020-01-01 22:05:00'), pd.to_datetime('2020-01-01 22:10:00')]
#
# plot_3 = vs.g_ohlc(p_ohlc=p_ohlc, p_theme=p_theme, p_dims=p_dims, p_vlines=p_vlines)
# plot_3.show()

# -- ---------------------------------------------------------------- PLOT: Multiple TimeSeries 1 Y-axis -- #

p_series = {'close': price_data['close'].reset_index(drop=True),
            'high': price_data['high'].reset_index(drop=True),
            'low': price_data['low'].reset_index(drop=True)}

p_ts = price_data['timestamp'].reset_index(drop=True)

p_theme = {'color_1': '#ABABAB', 'color_2': '#ABCDED', 'font_size_1': 12, 'font_size_2': 16}
p_dims = {'width': 1080, 'height': 720}
