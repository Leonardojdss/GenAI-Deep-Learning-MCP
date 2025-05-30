# GenAI Machine Learning MCP

Este projeto é uma solução completa para análise de risco de crédito utilizando machine learning, composta por três principais módulos:

- **Pipeline de Machine Learning**: Responsável pelo treinamento, avaliação e salvamento do modelo preditivo.
- **Servidor MCP (Model Context Protocol)**: Expõe o modelo treinado como uma API para consumo externo.
- **Chat de Consulta**: Interface conversacional para consulta ao modelo de risco de crédito.

---

## Estrutura do Projeto

```
├── pipeline-machine-learning/   # Pipeline de ML e geração do modelo
├── ms-mcp-server/              # Servidor MCP para servir o modelo via API
├── ms-chat/                    # Chat para consulta ao modelo
├── requirements.txt            # Dependências do projeto
└── README.md                   # (Este arquivo)
```

---

## Como utilizar

### 1. Gerar o modelo preditivo
Acesse o diretório `pipeline-machine-learning/` e siga as instruções do README local para treinar e salvar o modelo.

### 2. Iniciar o servidor MCP
Acesse o diretório `ms-mcp-server/` e siga as instruções do README local para iniciar o servidor e expor o modelo via API.

### 3. Rodar o chat
Acesse o diretório `ms-chat/` e siga as instruções do README local para iniciar a interface de chat e consultar o modelo.

---

## Requisitos
- Python 3.8+
- Instale as dependências com:

```bash
pip install -r requirements.txt
```

---

## Observações
- Certifique-se de seguir a ordem: pipeline → servidor MCP → chat (Inserir a rota mcp http://localhost:8000/mcp).
- Cada módulo possui um README detalhado com instruções específicas.
- O projeto é modular e pode ser expandido para outros casos de uso de machine learning.

---

## Licença
Este projeto está licenciado sob os termos do arquivo LICENSE.
