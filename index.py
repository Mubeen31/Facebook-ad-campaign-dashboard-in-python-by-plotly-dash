import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import dash_table as dt
import pathlib


PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("./data").resolve()

data1 = pd.read_csv(DATA_PATH.joinpath('data.csv'))
data1['campaign date'] = data1[['reporting_start', 'reporting_end']].agg('-'.join, axis=1)
data1['interest'] = data1['interest1'] + data1['interest2'] + data1['interest3']


app = dash.Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}])

app.layout = html.Div([
    html.Div([
        html.Div([
            html.Div([

                html.Div([
                html.H5('World Countries Information', className = 'title_text'),

dcc.Dropdown(id = 'select_date',
                         multi = False,
                         clearable = True,
                         disabled = False,
                         style = {'display': True},
                         value = '19/08/2017-19/08/2017',
                         placeholder = 'Select Date',
                         options = [{'label': c, 'value': c}
                                    for c in data1['campaign date'].unique()], className = 'dcc_compon1'),
        ], className = 'adjust_drop_down_lists'),
            ], className = "title_container_width")
        ], className = "title_container twelve columns")
    ], className = "row flex-display"),

    html.Div([
        html.Div([
               html.Div([
dcc.Graph(id = 'line_chart1',
                      config = {'displayModeBar': False}, className = 'grid_height'),
dcc.Graph(id = 'line_chart2',
                      config = {'displayModeBar': False}, className = 'grid_height'),
dcc.Graph(id = 'line_chart3',
                      config = {'displayModeBar': False}, className = 'grid_height'),
dcc.Graph(id = 'line_chart4',
                      config = {'displayModeBar': False}, className = 'grid_height'),
dcc.Graph(id = 'line_chart5',
                      config = {'displayModeBar': False}, className = 'grid_height'),
dcc.Graph(id = 'line_chart6',
                      config = {'displayModeBar': False}, className = 'grid_height'),

                ], className = 'adjust_drop_down_lists1'),


        ], className = "create_container2 four columns"),

html.Div([

dcc.Graph(id = 'line_chart7',
                      config = {'displayModeBar': 'hover'}),

        ], className = "create_container3 eight columns")

    ], className = "row flex-display")

], id= "mainContainer", style={"display": "flex", "flex-direction": "column"})


@app.callback(Output('line_chart1', 'figure'),
              [Input('select_date', 'value')])

def update_graph(select_date):
    data2 = data1.groupby(['campaign date'])['clicks'].sum().reset_index()
    data2['previous day'] = data2['clicks'].shift(1)
    data2['growth'] = data2['clicks'].pct_change()
    data2.fillna(0, inplace = True)
    data3 = data2[data2['campaign date'] == select_date]

    return {
        'data':[
            go.Indicator(
                mode = 'number+delta',
                value = int(data3['clicks']),
                delta = {'reference': int(data3['previous day']),
                         'valueformat': ',.0f'},
                title = {'text': 'Clicks'},
                domain = {'y': [0, 1], 'x': [0.25, 0.75]}),

            go.Scatter(
                x = data2['campaign date'],
                y = data2['clicks'],
                mode = 'lines',
                fill = 'tozeroy',
                line = dict(width = 2, color = '#38D56F'),
                hoverinfo = 'skip',
            )],


        'layout': go.Layout(
             font = dict(color = '#e55467'),
             plot_bgcolor='#d5f6e1',
             paper_bgcolor='#d5f6e1',
             margin = dict(l = 0, r = 0, t = 0, b = 0),

             xaxis = dict(title = '<b>Years</b>',
                          visible = False,
                          color = 'black',
                          showline = False,
                          showgrid = False,
                          showticklabels = False,
                          linecolor = 'black',
                          linewidth = 1,
                          ticks = 'outside',
                          tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = 'black')

                         ),

             yaxis = dict(title = '<b>Life Expectancy</b>',
                          visible = False,
                          color = 'black',
                          showline = False,
                          showgrid = False,
                          showticklabels = False,
                          linecolor = 'black',
                          linewidth = 1,
                          ticks = '',
                          tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = 'black')

                         ),

        )

    }

@app.callback(Output('line_chart2', 'figure'),
              [Input('select_date', 'value')])

