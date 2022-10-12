from multiprocessing import Value


cadastrolist = []
def cadastrar(cpf, nome, idade, telefone):
   cadastro = { cpf : {'nome':nome,'idade':idade,'telefone':telefone}}
   return cadastro
op = 1
while op != 0:
   print('1 - Cadastrar')
   print('0 - Sair')
   op = int(input('Informe opção: '))
   if op == 1:
      cpf = input('Informe CPF: ')
      nome = input('Indforme nome: ')
      idade = input('Informe idade: ')
      telefone = input('Informe telefone: ')
      cadastro = cadastrar(cpf,nome,idade, telefone)
      cadastrolist.append(cadastro)
   print(f'{cadastrolist}')
