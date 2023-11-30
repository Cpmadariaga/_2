import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Datos de ejemplo
df = pd.DataFrame({
    "X": [1, 2, 3, 4, 5],
    "Y1": [2, 3, 5, 7, 11],
    "Y2": [1, 4, 6, 8, 9]
})

# Crear la aplicación Dash
app = dash.Dash(__name__)

# Definir el layout del dashboard con pestañas
app.layout = html.Div([
    dcc.Tabs(id='pestanas', value='pestana-1', children=[
        dcc.Tab(label='Gráfico 1', value='pestana-1'),
        dcc.Tab(label='Gráfico 2', value='pestana-2')
    ]),
    html.Div(id='contenido-pestanas')
])

# Callback para cambiar el contenido de las pestañas
@app.callback(
    dash.dependencies.Output('contenido-pestanas', 'children'),
    [dash.dependencies.Input('pestanas', 'value')]
)
def actualizar_contenido_pestanas(valor_pestanas):
    if valor_pestanas == 'pestana-1':
        figura = px.line(df, x='X', y='Y1', title='Gráfico 1')
    elif valor_pestanas == 'pestana-2':
        figura = px.line(df, x='X', y='Y2', title='Gráfico 2')
    return dcc.Graph(figure=figura)

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
