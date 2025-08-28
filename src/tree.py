import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree

import matplotlib.pyplot as plt

# Leitura e pré-processamento
data = pd.read_csv('./assets/questionario.csv', sep=';')
data.columns = [
    'id', 'idade', 'renda_familiar', 'investimentos', 'estudante', 'curso', 'transacoes_mensais'
]

# Preprocessamento
for col in ['idade', 'transacoes_mensais']:
    data[col] = pd.to_numeric(data[col], errors='coerce')
    data[col] = data[col].apply(lambda x: np.random.randint(
        0, 100) if x < 0 or pd.isna(x) else x)
    data[col] = data[col].round().astype(int)


for col in ['renda_familiar', 'curso']:
    data[col] = data[col].astype('category')
    data[col] = data[col].cat.codes

data['investimentos'] = data['investimentos'].apply(
    lambda x: 1 if x.strip().lower() == 'sim' else 0
)
data['estudante'] = data['estudante'].apply(
    lambda x: 1 if x.strip().lower() == 'sim' else 0
)

# Variáveis preditoras
X = data[['idade', 'renda_familiar', 'transacoes_mensais', 'estudante']]
y = data['investimentos']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=7
)

clf = DecisionTreeClassifier(max_depth=3, random_state=7)
clf.fit(X_train, y_train)

plt.figure(figsize=(12, 8))
plot_tree(
    clf,
    feature_names=X.columns,
    class_names=['Não', 'Sim'],
    filled=True
)
plt.title("Árvore de Decisão para Previsão de Investimentos")
plt.show()

y_pred = clf.predict(X_test)

novo_dado = pd.DataFrame({
    'idade': [40],
    'renda_familiar': [2],
    'transacoes_mensais': [96],
    'estudante': [0]
})

probabilidade = clf.predict_proba(novo_dado)[0][1]
print(f'Probabilidade de possuir investimentos: {probabilidade:.2f}')
