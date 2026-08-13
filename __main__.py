from codigo_principal import interface
from rich import print
from produtos_terminal import cadastrar_produto
from vendas_terminal import realizar_venda
from clientes_terminal import cadastrar_cliente
from banco_dados import criar_tabela, fechar_banco, zera_fechamento
from relatorios_terminal import exibir_estoque, exibir_cadastro_cliente, exibir_fechamento_caixa

def main():  
    
    while True:
        opc=None
        interface()
        try:
            opc=int(input('Qual operação deseja realizar? '))
            print(f'\n')
        except (ValueError):
            print(f'[red] Opção invalida[/]')
            continue
        except(KeyboardInterrupt):
            print('[yellow]Programa enceraado pelo usuario[/]')
            fechar_banco()
            break
        if opc == 1: 
            cadastrar_produto()
           
        elif opc ==2: 
            realizar_venda()
            
        elif opc ==3:
            cadastrar_cliente()
           
        elif opc==4:
           exibir_estoque()

        elif opc ==5:
            exibir_cadastro_cliente()

        elif opc ==6:
            exibir_fechamento_caixa()

        elif opc==7:
            zera_fechamento() 

        elif opc==0:
            print('[blue] Programa encerrado, volte sempre![/]')
            fechar_banco()
            break
        else:
            print('[red] ERRO! Por favor digite opções validas.[/] ')
    print(f'\n')  
if __name__=='__main__':
    criar_tabela()
    main()




 