import plotly.express as px
import pandas as pd

# Datos de ejemplo
df = pd.DataFrame({
    "X": [1, 2, 3, 4, 5],
    "Y": [2, 3, 5, 7, 11]
})

# Crear el gráfico de dispersión
fig = px.scatter(df, x='X', y='Y', title='Gráfico de dispersión')

# Mostrar el gráfico
fig.show()

# Datos de ejemplo
import numpy as np
np.random.seed(0)
x = np.random.randn(1000)

# Crear el histograma
fig = px.histogram(x, title='Histograma')

# Mostrar el gráfico
fig.show()

