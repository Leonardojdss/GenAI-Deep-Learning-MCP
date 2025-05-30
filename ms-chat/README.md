# Chat de Consulta ao Modelo de Crédito

Este diretório contém a aplicação de chat que permite a interação com o modelo de risco de crédito via interface conversacional.

## Estrutura

- `app.py`: Script principal para iniciar a interface de chat.
- `client_server_claude.py`: Cliente responsável por se comunicar com o servidor MCP e obter previsões.

## Como iniciar o chat

1. **Instale as dependências**
   - Certifique-se de que o ambiente virtual está ativado e as dependências do `requirements.txt` na raiz do projeto estão instaladas:

```bash
pip install -r requirements.txt
```

2. **Execute o chat**

```bash
cd ms-chat
streamlit run app.py
```

A interface de chat será iniciada e você poderá interagir para consultar previsões de risco de crédito.

## Funcionalidades
- Envia dados para o servidor MCP e exibe a resposta do modelo preditivo.
- Permite simular diferentes cenários de análise de crédito de forma interativa.

## Observações
- O servidor MCP deve estar em execução para que o chat funcione corretamente.
- Ideal para demonstrações, testes e integração com fluxos de atendimento automatizado.
