Para rodar esse código de servidor MCP (Model Context Protocol) de forma simples, você precisa seguir alguns passos:

## 1. Instalação das dependências

Primeiro, instale o FastMCP:

```bash
pip install fastmcp
```

```bash
pip install 'mcp[cli]'
```

pipx install uv
ou
pip install pipx
pipx ensurepath
pipx install uv

## 2. Estrutura do projeto

Organize seus arquivos assim:

```
projeto/
├── server.py  (seu código)
└── contas_a_pagar.txt  (arquivo de dados)
```

## 3. Criar o arquivo de dados

Crie o arquivo `contas_a_pagar.txt` no mesmo diretório:

```txt
Luz: R$ 120,00
Água: R$ 80,00
Internet: R$ 99,90
Aluguel: R$ 1200,00
```

## 4. Executar o servidor

### Opção 1 - STDIO (mais simples): vai rodar e nada vai acontecer poois nao tem o client

```bash
mcp run app/01basic/server.py
```

### Opção 2 - HTTP/SSE: vai rodar e nada vai acontecer poois nao tem o client

```bash
mcp run app/01basic/server.py --transport sse
```

## Modo depuração: ferrmaneta para testar os servidores ante de criar um cliente

### Opção 3 - Modo desenvolvimento: tem que ter o node instalado para depurar

```bash
mcp dev app/01basic/server.py
```

## passos:

1- Conecte ao servidor
2- No menu superior, selecione List ressources, e cliquem em depesas_mensais. Veja as informações do recurso.
3- No menu prompts, selecione List list prompts, e cliquem em formatar_dado_cadastral. Insira o cpt e clique em get Prompt. Veja as informações do prompt.
3- No menu tools, selecione List list tools, e cliquem em adiciona. Insira os valores e clique em run tool. Veja as informações.

## 5. Testando

Para testar se está funcionando, você pode usar um cliente MCP ou integrar com aplicações que suportam MCP (como o Claude Desktop).

## Dica adicional

Se você quiser um exemplo mais completo, salve seu código como `server.py` e execute:Com esse código completo, você pode simplesmente executar:

```bash
python server.py
```

O servidor criará automaticamente o arquivo `contas_a_pagar.txt` se ele não existir e ficará rodando, pronto para receber conexões MCP.
