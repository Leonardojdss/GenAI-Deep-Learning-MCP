# Pipeline de Machine Learning para Classificação de Crédito

Este diretório contém o pipeline de machine learning responsável por treinar, avaliar e salvar o modelo preditivo de risco de crédito.

## Estrutura

- `massa/credit_risk_dataset_original.csv`: Base de dados original utilizada para o treinamento.
- `model/model_credit_risk.pkl`: Modelo treinado salvo em formato pickle.
- `pipeline/Classificacao-credito.ipynb`: Notebook com todo o processo de análise, pré-processamento, treinamento e avaliação do modelo.

## Como executar o pipeline

1. **Abra o notebook**
   - Utilize o Jupyter Notebook ou VS Code para abrir `pipeline/Classificacao-credito.ipynb`.

2. **Execute as células**
   - Siga o notebook para realizar o pré-processamento, treinamento e avaliação do modelo.

3. **Salvar o modelo**
   - O modelo treinado será salvo automaticamente em `model/model_credit_risk.pkl` ao final do notebook.

## Requisitos

- Python 3.8+
- Instale as dependências listadas em `requirements.txt` na raiz do projeto:

```bash
pip install -r requirements.txt
```

## Observações
- Certifique-se de que os caminhos dos arquivos estejam corretos ao executar scripts/notebooks.
- O modelo gerado será utilizado pelo servidor MCP para servir previsões via API.
