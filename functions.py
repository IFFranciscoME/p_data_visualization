
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: data visualization codes for python                                                        -- #
# -- script: functions.py : script with data visualization functions                                -- #
# -- author: FranciscoME                                                                                 -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository: https://github.com/IFFranciscoME/p_data_visualization                                   -- #
# -- --------------------------------------------------------------------------------------------------- -- #

# -- -------------------------------------------------- PLOT: (Pending) price chart with trading signals -- #
# -- --------------------------------------------------------------------------------------------------- -- #

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
    p_x = {'data':[], 'x_ticks':5}
    p_y0 = {'data':[], 'color':'#ABABAB', 'type': 'dash', 'size': 1.5, 'n_ticks':5}
    p_y1 = {'data':[], 'color':'#ABABAB', 'type': 'dash', 'size': 1.5, 'n_ticks':5}
    p_theme = {'color_1': '#ABABAB', 'color_2': '#ABABAB', 'font_size_1': 12, 'font_size_2': 16}
    p_dims = {'width': 480, 'heigth': 480}

    """

    # data values and labels for y0
    y0_ticks_n = p_y0['n_ticks']
    y0_ticks_vals = np.arange(min(p_y0), max(p_y0), (max(p_y0) - min(p_y0)) / y0_ticks_n)
    y0_ticks_vals = np.append(y0_ticks_vals, max(p_y0))
    y0_ticks_text = [str("%.4f" % i) for i in y0_ticks_vals]

    # data values and labels for y1
    y1_ticks_n = p_y1['n_ticks']
    y1_ticks_vals = np.arange(min(p_y1), max(p_y1), (max(p_y1) - min(p_y1)) / y1_ticks_n)
    y1_ticks_vals = np.append(y1_ticks_vals, max(p_y1))
    y1_ticks_text = [str("%.4f" % i) for i in y1_ticks_vals]

    # figure object
    fig_g_lineas = go.Figure()

    # add first series (y0)
    fig_g_lineas.add_trace(
        go.Scatter(y=p_y0, name="Serie original",
                   line=dict(color=p_y0['color'], width=p_y0['size'], dash=p_y0['type'])))

    # add second series (y1)
    fig_g_lineas.add_trace(
        go.Scatter(y=p_y1, name="Serie patron encontrado", yaxis="y2",
                   line=dict(color=p_y1['color'], width=p_y1['size'], dash=p_y1['type'])))

    # general layout
    fig_g_lineas.update_layout(

        # x axis modifications
        xaxis=dict(tickvals=p_x),

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
