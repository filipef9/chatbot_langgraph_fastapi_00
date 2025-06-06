
# FastAPI Chatbot with LangGraph

Um chatbot inteligente construído com FastAPI, LangGraph e Groq LLM, com suporte a WebSocket para comunicação em tempo real.

## 📋 Funcionalidades

- **Chat em tempo real** via WebSocket
- **API REST** para integração
- **Gerenciamento de contexto** com limitação de tokens
- **Memória persistente** por thread/sessão
- **Interface web** integrada
- **Streaming de respostas** em tempo real

## 🚀 Tecnologias Utilizadas

- **FastAPI** - Framework web moderno e rápido
- **LangGraph** - Orquestração de aplicações LLM
- **LangChain** - Framework para desenvolvimento com LLM
- **Groq** - Provedor de LLM (Llama 3.3 70B)
- **Uvicorn** - Servidor ASGI
- **Poetry** - Gerenciamento de dependências
- **WebSockets** - Comunicação em tempo real

## 📁 Estrutura do Projeto

```
├── main.py              # Aplicação FastAPI principal
├── graph.py             # Configuração do LangGraph
├── llm.py               # Configuração do modelo LLM
├── context_manager.py   # Gerenciamento de contexto e tokens
├── template.py          # Template HTML para interface web
├── pyproject.toml       # Configurações do Poetry
└── README.md            # Este arquivo
```

## 🛠️ Instalação e Configuração

### 1. Instalar Dependências

```bash
poetry install
```

### 2. Configurar Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
GROQ_API_KEY=sua_chave_api_groq_aqui
```

### 3. Executar a Aplicação

```bash
poetry run uvicorn main:app --host 0.0.0.0 --port 5000 --reload
```

A aplicação estará disponível em: `http://0.0.0.0:5000`

## 📡 Endpoints da API

### POST /chat

Endpoint para envio de mensagens via HTTP.

**Request Body:**
```json
{
  "messages": ["Olá, como você está?"],
  "thread_id": "usuario123"
}
```

**Response:**
```json
"Olá! Estou bem, obrigado por perguntar. Como posso ajudá-lo hoje?"
```

### WebSocket /ws/{thread_id}

Endpoint para comunicação em tempo real via WebSocket.

**Exemplo de uso:**
```javascript
const ws = new WebSocket('ws://localhost:5000/ws/usuario123');
ws.onmessage = (event) => console.log(event.data);
ws.send('Olá, chatbot!');
```

### GET /

Interface web simples para testar o chatbot via WebSocket.

## 🧠 Como Funciona

### 1. Arquitetura do LangGraph

O chatbot utiliza um grafo simples com um único nó:

```
START → chatbot → END
```

### 2. Gerenciamento de Contexto

- **Contagem de tokens** usando tiktoken
- **Trimming automático** quando o limite é atingido
- **Preservação de mensagens do sistema**
- **Limite padrão**: 4000 tokens

### 3. Memória Persistente

- Cada `thread_id` mantém sua própria sessão
- Histórico de conversas preservado
- Checkpoint automático após cada interação

## 🔧 Personalização

### Alterar o Modelo LLM

Edite o arquivo `llm.py`:

```python
llm = ChatGroq(model="llama-3.1-8b-instant")  # Modelo mais rápido
# ou
llm = ChatGroq(model="mixtral-8x7b-32768")    # Mais contexto
```

### Modificar o Prompt do Sistema

Edite o arquivo `graph.py`:

```python
system_message = "Você é um assistente especializado em..."
```

### Ajustar Limite de Tokens

Edite o arquivo `graph.py`:

```python
state["messages"] = trim_messages(state["messages"], max_tokens=8000)
```

## 🐛 Solução de Problemas

### Erro de WebSocket em HTTPS

Se estiver usando HTTPS, altere no `template.py`:

```javascript
var ws = new WebSocket('wss://' + window.location.hostname + '/ws/123');
```

### Erro de API Key

Certifique-se de que a variável `GROQ_API_KEY` está configurada:

```bash
export GROQ_API_KEY=sua_chave_aqui
```

### Problemas de Dependências

Reinstale as dependências:

```bash
poetry install --no-cache
```

## 📈 Melhorias Futuras

- [ ] Autenticação de usuários
- [ ] Histórico persistente em banco de dados
- [ ] Suporte a múltiplos modelos LLM
- [ ] Interface web mais avançada
- [ ] Métricas e logging
- [ ] Rate limiting
- [ ] Suporte a arquivos/imagens

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 🆘 Suporte

Se você encontrar algum problema ou tiver dúvidas:

1. Verifique os logs do servidor
2. Consulte a documentação do [FastAPI](https://fastapi.tiangolo.com/)
3. Consulte a documentação do [LangGraph](https://langchain-ai.github.io/langgraph/)
4. Abra uma issue neste repositório

---

Feito com ❤️ usando FastAPI e LangGraph
