
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: data visualization codes for python                                                        -- #
# -- script: visualizations.py : script with data visualization functions                                -- #
# -- author: FranciscoME                                                                                 -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository: https://github.com/IFFranciscoME/p_data_visualization                                   -- #
# -- --------------------------------------------------------------------------------------------------- -- #

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
pio.renderers.default = "browser"

# -- ------------------------------------------------------ PLOT: (Pending) 4D Surface with trace points -- #
# -- --------------------------------------------------------------------------------------------------- -- #


# -- ------------------------------------------------------ PLOT: Multiple Timeseries plot with 1 Y-axis -- #
# -- --------------------------------------------------------------------------------------------------- -- #

def g_mult_ts(p_series, p_ts, p_theme, p_dims):
    """
    Multiple Timeseries plots with a single Y-Axis and vertical/horizontal legend

    Requirements
    ------------
    numpy
    pandas
    plotly

    Parameters
    ----------
    p_series
    p_theme
    p_dims
    p_ts

    Returns
    -------
    fig_g_mult_ts: plotly
        objeto/diccionario tipo plotly para graficar

    Debugging
    ---------
    p_series = p_series
    p_ts = p_ts
    p_theme = p_theme
    p_dims = p_dims

    """

    x_ticks = []
    x_labels = []

    # list of periods for the x axis
    l_periods = pd.date_range(pd.to_datetime(p_ts.to_list()[0]),
                              pd.to_datetime(p_ts.to_list()[-1])).strftime("%m/%y")

    # # calculations for the y axis
    # l_profit = p_y0['data'] / 100
    # y_profit = np.round(np.median(l_profit), 4)
    # l_dde = p_y1['data'] / 100
    # y_dde = np.round(np.median(l_dde), 4)

    # # ticks values for y axis
    # y0_ticks_vals = np.arange(min(l_dde), max(l_profit), (max(l_profit) - min(l_dde)) / 10)
    # y0_ticks_vals = np.append(y0_ticks_vals, max(l_profit))
    # y0_ticks_vals = np.round(y0_ticks_vals, 4)

    data = []
    for name in list(p_series.keys()):
        data.append({"type": 'scatter',
                     "x": p_ts,
                     "y": p_series[name],
                     "name": name,
                     })

    # Base de figura
    fig_g_mult_ts = go.Figure(dict({"data": data}))

    # Layout de margen, titulos y ejes
    fig_g_mult_ts.update_layout(
        margin=go.layout.Margin(l=50, r=50, b=20, t=50, pad=20),
        xaxis=dict(title_text='Hora del dia', rangeslider=dict(visible=False)),
        yaxis=dict(title_text='Precio del EurUsd'))

    # x tick formatting
    fig_g_mult_ts.update_layout(
        xaxis=dict(
            tickmode='array',
            tickvals=[1, 3, 5, 7, 9, 11],
            ticktext=['One', 'Three', 'Five', 'Seven', 'Nine', 'Eleven']
        )
    )

    # layout for the legend
    fig_g_mult_ts.update_layout(legend=go.layout.Legend(x=.45, y=-.15, orientation='h',
                                                        font=dict(size=p_theme['font_size_1'],
                                                                  color=p_theme['color_1'])))

    # debugging
    fig_g_mult_ts.show()

    return fig_g_mult_ts


# -- -------------------------------------------------------- PLOT: OHLC Price Chart with Vertical Lines -- #
# -- --------------------------------------------------------------------------------------------------- -- #

