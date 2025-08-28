# Apresentação - UNESP Sorocaba

Esse repositório foi criado para contemplar todo o material utilizado na apresentação realizada pelo [Lucas de Brito Silva](https://www.linkedin.com/in/lucas-brito100/) na UNESP de Sorocaba.

## Estrutura do Projeto

```bash
.
├── README.md
├── assets
│   ├── questionario.csv
│   └── yolov8n.pt
├── requirements.txt
└── src
    ├── generate_dataset.py
    ├── kmeans.py
    ├── tree.py
    └── yolo.py
```

### Descrição

- `assets`: Arquivos de dados e imagens utilizados nos scripts.
- `src`: Scripts principais do projeto.
  - `generate_dataset.py`: Gera o arquivo questionario.csv com dados simulados.
  - `kmeans.py`: Realiza agrupamento dos usuários usando KMeans e visualiza os clusters.
  - `tree.py`: Cria uma árvore de decisão para prever investimentos.
  - `yolo.py`: Executa detecção de objetos em imagens usando YOLO.

## Requisitos

- Python 3.7+
- Instale as dependências com:

  ```bash
     pip install -r requirements.txt
     ```

- Para rodar o YOLO, instale também:

  ```bash
     pip install ultralytics opencv-python
     ```

## Como executar os scripts?

1. Caso queira rodar os scripts `src/kmeans.py` e `src/tree.py`, atualize a variável `data` no código, apontando para o diretório onde está o arquivo `questionario.csv`. Se não tiver nenhum conteúdo para `questionario.csv` execute o arquivo `src/generate_dataset.py` através do seguinte código:

    ```bash
    python src/kmeans.py
    ```

    Será gerado um arquivo `questionario.csv` na pasta assets.

2. Execute cada script conforme desejado:

- Rodar o KMeans:

   ```bash
   python src/kmeans.py
   ```

  - Rodar a árvore de decisão:

   ```bash
   python src/tree.py
   ```

  - Rodar o YOLO (necessário ultralytics e opencv):

   ```bash
   python src/yolo.py
   ```
