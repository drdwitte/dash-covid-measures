import plotly.graph_objects as go


def generate_traces_areaplot(df_datahub, country, measures):
    all_traces = []
    mask_country = df_datahub['id'] == country
    df = df_datahub[mask_country]

    for measure in measures:

        trace1 = go.Scatter(x=df['date'],
                            y=df[measure],
                            name=measure,
                            mode='lines',
                            yaxis='y1',
                            stackgroup='one',
                            hoverinfo='x+y+text',
                            hovertext=measure,
                            )

        all_traces.append(trace1)


    return all_traces


def generate_traces_lineplot(df_datahub, country, what_2_plot):
    all_traces = []
    mask_country = df_datahub['id'] == country
    df = df_datahub[mask_country]

    colors = ['black', 'white', 'grey', 'blue', 'green', 'red']

    for i, pl in enumerate(what_2_plot):

        if pl == 'new_cases':
            column = df['confirmed'].diff().fillna(0).rolling(7).mean()
        elif pl == 'new_deaths':
            column = df['deaths'].diff().fillna(0).rolling(7).mean()

        else:
            column = df[pl].rolling(7).mean()


        trace = go.Scatter(x=df['date'],
                           y =  column,
                           name=pl,
                           mode='lines',
                           yaxis='y2',
                           line={
                               "color": colors[i%len(colors)],
                               "width": 5,

                           },
                           hoverinfo='x+y+text',
                           hovertext=pl
                           )
        all_traces.append(trace)




    return all_traces


def generate_traces_layout(country):
    layout = go.Layout(
        {
            "title": "Covid Measures "+country,
            'xaxis': {
                'title_text': 'Date',
                'showspikes': True,
                'spikethickness': 1,
                'spikecolor': 'black',
                'range': ["2020-02-01", "2020-07-01"]
            },
            "yaxis": {
                "title_text": "Strength",
                "side":       "left",
                'showspikes': True,
                'spikethickness': 1,
                'spikecolor': 'black',
                'range': [0,30]
            },
            "yaxis2": {
                "title_text": "",
                "side":       "right",
                "overlaying": 'y',
                'showspikes': True,
                'spikethickness': 1,
                'spikecolor': 'black',


            },

        },
        showlegend=False,
        plot_bgcolor='rgb(254, 254, 254)'
    )

    return layout