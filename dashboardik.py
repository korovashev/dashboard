import dash
from dash import html
from dash import dcc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

colors_1 = ['#0000ff', '#ff0000']
compliant = 4
uncompliant = 2
total_1 = compliant + uncompliant
compliant_percent = compliant / total_1
fig1 = go.Figure(data=[go.Pie(labels=[f'Compliant - {compliant}', f'Uncompliant - {uncompliant}'],
                    values=[compliant, uncompliant],
                    hole=0.8,
                    title='Policies',
                    titleposition='top center',
                    title_font=dict(family='PT Sans Narrow', size=25),
                    name='Policies'
                    )])
fig1.update_traces(hoverinfo='label+percent+value', textinfo='none', marker=dict(colors=colors_1))
fig1.add_annotation(text=f'{compliant_percent:.0%}', font=dict(size=40), x=0.5, y=0.45, showarrow=False)
fig1.update_layout(font=dict(family='PT Sans Narrow', size=20), legend=dict(orientation='h', yanchor='top', y=-0.1, xanchor='center', x=0.5))


colors_2 = ['#008000', '#ff0000']
protected = 16
unprotected = 17
total_2 = protected + unprotected
protected_percent = protected / total_2
fig2 = go.Figure(data=[go.Pie(labels=[f'Protected - {protected}', f'Unprotected - {unprotected}'],
                    values=[protected, unprotected],
                    hole=0.8,
                    title='Virtual Machine',
                    titleposition='top center',
                    title_font=dict(family='PT Sans Narrow', size=25),
                    name='Virtual Machine'
                    )])
fig2.update_traces(hoverinfo='label+percent+value', textinfo='none', marker=dict(colors=colors_2))
fig2.add_annotation(text=f'{protected_percent:.0%}', font=dict(size=40), x=0.5, y=0.45, showarrow=False)
fig2.update_layout(font=dict(family='PT Sans Narrow', size=20), legend=dict(orientation='h', yanchor='top', y=-0.1, xanchor='center', x=0.5))

fig3 = go.Figure(go.Scatter(
    y=[100, 100, 100, 90, 100, 100, 50],
    x=["03.06", "04.06", "05.06", "06.06", "07.06", "08.06", "09.06"], line=dict(color='#008000'),
    name='Backups'))
fig3.update_layout(font=dict(family='PT Sans Narrow', size=20),
    title={
        'text': "Backups",
        'y':0.84,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})

fig4 = go.Figure(go.Scatter(
    y=[0, 8, 4, 12, 5, 0, 25],
    x=["0", "Thu 08", "12", "PM", "Fri 09", "12", "PM"], line=dict(color='#008000'),
    name='Jobs'))
fig4.add_trace(go.Scatter(
    y=[0, 0, 0, 0, 15, 0, 8],
    x=["0", "Thu 08", "12", "PM", "Fri 09", "12", "PM"], line=dict(color='#ff0000')))
fig4.update_layout(font=dict(family='PT Sans Narrow', size=20),
    title={
        'text': "Jobs",
        'y':0.84,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})

fig5 = go.Figure()
fig5.add_trace(go.Scatter(
    y=[0, 20, 15, 20, 20, 10, 50],
    x=[0, "Thu 08", "12", "PM", "Fri 09", "12", "PM"], line=dict(color='#008000'),
    name='Events'))
fig5.add_trace(go.Scatter(
    y=[0, 0, 0, 0, 110, 130, 120],
    x=[0, "Thu 08", "12", "PM", "Fri 09", "12", "PM"], line=dict(color='#ff0000')))
fig5.add_trace(go.Scatter(
    y=[0, 0, 0, 0, 0, 0, 10],
    x=[0, "Thu 08", "12", "PM", "Fri 09", "12", "PM"], line=dict(color='yellow')))
fig5.update_layout(font=dict(family='PT Sans Narrow', size=20),
    title={
        'text': "Events",
        'y':0.84,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})


fig = make_subplots(rows=1, cols=3, specs=[[{'type': 'pie'}, {'type': 'pie'}, {'type': 'xy'}]])
fig.add_trace(fig1.data[0], row=1, col=1)
fig.add_trace(fig2.data[0], row=1, col=2)
fig.add_trace(fig3.data[0], row=1, col=3)

figg = make_subplots(rows=1, cols=3, specs=[[{'type': 'pie'}, {'type': 'xy'}, {'type': 'xy'}]])
figg.add_trace(fig1.data[0], row=1, col=1)
figg.add_trace(fig4.data[0], row=1, col=2)
figg.add_trace(fig5.data[0], row=1, col=3)

fig.update_layout(showlegend=True)
figg.update_layout(showlegend=True)

app = dash.Dash(__name__)
app.layout = html.Div([html.Div([dcc.Graph(figure=fig)]), html.Div([dcc.Graph(figure=figg)])])

if __name__ == '__main__':
    app.run_server(debug=True)

