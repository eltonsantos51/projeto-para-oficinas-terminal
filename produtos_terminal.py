from codigo_principal import Produto
from banco_dados import banco,cursor
from time import sleep
from rich import print
def cadastrar_produto()-> tuple: 
    """Cadastra produtos coletando informações como nome, preço e quantidade.
Caso o produto já exista no estoque, sua quantidade é atualizada somando
a nova quantidade informada à existente.

Returns:
    tuple: Dados do produto cadastrado.

    """
    try:
        while True:
            print('-----Cadastrar Produto-----')
            nome_produto= str(input('Nome do produto:')).upper().strip()
            preco_produto= float(input('Preço:'))
            quantidade_produto=int(input('Quantidade:'))
            produto=Produto(nome_produto,preco_produto,quantidade_produto)
            cursor.execute('SELECT Nome FROM produto WHERE Nome =?',(produto.nome,))
            resultado_nome= cursor.fetchone()
            if  resultado_nome is None:
                cursor.execute(
                    'INSERT INTO produto VALUES (?,?,?)',
                    (produto.nome,produto.preco,produto.quantidade))
                sleep(1)
                print(f'[green]{produto.nome} Cadastrado com sucesso[/]')
                sleep(2) 
            else:
                cursor.execute('SELECT Quantidade FROM produto WHERE Nome=?',(produto.nome,))
                soma_estoque=cursor.fetchone()
                atualizar_estoque= produto.quantidade + soma_estoque[0]
                cursor.execute(
                    'UPDATE produto SET Quantidade =? WHERE Nome=?',
                    (atualizar_estoque,produto.nome))
            
                sleep(1)
                print(f'[green]{produto.nome} Atualizado com sucesso[/]')
                sleep(2) 
            banco.commit()

            deseja=None
            while deseja not in ("S","N"):
                resposta=input('deseja continuar cadastrando?[Sim/Não]').upper().strip()
                if resposta:
                    deseja= resposta[0]
                else:
                    deseja=None
            if deseja =='N':
                break
    except(ValueError):
        print('[red]Opção invalida[/]')
    except(KeyboardInterrupt):
        print('[yellow] Operação interrompida! exibir itens ja cadastrados[/]')              
