Para rodar o código do cliente e do servidor MCP (Model Context Protocol), você precisa seguir alguns passos:

## 1. Execução do mcp client STDIO

```bash
python app/02MCPClient/client_example.py
```

## 2. Execução do mcp server STDIO

```bash
mcp run app/01MCPServer/server.py
```

Resposta:

```bash
Listando tools
[08/04/25 22:45:11] INFO     Processing request of type ListToolsRequest                  server.py:625
Nome: adiciona, Descrição: Ferramenta para soma de dois números inteiros
Chamando a ferramenta adiciona
                    INFO     Processing request of type CallToolRequest                   server.py:625
21

Listando resources
                    INFO     Processing request of type ListResourcesRequest              server.py:625
name='despesas_mensais' title=None uri=AnyUrl('memory://despesas_mensais') description='Lista de despesas mensais registradas' mimeType='text/plain' size=None annotations=None meta=None
Acessando recurso despesas_mensais
                    INFO     Processing request of type ReadResourceRequest               server.py:625
Luz: R$ 120,00
Água: R$ 80,00
Internet: R$ 99,90
Aluguel: R$ 1200,00

Listando prompts
                    INFO     Processing request of type ListPromptsRequest                server.py:625
name='formatar_dado_cadastral' title=None description='Prompt para formatar dados cadastrais' arguments=[PromptArgument(name='cpf', description=None, required=True)] meta=None
Formatando Dado Cadastral
                    INFO     Processing request of type GetPromptRequest                  server.py:625
Formate o CPF informado no padrão xxx.xxx.xxx-xx: 12312312312
```
