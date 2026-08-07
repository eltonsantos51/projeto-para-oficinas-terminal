
from datetime import datetime
class Produto:
    def __init__(self,nome, preco,quantidade):
        self.nome=nome
        self.preco=preco
        self.quantidade=quantidade
        
    def __repr__(self):
        return f'Nome:{self.nome}| Preço:{self.preco}|Quantidade:{self.quantidade}'
    
class Venda:
    def __init__(self, nome='', preco=0, quantidade=1, desconto=0):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.desconto = desconto
        self.valor_total=0
        self.data=datetime.now().strftime('%d/%m/%Y %H:%M:%S' )

    def calcular_valor_total(self):
        self.valor_total= self.preco * self.quantidade
        return self.valor_total - (self.valor_total * self.desconto / 100)

    def nota_vendas(self):
        resultado= f'Mercadoria: {self.nome}\n'
        resultado+=f'Preço:{self.preco}\n'
        resultado+=f'Desconto:{self.desconto}%\n'
        resultado+=f'Total:{self.calcular_valor_total()}\n'
        resultado+=f'Data/Hora:{self.data}'
        return resultado
    
def interface():
    print('-='*30)
    print(f'{"Sistema para Oficina":^50}')
    print('-='*30)
    conteudo= f'{"1-Para cadastrar Produtos":^50}\n'
    conteudo+=f'{"2-Para Area de venda":^50}\n'
    conteudo+=f'{"3-Para cadastrar Clientes":^50}\n'
    conteudo+=f'{"4-Para exibir estoque de produtos":^50}\n'
    conteudo+=f'{"5-Para exibir cadastro de clientes":^50}\n'
    conteudo+=f'{"6-Para exbir total de venda no dia":^50}\n'
    conteudo+=f'{"7-Para zerar os dados do Fechamento":^50}\n'
    conteudo+=f'{"0-Para encerrar":^50}'
    print(conteudo)
    print('-='*30)


class Cliente: 
    def __init__(self,nome='',cpf='',tel='',placa='',km=0,servico=''):
        self.nome= nome
        self.cpf=cpf
        self.telefone=tel
        self.placa=placa
        self.km=km
        self.servico=servico
        self.data=datetime.now().strftime('%d/%m/%Y')
        
    def __repr__(self):
        conteudo= f'Nome do Cliente: {self.nome} | CPF:{self.cpf} |{self.telefone}'
        conteudo +=f'| Placa do veiculo:{self.placa} | KM do veiculo:{self.km}'
        conteudo+=f'|Serviço:{self.servico} | Data:{self.data}'
        return conteudo



