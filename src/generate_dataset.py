import pandas as pd
import numpy as np

renda_opcoes = ['Até R$3.000', 'Entre R$3.000 e R$8.000', 'Acima de R$8.000']
investimentos_opcoes = ['Sim', 'Não']
estudante_opcoes = ['Sim', 'Não']
cursos_opcoes = [
    'Engenharia Ambiental',
    'Engenharia de Controle e Automação',
    'Ciência e Tecnologia de Materiais',
    'Ciências Ambientais',
    'Engenharia Elétrica',
    'Outro',
    'Nenhum'
]

n = 1000

ids = np.arange(1, n + 1)
idades = np.random.randint(17, 80, size=n)
renda_familiar = np.random.choice(renda_opcoes, size=n, p=[0.3, 0.5, 0.2])
investimentos = np.random.choice(investimentos_opcoes, size=n, p=[0.4, 0.6])
estudantes = np.random.choice(estudante_opcoes, size=n, p=[0.7, 0.3])
cursos = np.random.choice(cursos_opcoes, size=n)
transacoes_mensais = np.random.randint(0, 100, size=n)

df = pd.DataFrame({
    'id': ids,
    'idade': idades,
    'renda_familiar': renda_familiar,
    'investimentos': investimentos,
    'estudante': estudantes,
    'curso': cursos,
    'transacoes_mensais': transacoes_mensais
})

df.to_csv('./assets/questionario.csv', index=False, sep=';')

print("CSV gerado com sucesso!")