def g_ohlc(p_ohlc, p_theme, p_dims, p_vlines=None):
    """

    Timeseries Candlestick with OHLC prices and figures for trades indicator

    Requirements
    ------------
    numpy
    pandas
    plotly

    Parameters
    ----------
    p_ohlc: pd.DataFrame
        debe de contener las columnas 'timestamp', 'open', 'high', 'low', 'close'
    p_theme: dict
        diccionario con tema de visualizaciones
    p_dims: dict
        diccionario con tamanos para visualizaciones
    p_vlines: list
        lista con fechas donde para visualizar lineas verticales

    Returns
    -------
    fig_g_ohlc: plotly
        objeto/diccionario tipo plotly para graficar

    Debugging
    ---------
    p_ohlc = price_data
    p_timestamp = price_data['timestamp']
    p_theme = tema_base
    p_dims = dimensiones_base
    p_vlines = [pd.to_datetime('2020-01-01 22:05:00'), pd.to_datetime('2020-01-01 22:10:00')]
    """

    # Base de figura
    fig_g_ohlc = go.Figure()

    # Agregar capa de figura de velas japonesas (candlestick)
    fig_g_ohlc.add_trace(
        go.Candlestick(name='ohlc',
                       x=p_ohlc['timestamp'],
                       open=p_ohlc['open'],
                       high=p_ohlc['high'],
                       low=p_ohlc['low'],
                       close=p_ohlc['close'],
                       opacity=0.7))

    # Layout de margen, titulos y ejes
    fig_g_ohlc.update_layout(
        margin=go.layout.Margin(l=50, r=50, b=20, t=50, pad=20),
        xaxis=dict(title_text='Hora del dia', rangeslider=dict(visible=False)),
        yaxis=dict(title_text='Precio del EurUsd'))

    # Color y fuente de texto en ejes
    fig_g_ohlc.update_layout(
        xaxis=dict(titlefont=dict(color=p_theme['color_1']),
                   tickfont=dict(color=p_theme['color_1'],
                                 size=p_theme['font_size_1'])),
        yaxis=dict(zeroline=False, automargin=True,
                   titlefont=dict(color=p_theme['color_1']),
                   tickfont=dict(color=p_theme['color_1'],
                                 size=p_theme['font_size_1']),
                   showgrid=True))

    # Formato de leyenda
    fig_g_ohlc.update_layout(
        legend=go.layout.Legend(x=.3, y=-.15, orientation='h',
                                font=dict(size=p_theme['font_size_1'],
                                          color=p_theme['color_2'])))

    # Formato de tamanos
    fig_g_ohlc.layout.autosize = True
    fig_g_ohlc.layout.width = p_dims['width']
    fig_g_ohlc.layout.height = p_dims['height']

    # Dynamically add vertical lines according to the provided list of x dates.
    shapes_list = list()
    for i in p_vlines:
        shapes_list.append({'type': 'line', 'fillcolor': p_theme['color_1'],
                            'line': {'color': p_theme['color_1'], 'dash': 'dashdot'},
                            'x0': i, 'x1': i, 'xref': 'x',
                            'y0': min(p_ohlc['low']), 'y1': max(p_ohlc['high']), 'yref': 'y'})

    # Update layout
    fig_g_ohlc.update_layout(shapes=shapes_list)

    # Show picture for debugging
    fig_g_ohlc.show()

    return fig_g_ohlc


# -- --------------------------------------------------------------------- PLOT: Stacked Horizontal Bars -- #
# -- --------------------------------------------------------------------------------------------------- -- #

