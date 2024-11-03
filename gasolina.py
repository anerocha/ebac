
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Ler os dados do CSV
data = pd.read_csv('gasolina.csv')

# Criar o gráfico
plt.figure(figsize=(10, 6))
sns.lineplot(data=data, x='dia', y='venda', marker='o')
plt.title('Preço Médio de Venda da Gasolina em São Paulo (Julho 2021)')
plt.xlabel('Dia')
plt.ylabel('Preço (R$)')
plt.legend(['Preço da Gasolina'])
plt.grid(True)

# Salvar o gráfico
plt.savefig('gasolina.png')
