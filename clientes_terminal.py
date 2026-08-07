from codigo_principal import Cliente
from banco_dados import banco,cursor
from time import sleep
from rich import print

def cadastrar_cliente()-> tuple:
    """ Cadastra um cliente coletando informações como nome, CPF, telefone,
placa do veículo, quilometragem e descrição do serviço. Ao final,
armazena os dados do cliente no banco de dados.

Returns:
    tuple: Dados do cliente cadastrado.
    """
    try:
        while True:
            print('-----Cadastrar Clientes-----')
            nome_cliente=str(input('Nome do Cliente:')).upper().strip()
            cpf=''
            while len(cpf)!=11:
                try:
                    cpf=str(input('Digite o CPF:')).replace('.','').replace('-','')
                    if len (cpf) !=11:
                        print('[red] ERRO! CPF invalido.[/]')
                    else:
                        cpf_formatado= f'{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}'
                except(KeyboardInterrupt):
                    raise KeyboardInterrupt
            telefone=''
            while len(telefone) != 11:
                try:
                    print('ex:(xx)xxxxx-xxxx')
                    telefone=str(input('Digite o numero do telefone: '))
                    telefone=telefone.strip().replace(' ','').replace('(','').replace(')','').replace('-','')
                    if len(telefone)!=11:
                        print('[red]ERRO! Telefone invalido.')
                    else:
                        telefone_formatado= f'({telefone[0:2]}) {telefone[2:7]}-{telefone[7:11]} '
                except (KeyboardInterrupt):
                    raise KeyboardInterrupt
            placa=''
            while len(placa)!=7:
                try:
                    placa=str(input('Placa do veiculo:')).upper().strip().replace(' ','').replace('-','')
                    if len(placa)!=7:
                        print('[red] ERRO! Placa invalida.[/]')
                except(KeyboardInterrupt):   
                    raise KeyboardInterrupt
                    
            km=int(input('Km do veiculo:'))
            servico=str(input('Serviço feito:'))
            cliente=Cliente(nome_cliente,cpf_formatado,telefone_formatado,placa,km,servico)
            cursor.execute(
                'INSERT INTO clientes VALUES(?,?,?,?,?,?,?)',
                (cliente.nome,
                  cliente.cpf,
                  cliente.telefone,
                  cliente.placa,
                  cliente.km,
                  cliente.servico,
                  cliente.data)
                )
            banco.commit()
            sleep(1)
            print(f'[green]{cliente.nome} cadastrado com sucesso[/]\n')
            sleep(2)

            print(cliente)

            conti=None
            while conti not in ("S","N"):
                resposta= str(input(' Deseja continuar Cadastrando clientes? [Sim/Não]')).upper().strip()
                if resposta:
                    conti= resposta[0]
                else:
                    conti=None
            if conti=='N':
                break
    except(ValueError):
        print('[red] Opção inválida[/]')
        
    except(KeyboardInterrupt):
        print('[yellow] Operação interrompida! exibir itens ja cadastrados[/]')