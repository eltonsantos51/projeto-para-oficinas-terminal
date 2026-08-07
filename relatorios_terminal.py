from banco_dados import banco,cursor
from rich.console import Console
from rich.table import Table
from time import sleep


def exibir_estoque()->None: 
    """Exibe todos os clientes cadastrados no banco de dados, apresentando
informações como nome, CPF, telefone, placa do veículo, quilometragem
e descrição do serviço.

Returns:
    None
    """
    console=Console()
    tabela_estoque= Table(title='Estoque completo')
    tabela_estoque.add_column('Nome da Pecça')
    tabela_estoque.add_column('Preço')
    tabela_estoque.add_column('Quantidade')       
    cursor.execute('SELECT * FROM produto  ')
    for estoque in cursor.fetchall():
        tabela_estoque.add_row(*(str(item)for item in estoque ))
    sleep(1)
    console.print(tabela_estoque)   
    sleep(2)        

def exibir_cadastro_cliente()->None:
    """Exibe todos os produtos cadastrados no estoque, mostrando informações
como nome, preço e quantidade disponível.

Returns:
    None
    """
    console=Console()
    tabela_cliente=Table(title="Cadastros de clientes")
    tabela_cliente.add_column('Nome do cliente')
    tabela_cliente.add_column('CPF do cliente')
    tabela_cliente.add_column('Telefone')
    tabela_cliente.add_column('Placa do veiculo')
    tabela_cliente.add_column('Km do veiculo')
    tabela_cliente.add_column('Serviço feito')
    tabela_cliente.add_column('Data')
    cursor.execute('SELECT * FROM clientes')
    for cad in cursor.fetchall():
        converter_dados=[]
        for iten in cad:
            converter_dados.append(str(iten))
        tabela_cliente.add_row(*converter_dados)
    sleep(1)
    console.print(tabela_cliente)
    sleep(2)

def exibir_fechamento_caixa()->None:
    """Exibe o relatório de fechamento de caixa, apresentando todas as vendas
registradas, incluindo informações dos produtos, quantidades, descontos
e valores das vendas.

Returns:
    None
    """
    console=Console()
    tabela_fechamento=Table(title='Fechamento de caixa')
    tabela_fechamento.add_column('Produto')
    tabela_fechamento.add_column('Preço')
    tabela_fechamento.add_column('Quantidade')
    tabela_fechamento.add_column('Data')
    tabela_fechamento.add_column('Total')
    cursor.execute('SELECT * FROM fechamento_caixa')
    for caixa in  cursor.fetchall():
        conversor_caixa=[]
        for item in caixa:
            conversor_caixa.append(str(item))
        tabela_fechamento.add_row(*conversor_caixa)
    sleep(1)
    console.print(tabela_fechamento)
    sleep(2)