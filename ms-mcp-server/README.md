# Servidor MCP (Model Context Protocol)

Este diretório contém a implementação do servidor MCP, responsável por expor o modelo preditivo de risco de crédito como uma API para consumo externo.

## Estrutura

- `mcp_server.py`: Script principal para inicializar o servidor MCP.
- `api/tools.py`: Ferramenta preditiva.

## Como iniciar o servidor MCP

1. **Instale as dependências**
   - Certifique-se de que o ambiente virtual está ativado e as dependências do `requirements.txt` na raiz do projeto estão instaladas:

```bash
pip install -r requirements.txt
```

2. **Execute o servidor**

```bash
cd ms-mcp-server
uvicorn mcp_server:app --host 0.0.0.0 --port 8000
```

O servidor será iniciado e ficará disponível para receber requisições.

## Funcionalidades
- Executa o modelo treinado salvo em `pipeline-machine-learning/model/model_credit_risk.pkl`.
- Expõe endpoints para realizar previsões de risco de crédito.

## Observações
- Certifique-se de que o modelo preditivo já foi treinado e salvo antes de iniciar o servidor MCP.
- O servidor pode ser integrado a outros sistemas, como o chat, para fornecer previsões em tempo real.
