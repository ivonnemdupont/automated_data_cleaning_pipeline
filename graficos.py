# %% Importación de las bibliotecas
import matplotlib.pyplot as plt
import seaborn as sns

# %% Carga de datos
iris = sns.load_dataset("iris")

# %% Exploración de datos
print(iris.head())

# %% Exploración de datos
print(iris.head())

# %% Gráfico de dispersión
sns.scatterplot(x="sepal_length", y="sepal_width", data=iris, hue="species")
plt.title("Gráfico de dispersión de longitud del sépalo vs. ancho del sépalo")
plt.xlabel("Longitud del sépalo")
plt.ylabel("Ancho del sépalo")
plt.show()


# %% Histograma
sns.histplot(data=iris, x="petal_length", hue="species", kde=True)
plt.title("Histograma de longitud del pétalo")
plt.xlabel("Longitud del pétalo")
plt.show()

# %% Boxplot
sns.boxplot(x="species", y="petal_width", data=iris)
plt.title("Diagrama de caja de ancho del pétalo por especie")
plt.xlabel("Especie")
plt.ylabel("Ancho del pétalo")
plt.show()
