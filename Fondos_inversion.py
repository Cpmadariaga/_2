import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Datos de ejemplo (simulados)
data = {
    'Fecha': pd.date_range(start='202-01-01', periods=100),
    'Fondo_A': pd.Series(range(100)),
    'Fondo_B': pd.Series(range(100, 200)),
    'Fondo_C': pd.Series(range(50, 150))
}
df = pd.DataFrame(data)

# Crear la aplicación Dash
app = dash.Dash(__name__)

# Layout del dashboard
app.layout = html.Div([
    html.H1('Dashboard de Fondos de Inversión'),

    # Gráfico de líneas para mostrar el rendimiento histórico de los fondos
    dcc.Graph(
        id='grafico-rendimiento',
        figure=px.line(df, x='Fecha', y=df.columns[1:], title='Rendimiento Histórico de Fondos')
    ),

    # Dropdown para seleccionar fondos
    html.Label('Selecciona Fondos:'),
    dcc.Dropdown(
        id='dropdown-fondos',
        options=[{'label': col, 'value': col} for col in df.columns[1:]],
        value=df.columns[1:],
        multi=True
    ),

    # Gráfico de barras para comparar fondos seleccionados
    dcc.Graph(id='grafico-comparativo')
])

# Callback para actualizar el gráfico comparativo según los fondos seleccionados
@app.callback(
    dash.dependencies.Output('grafico-comparativo', 'figure'),
    [dash.dependencies.Input('dropdown-fondos', 'value')]
)
def actualizar_grafico_comparativo(selected_funds):
    return px.line(df, x='Fecha', y=selected_funds, title='Comparación de Fondos')

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