def update_graph(select_date):
    data2 = data1.groupby(['campaign date'])['impressions'].sum().reset_index()
    data2['previous day'] = data2['impressions'].shift(1)
    data2['growth'] = data2['impressions'].pct_change()
    data2.fillna(0, inplace = True)
    data3 = data2[data2['campaign date'] == select_date]

    return {
        'data':[
            go.Indicator(
                mode = 'number+delta',
                value = int(data3['impressions']),
                delta = {'reference': int(data3['previous day']),
                         'valueformat': ',.0f'},
                title = {'text': 'Impressions'},
                domain = {'y': [0, 1], 'x': [0.25, 0.75]}),

            go.Scatter(
                x = data2['campaign date'],
                y = data2['impressions'],
                mode = 'lines',
                fill = 'tozeroy',
                line = dict(width = 2, color = '#FFA07A'),
                hoverinfo = 'skip',
            )],


        'layout': go.Layout(
             font = dict(color = '#e55467'),
             plot_bgcolor='#ffede6',
             paper_bgcolor='#ffede6',
             margin = dict(l = 0, r = 0, t = 0, b = 0),

             xaxis = dict(title = '<b>Years</b>',
                          visible = False,
                          color = 'black',
                          showline = False,
                          showgrid = False,
                          showticklabels = False,
                          linecolor = 'black',
                          linewidth = 1,
                          ticks = 'outside',
                          tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = 'black')

                         ),

             yaxis = dict(title = '<b>Life Expectancy</b>',
                          visible = False,
                          color = 'black',
                          showline = False,
                          showgrid = False,
                          showticklabels = False,
                          linecolor = 'black',
                          linewidth = 1,
                          ticks = '',
                          tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = 'black')

                         ),

        )

    }

@app.callback(Output('line_chart3', 'figure'),
              [Input('select_date', 'value')])

def update_graph(select_date):
    data2 = data1.groupby(['campaign date'])['spent'].sum().reset_index()
    data2['previous day'] = data2['spent'].shift(1)
    data2['growth'] = data2['spent'].pct_change()
    data2.fillna(0, inplace = True)
    data3 = data2[data2['campaign date'] == select_date]

    return {
        'data':[
            go.Indicator(
                mode = 'number+delta',
                value = int(data3['spent']),
                delta = {'reference': int(data3['previous day']),
                         'valueformat': ',.0f'},
                title = {'text': 'Spent'},
                domain = {'y': [0, 1], 'x': [0.25, 0.75]}),

            go.Scatter(
                x = data2['campaign date'],
                y = data2['spent'],
                mode = 'lines',
                fill = 'tozeroy',
                line = dict(width = 2, color = '#9e7700'),
                hoverinfo = 'skip',
            )],


        'layout': go.Layout(
             font = dict(color = '#e55467'),
             plot_bgcolor='#ffecb3',
             paper_bgcolor='#ffecb3',
             margin = dict(l = 0, r = 0, t = 0, b = 0),

             xaxis = dict(title = '<b>Years</b>',
                          visible = False,
                          color = 'black',
                          showline = False,
                          showgrid = False,
                          showticklabels = False,
                          linecolor = 'black',
                          linewidth = 1,
                          ticks = 'outside',
                          tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = 'black')

                         ),

             yaxis = dict(title = '<b>Life Expectancy</b>',
                          visible = False,
                          color = 'black',
                          showline = False,
                          showgrid = False,
                          showticklabels = False,
                          linecolor = 'black',
                          linewidth = 1,
                          ticks = '',
                          tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = 'black')

                         ),

        )

    }

@app.callback(Output('line_chart4', 'figure'),
              [Input('select_date', 'value')])

def update_graph(select_date):
    data2 = data1.groupby(['campaign date'])['interest'].sum().reset_index()
    data2['previous day'] = data2['interest'].shift(1)
    data2['growth'] = data2['interest'].pct_change()
    data2.fillna(0, inplace = True)
    data3 = data2[data2['campaign date'] == select_date]

    return {
        'data':[
            go.Indicator(
                mode = 'number+delta',
                value = int(data3['interest']),
                delta = {'reference': int(data3['previous day']),
                         'valueformat': ',.0f'},
                title = {'text': 'Interest'},
                domain = {'y': [0, 1], 'x': [0.25, 0.75]}),

            go.Scatter(
                x = data2['campaign date'],
                y = data2['interest'],
                mode = 'lines',
                fill = 'tozeroy',
                line = dict(width = 2, color = '#38D5CB'),
                hoverinfo = 'skip',
            )],


        'layout': go.Layout(
             font = dict(color = '#e55467'),
             plot_bgcolor='#c0f2ee',
             paper_bgcolor='#c0f2ee',
             margin = dict(l = 0, r = 0, t = 0, b = 0),

             xaxis = dict(title = '<b>Years</b>',
                          visible = False,
                          color = 'black',
                          showline = False,
                          showgrid = False,
                          showticklabels = False,
                          linecolor = 'black',
                          linewidth = 1,
                          ticks = 'outside',
                          tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = 'black')

                         ),

             yaxis = dict(title = '<b>Life Expectancy</b>',
                          visible = False,
                          color = 'black',
                          showline = False,
                          showgrid = False,
                          showticklabels = False,
                          linecolor = 'black',
                          linewidth = 1,
                          ticks = '',
                          tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = 'black')

                         ),

        )

    }

