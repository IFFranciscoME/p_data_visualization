
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: data visualization codes for python                                                        -- #
# -- script: visualizations.py : script with data visualization functions                                -- #
# -- author: FranciscoME                                                                                 -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository: https://github.com/IFFranciscoME/p_data_visualization                                   -- #
# -- --------------------------------------------------------------------------------------------------- -- #


import plotly.graph_objs as go                   # objetos de imagenes para funcion principal
import plotly.io as pio                          # renderizador para visualizar imagenes
import numpy as np                               # funciones numericas
pio.renderers.default = "browser"                # render de imagenes para correr en script


# -- --------------------------------------------------- PLOT: Timeseries double plot with double y-axis -- #
# -- --------------------------------------------------------------------------------------------------- -- #

def g_ts_2axis(p_x, p_y0, p_y1, p_theme, p_dims):
    """
    Time series line plot with 2 series, sharing the same x component, but with 2 separate y axis

    Parameters
    ----------
    p_x : np.array : x component of the data
    p_y0 : np.array : y1 component of the data
    p_y1 : np.array : y2 component of the data
    p_theme : dict : theme for the visualization
    p_dims : dict : dimensions for the final plot (heigth, width)

    Returns
    -------
    fig_ts_2axis : fig : resulting plot

    Debugging
    ---------
    p_x = []
    p_y1 = []
    p_y2 = []
    p_theme = tema_base
    p_dims = {'width': 480, 'heigth': 480}

    """

    # Determinar los valores y los textos para el eje y0
    y0_ticks_n = 5
    y0_ticks_vals = np.arange(min(p_y0), max(p_y0), (max(p_y0) - min(p_y0)) / y0_ticks_n)
    y0_ticks_vals = np.append(y0_ticks_vals, max(p_y0))
    y0_ticks_text = [str("%.4f" % i) for i in y0_ticks_vals]

    # Determinar los valores y los textos para el eje y1
    y1_ticks_n = 5
    y1_ticks_vals = np.arange(min(p_y1), max(p_y1), (max(p_y1) - min(p_y1)) / y1_ticks_n)
    y1_ticks_vals = np.append(y1_ticks_vals, max(p_y1))
    y1_ticks_text = [str("%.4f" % i) for i in y1_ticks_vals]

    # figure object
    fig_g_lineas = go.Figure()

    # add first series
    fig_g_lineas.add_trace(
        go.Scatter(y=p_y0, name="Serie original",
                   line=dict(color=p_theme['color_linea_1'],
                             width=p_theme['tam_linea_2'])))

    # add second series
    fig_g_lineas.add_trace(
        go.Scatter(y=p_y1, name="Serie patron encontrado", yaxis="y2",
                   line=dict(color=p_theme['color_linea_2'],
                             width=p_theme['tam_linea_2'], dash='dash')))

    # general layout
    fig_g_lineas.update_layout(

        # x axis modifications
        xaxis=dict(tickvals=p_x),

        # first y axis modifications (left)
        yaxis=dict(tickvals=y0_ticks_vals, ticktext=y0_ticks_text, zeroline=False, automargin=True,
                   showgrid=True, tickfont=dict(color=p_theme['color_linea_1'],
                                                size=p_theme['tam_texto_ejes'])),
        # second y axis modifications (right)
        yaxis2=dict(tickvals=y1_ticks_vals, ticktext=y1_ticks_text, zeroline=False, automargin=True,
                    showgrid=True, tickfont=dict(color=p_theme['color_linea_2'],
                                                 size=p_theme['tam_texto_ejes']),

                    overlaying="y", side="right"))

    # layout for the legend
    fig_g_lineas.update_layout(
        legend=go.layout.Legend(x=.2, y=-.2, font=dict(size=p_theme['tam_texto_leyenda'],
                                                       color=p_theme['color_texto_leyenda'])),
        legend_orientation="h")

    # margin modification
    fig_g_lineas.update_layout(autosize=False, width=1240, height=400, paper_bgcolor="white",
                               margin=go.layout.Margin(l=55, r=65, b=5, t=5, pad=1))

    # text anotations
    fig_g_lineas.update_layout(annotations=[

        # first series name
        go.layout.Annotation(x=0, y=0.35, text="Serie Original", textangle=-90,
                             xref="paper", yref="paper", showarrow=False,
                             font=dict(size=p_theme['tam_texto_grafica'],
                                       color=p_theme['color_linea_1'])),
        # second series name
        go.layout.Annotation(x=1, y=0.35, text="Serie Patron Encontrado", textangle=-90,
                             xref="paper", yref="paper", showarrow=False,
                             font=dict(size=p_theme['tam_texto_grafica'],
                                       color=p_theme['color_linea_2']))])

    # format to main title
    fig_g_lineas.update_layout(margin=go.layout.Margin(l=50, r=50, b=20, t=50, pad=20),
                               title=dict(x=0.5, text='<b> Serie Original </b> - '),
                               legend=go.layout.Legend(x=.3, y=-.15, orientation='h', font=dict(size=15)))

    # final plot dimensions
    fig_g_lineas.layout.autosize = True
    fig_g_lineas.layout.width = p_dims['figura_1']['width']
    fig_g_lineas.layout.height = p_dims['figura_1']['height']

    return fig_g_lineas