def g_relative_bars(p_y0, p_y1, p_theme, p_dims):
    """

    Generates a plot with two bars (two series of values) and two horizontal lines (medians of each
    series)

    Requirements
    ------------
    numpy
    pandas
    plotly

    Parameters
    ----------

    p_y0: dict
        values for upper bar plot

        {data: y0 component to plot (left axis), color: for this data, type: line/dash/dash-dot,
        size: for this data, n_ticks: number of ticks for this axis}

    p_y1: dict
        values for lower bar plot

        {data: y0 component to plot (right axis), color: for this data, type: line/dash/dash-dot,
        size: for this data, n_ticks: number of ticks for this axis}

    p_theme: dict
        colors and font sizes

        {'color_1': '#ABABAB', 'color_2': '#ABABAB', 'color_3': '#ABABAB', 'font_color_1': '#ABABAB',
        'font_size_1': 12, 'font_size_2': 16}

    p_dims: dict
        final dimensions of the plot as a file

        {'width': width in pixels, 'heigth': height in pixels}

    Returns
    -------
    fig_relative_bars: plotly
        Object with plotly generating code for the plot

    Debugging
    ---------
    p_y0 = df_f_data['c2'].copy()
    p_y1 = df_f_data['c16'].copy()
    p_theme = base_theme

    """

    # list of periods for the x axis
    l_periods = pd.date_range('2017-01-01', '2020-02-28', freq='MS').strftime("%m/%y")

    # calculations for the y axis
    l_profit = p_y0['data'] / 100
    y_profit = np.round(np.median(l_profit), 4)
    l_dde = p_y1['data'] / 100
    y_dde = np.round(np.median(l_dde), 4)

    # ticks values for y axis
    y0_ticks_vals = np.arange(min(l_dde), max(l_profit), (max(l_profit) - min(l_dde)) / 10)
    y0_ticks_vals = np.append(y0_ticks_vals, max(l_profit))
    y0_ticks_vals = np.round(y0_ticks_vals, 4)

    # instantiate a figure object
    fig_relative_bars = go.Figure()

    # add upper bars
    fig_relative_bars.add_trace(go.Bar(name='Return (%)', x=l_periods, y=l_profit,
                                       marker_color=p_y0['color'],
                                       marker_line_color=p_y0['color'],
                                       marker_line_width=1.5, opacity=0.99))
    # add lower bars
    fig_relative_bars.add_trace(go.Bar(name='DrawDown (%)', x=l_periods, y=l_dde,
                                       marker_color=p_y1['color'],
                                       marker_line_color=p_y1['color'],
                                       marker_line_width=1.5, opacity=0.99))

    # Horizontal lines
    lines = [dict(x0=0, x1=1, xref='paper', y0=y_profit, y1=y_profit, yref='y',
                  type='line', line=dict(color=p_theme['color_3'], width=1.5, dash='dashdot')),
             dict(x0=0, x1=1, xref='paper', y0=y_dde, y1=y_dde, yref='y',
                  type='line', line=dict(color=p_theme['color_3'], width=1.5, dash='dashdot'))]

    # Layout
    fig_relative_bars.update_layout(barmode='relative', yaxis_tickformat='.2%',
                                    margin=go.layout.Margin(l=50, r=50, b=20, t=50, pad=20),
                                    xaxis=dict(title_text='month/year', rangeslider=dict(visible=False)),
                                    yaxis=dict(title_text='DrawDown (%)    |    Return(%)'),
                                    shapes=lines)

    # Text anotations inside graph
    fig_relative_bars.update_layout(annotations=[
        go.layout.Annotation(x=36, y=y_profit * 1.2,
                             text="Median Return <b> (" + str(np.round(y_profit * 100, 2)) + "%) </b>",
                             textangle=0,
                             xref="x", yref='y', showarrow=False,
                             font=dict(size=p_theme['font_size_1'],
                                       color=p_theme['color_2'])),
        go.layout.Annotation(x=36, y=y_dde * 1.2,
                             text="Median DrawDown <b>(" + str(np.round(y_dde * 100, 2)) + "%)</b>",
                             textangle=0,
                             xref="x", yref="y", showarrow=False,
                             font=dict(size=p_theme['font_size_1'],
                                       color=p_theme['color_2']))])

    # Update layout for the background
    fig_relative_bars.update_layout(paper_bgcolor='white',
                                    yaxis=dict(tickvals=y0_ticks_vals, zeroline=False, automargin=True,
                                               tickfont=dict(color='grey', size=p_theme['font_size_1'])),
                                    xaxis=dict(tickfont=dict(color='grey', size=p_theme['font_size_1'])))

    # Update layout for the y axis
    fig_relative_bars.update_yaxes(showgrid=True, gridwidth=.25, gridcolor='lightgrey')

    # Legend format
    fig_relative_bars.update_layout(paper_bgcolor='white', plot_bgcolor='white',
                                    legend=go.layout.Legend(x=.41, y=-.15, orientation='h',
                                                            font=dict(size=14, color='grey')),
                                    margin=go.layout.Margin(l=50, r=50, b=50, t=50, pad=10))

    # Saquare in the upper text anotation
    fig_relative_bars.add_shape(type="rect", x0=32, y0=y_profit * 1.1, x1=40, y1=y_profit * 1.3,
                                line=dict(color=p_theme['color_3'], width=2), fillcolor=p_theme['color_3'])

    # Saquare in the lower text anotation
    fig_relative_bars.add_shape(type="rect", x0=32, y0=y_dde * 1.1, x1=40, y1=y_dde * 1.3,
                                line=dict(color=p_theme['color_3'], width=2), fillcolor=p_theme['color_3'])

    # Final plot dimensions
    fig_relative_bars.layout.autosize = True
    fig_relative_bars.layout.width = p_dims['width']
    fig_relative_bars.layout.height = p_dims['height']

    return fig_relative_bars


# -- ------------------------------------------------------------------ PLOT: 2 Timeseries with 2 Y-Axis -- #
# -- --------------------------------------------------------------------------------------------------- -- #