@app.callback(Output('line_chart5', 'figure'),
              [Input('select_date', 'value')])

def update_graph(select_date):
    data2 = data1.groupby(['campaign date'])['approved_conversion'].sum().reset_index()
    data2['previous day'] = data2['approved_conversion'].shift(1)
    data2['growth'] = data2['approved_conversion'].pct_change()
    data2.fillna(0, inplace = True)
    data3 = data2[data2['campaign date'] == select_date]

    return {
        'data':[
            go.Indicator(
                mode = 'number+delta',
                value = int(data3['approved_conversion']),
                delta = {'reference': int(data3['previous day']),
                         'valueformat': ',.0f'},
                title = {'text': 'Approved Conversion'},
                domain = {'y': [0, 1], 'x': [0.25, 0.75]}),

            go.Scatter(
                x = data2['campaign date'],
                y = data2['approved_conversion'],
                mode = 'lines',
                fill = 'tozeroy',
                line = dict(width = 2, color = '#CCCCFF'),
                hoverinfo = 'skip',
            )],


        'layout': go.Layout(
             font = dict(color = '#e55467'),
             plot_bgcolor='#e6e6ff',
             paper_bgcolor='#e6e6ff',
             margin = dict(l = 0, r = 0, t = 0, b = 0),

             xaxis = dict(title = '<b>Years</b>',
                          visible = False,
                          color = 'black',
                          showline = False,
                          showgrid = False,
                          showticklabels = False,
                          linecolor = 'black',
                          linewidth = 1,
                          ticks = 'outside',
                          tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = 'black')

                         ),

             yaxis = dict(title = '<b>Life Expectancy</b>',
                          visible = False,
                          color = 'black',
                          showline = False,
                          showgrid = False,
                          showticklabels = False,
                          linecolor = 'black',
                          linewidth = 1,
                          ticks = '',
                          tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = 'black')

                         ),

        )

    }

@app.callback(Output('line_chart6', 'figure'),
              [Input('select_date', 'value')])

def update_graph(select_date):
    data2 = data1.groupby(['campaign date'])['total_conversion'].sum().reset_index()
    data2['previous day'] = data2['total_conversion'].shift(1)
    data2['growth'] = data2['total_conversion'].pct_change()
    data2.fillna(0, inplace = True)
    data3 = data2[data2['campaign date'] == select_date]

    return {
        'data':[
            go.Indicator(
                mode = 'number+delta',
                value = int(data3['total_conversion']),
                delta = {'reference': int(data3['previous day']),
                         'valueformat': ',.0f'},
                title = {'text': 'Total Conversion'},
                domain = {'y': [0, 1], 'x': [0.25, 0.75]}),

            go.Scatter(
                x = data2['campaign date'],
                y = data2['total_conversion'],
                mode = 'lines',
                fill = 'tozeroy',
                line = dict(width = 2, color = '#808080'),
                hoverinfo = 'skip',
            )],


        'layout': go.Layout(
             font = dict(color = '#e55467'),
             plot_bgcolor='#e6e6e6',
             paper_bgcolor='#e6e6e6',
             margin = dict(l = 0, r = 0, t = 0, b = 0),

             xaxis = dict(title = '<b>Years</b>',
                          visible = False,
                          color = 'black',
                          showline = False,
                          showgrid = False,
                          showticklabels = False,
                          linecolor = 'black',
                          linewidth = 1,
                          ticks = 'outside',
                          tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = 'black')

                         ),

             yaxis = dict(title = '<b>Life Expectancy</b>',
                          visible = False,
                          color = 'black',
                          showline = False,
                          showgrid = False,
                          showticklabels = False,
                          linecolor = 'black',
                          linewidth = 1,
                          ticks = '',
                          tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = 'black')

                         ),

        )

    }


if __name__ == '__main__':
    app.run_server(debug=True)