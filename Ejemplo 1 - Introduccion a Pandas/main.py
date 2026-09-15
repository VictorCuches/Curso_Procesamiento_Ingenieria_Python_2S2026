# %%
import pandas as pd
# Instalar pandas
# python -m pip install pandas
# Verificar instalacion de pandas
# python -m pip show pandas

# Cargamos el contenido del archivo en la variable df
df = pd.read_csv('cafe_sales.csv')

# %%
# Cómo vienen los primeros registros
print("--- head() ---")
df.head()
print(df.head(2))

# %%

