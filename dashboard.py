import dash
import dash_core_components as dcc
import dash_html_components as html
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

# Definir el layout del dashboard
app.layout = html.Div([
    html.H1('Mi Dashboard'),

    dcc.Graph(
        id='grafico-1',
        figure=px.line(df, x='X', y='Y1', title='Gráfico 1')
    ),

    dcc.Graph(
        id='grafico-2',
        figure=px.line(df, x='X', y='Y2', title='Gráfico 2')
    )
])

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)