def g_ts_2axis(p_x, p_y0, p_y1, p_theme, p_dims):
    """

    Time series line plot with 2 series, sharing the same x component, but with 2 separate y axis

    Requirements
    ------------
    numpy
    pandas
    plotly

    Parameters
    ----------
    p_x: dict
        {data: x component to plot, x_ticks: number of ticks to show}

    p_y0: dict
        {data: y0 component to plot (left axis), color: for this data, type: line/dash/dash-dot,
        size: for this data, n_ticks: number of ticks for this axis}

    p_y1: dict
        {data: y0 component to plot (right axis), color: for this data, type: line/dash/dash-dot,
        size: for this data, n_ticks: number of ticks for this axis}

    p_theme: dict
        {'color_1': Color to use in plot, 'color_2': Color to use in plot, 'font_size_1': size of
        font to use in plot, 'font_size_2': size of fonto to use in plot}

    p_dims: dict
        {'width': width in pixels, 'heigth': height in pixels}

    Returns
    -------
    fig_ts_2axis:
        fig: plotly figure code for the resulting plot

    Debugging
    ---------
    p_x = {'data':[], 'x_ticks':5}
    p_y0 = {'data':[], 'color':'#ABABAB', 'type': 'dash', 'size': 1.5, 'n_ticks':5}
    p_y1 = {'data':[], 'color':'#ABABAB', 'type': 'dash', 'size': 1.5, 'n_ticks':5}
    p_theme = {'color_1': '#ABABAB', 'color_2': '#ABABAB', 'font_size_1': 12, 'font_size_2': 16}
    p_dims = {'width': 480, 'heigth': 480}

    """

    # ensure the data type  of every entry
    p_y0['data'] = p_y0['data'].astype(np.float64)
    p_y1['data'] = p_y1['data'].astype(np.float64)
    p_x['data'] = p_x['data'].astype(str)

    # data values and labels for y0
    y0_ticks_n = p_y0['n_ticks']
    y0_ticks_vals = np.arange(min(p_y0['data']), max(p_y0['data']),
                              (max(p_y0['data']) - min(p_y0['data'])) / y0_ticks_n)
    y0_ticks_vals = np.append(y0_ticks_vals, max(p_y0['data']))
    y0_ticks_text = [str("%.4f" % i) for i in y0_ticks_vals]

    # data values and labels for y1
    y1_ticks_n = p_y1['n_ticks']
    y1_ticks_vals = np.arange(min(p_y1['data']), max(p_y1['data']),
                              (max(p_y1['data']) - min(p_y1['data'])) / y1_ticks_n)
    y1_ticks_vals = np.append(y1_ticks_vals, max(p_y1['data']))
    y1_ticks_text = [str("%.4f" % i) for i in y1_ticks_vals]

    # figure object
    fig_g_lineas = go.Figure()

    # add first series (y0)
    fig_g_lineas.add_trace(
        go.Scatter(y=p_y0['data'], name="Serie original",
                   line=dict(color=p_y0['color'], width=p_y0['size'], dash=p_y0['type'])))

    # add second series (y1)
    fig_g_lineas.add_trace(
        go.Scatter(y=p_y1['data'], name="Serie patron encontrado", yaxis="y2",
                   line=dict(color=p_y1['color'], width=p_y1['size'], dash=p_y1['type'])))

    # general layout
    fig_g_lineas.update_layout(

        # x axis modifications
        xaxis=dict(tickvals=p_x['data']),

        # first y axis modifications (left)
        yaxis=dict(tickvals=y0_ticks_vals, ticktext=y0_ticks_text, zeroline=False, automargin=True,
                   showgrid=True, tickfont=dict(color=p_theme['color_1'],
                                                size=p_theme['font_size_1'])),
        # second y axis modifications (right)
        yaxis2=dict(tickvals=y1_ticks_vals, ticktext=y1_ticks_text, zeroline=False, automargin=True,
                    showgrid=True, tickfont=dict(color=p_theme['color_1'],
                                                 size=p_theme['font_size_1']),
                    overlaying="y", side="right"))

    # layout for the legend
    fig_g_lineas.update_layout(legend_orientation="h",
                               legend=go.layout.Legend(x=.2, y=-.2, font=dict(size=p_theme['font_size_1'],
                                                                              color=p_theme['color_1'])))

    # margin modification
    fig_g_lineas.update_layout(autosize=False, width=1240, height=400, paper_bgcolor="white",
                               margin=go.layout.Margin(l=50, r=50, b=50, t=50, pad=1))

    # text anotations
    fig_g_lineas.update_layout(annotations=[

        # first series name
        go.layout.Annotation(x=0, y=0.35, text="Serie Original", textangle=-90,
                             xref="paper", yref="paper", showarrow=False,
                             font=dict(size=p_theme['font_size_1'],
                                       color=p_theme['color_1'])),
        # second series name
        go.layout.Annotation(x=1, y=0.35, text="Serie Patron Encontrado", textangle=-90,
                             xref="paper", yref="paper", showarrow=False,
                             font=dict(size=p_theme['font_size_1'],
                                       color=p_theme['color_1']))])

    # format to main title
    fig_g_lineas.update_layout(margin=go.layout.Margin(l=50, r=50, b=20, t=50, pad=20),
                               title=dict(x=0.5, text='<b> Serie Original </b> - '),
                               legend=go.layout.Legend(x=.3, y=-.15, orientation='h', font=dict(size=15)))

    # final plot dimensions
    fig_g_lineas.layout.autosize = True
    fig_g_lineas.layout.width = p_dims['width']
    fig_g_lineas.layout.height = p_dims['height']

    return fig_g_lineas
