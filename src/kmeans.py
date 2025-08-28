import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

data = pd.read_csv('./assets/questionario.csv', sep=';')

data.columns = [
    'id', 'idade', 'renda_familiar', 'investimentos', 'estudante', 'curso', 'transacoes_mensais'
]

# Preprocessamento
for col in ['idade', 'transacoes_mensais']:
    data[col] = pd.to_numeric(data[col], errors='coerce')
    data[col] = data[col].apply(
        lambda x: np.random.randint(0, 100) if x < 0 or pd.isna(x) else x
    )
    data[col] = data[col].round().astype(int)

for col in ['renda_familiar', 'investimentos', 'estudante', 'curso']:
    data[col] = data[col].astype('category')
    data[col] = data[col].cat.codes

# Seleção de variáveis para KMeans
X = data[['idade', 'investimentos', 'transacoes_mensais']].values

# Aplicar KMeans
kmeans = KMeans(n_clusters=3, random_state=7)
labels = kmeans.fit_predict(X)
data['cluster'] = labels

# Plotagem
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.scatter(data['idade'], data['transacoes_mensais'],
            c=data['cluster'], cmap='viridis', alpha=0.6)
plt.xlabel('Idade')
plt.ylabel('Transações Mensais')
plt.title('Clusters de Usuários')
plt.colorbar(label='Cluster')

plt.subplot(1, 3, 2)
plt.scatter(data['investimentos'], data['transacoes_mensais'],
            c=data['cluster'], cmap='viridis', alpha=0.6)
plt.xlabel('Investimentos')
plt.ylabel('Transações Mensais')
plt.title('Clusters de Usuários')
plt.colorbar(label='Cluster')

plt.subplot(1, 3, 3)
tsne = TSNE(n_components=2, random_state=7, perplexity=30)
X_tsne = tsne.fit_transform(X)
plt.scatter(X_tsne[:, 0], X_tsne[:, 1],
            c=data['cluster'], cmap='viridis', alpha=0.6)
plt.title('t-SNE de Clusters de Usuários')
plt.colorbar(label='Cluster')

plt.tight_layout()
plt.show()
