from codigo_principal import Venda
from time import sleep
from banco_dados import banco,cursor
from rich import print

def realizar_venda ():
    """Realiza uma venda coletando as informações do produto, como nome, preço,
    quantidade e desconto (em porcentagem). Calcula o valor final da venda,
    registra a operação no banco de dados (fechamento de caixa) e retorna
    os dados da venda.

    
    """
    print('-----Venda de mercadoria-----')
    preco_venda=desconto=0
    quantidade_venda=1
    venda=None
    try: 
        nome_produto= str(input('Nome do produto:')).upper().strip()
        preco_venda= float(input('Preço:'))
        quantidade_venda=int(input('Quantidade:'))
        desconto=float(input('Desconto: '))
        
        venda=Venda(nome_produto,preco_venda,quantidade_venda,desconto)
        total_pagar=venda.calcular_valor_total()
        cursor.execute('SELECT Quantidade FROM produto WHERE Nome =?',(venda.nome,))
        resultado= cursor.fetchone()
        
        if resultado is None:
            print('[red]Produto não cadastrado![/]')
            return
        estoque= resultado[0]
        if estoque >= venda.quantidade:
            novo_estoque= estoque - venda.quantidade
            cursor.execute(
                'UPDATE produto SET Quantidade = ? WHERE Nome= ?',
                (novo_estoque,venda.nome)
                )
            print('\n [green]Venda aprovada[/]')
            cursor.execute(
                'INSERT INTO fechamento_caixa VALUES (?,?,?,?,?)',
                (venda.nome,venda.preco,venda.quantidade,venda.data,total_pagar)
                )        
            banco.commit()
            sleep(1)
            print(venda.nota_vendas())
            sleep(2)
            print(f'\n')
        else:
            print('estoque insuficiente')  
       
    except(ValueError):
        print('[red] opção inválida[/]')
        
    except(KeyboardInterrupt):
        print('[yellow] Venda cancelada pelo usuario[/]')
                    
