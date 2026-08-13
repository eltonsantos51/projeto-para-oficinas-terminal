import sqlite3

banco=sqlite3.connect('oficina.db')#objeto da conexão com banco 
cursor=banco.cursor()

def criar_tabela()->None:
    """Cria as tabelas necessárias no banco de dados caso elas ainda não existam.
        As tabelas criadas são: produto, clientes e fechamento_caixa, cada uma
        com suas respectivas colunas e estruturas de dados.
    """
    
    cursor.execute('CREATE TABLE IF NOT EXISTS produto'
            '(Nome text, Preço REAL, Quantidade integer)')

    cursor.execute('CREATE TABLE IF NOT EXISTS clientes'
            '(Nome text, CPF text,Telefone text, Placa text,' 
            ' Km integer,Serviço text, Data text)')

    cursor.execute('CREATE TABLE IF NOT EXISTS fechamento_caixa'
              '(Produto text, Preco REAL, Quantidade integer, Data text, Total REAL  )')

    banco.commit()

def fechar_banco()->None:
    """ Fecha a conexão com o banco de dados.
    Returns: None
    """
    banco.close()

def zera_fechamento()->None:
        """
    Remove todos os registros do fechamento de caixa,
    mantendo a estrutura da tabela.

    Returns:
        None
    """
        cursor.execute('DELETE from fechamento_caixa')
        banco.commit()
