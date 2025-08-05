from mcp.server.fastmcp import FastMCP
import os

# criando o nome do servidor
mcp = FastMCP("AssistenteFinanceiro")

# registrar as ferramentas e nome da ferramenta(adiciona)
@mcp.tool()
def adiciona(a: int, b: int) -> int:
    """Ferramenta para soma de dois números inteiros"""
    return a + b

# registrar os recursos e nome do recurso(despesas_mensais)
@mcp.resource("memory://despesas_mensais")
def despesas_mensais() -> str:
    """Lista de despesas mensais registradas"""
    try:
        # carregar os arquivos contas a pagar
        SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
        FILE_PATH = os.path.join(SCRIPT_DIR, "contas_a_pagar.txt")
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "Nenhuma despesa registrada."
    
# registrar o prompt e nome do prompt(formatar_dado_cadastral)
@mcp.prompt()
def formatar_dado_cadastral(cpf: str) -> str:
    """Prompt para formatar dados cadastrais"""
    return f"Formate o CPF informado no padrão xxx.xxx.xxx-xx: {cpf}"



# executar server: mcp run app/01MCPServer/server.py