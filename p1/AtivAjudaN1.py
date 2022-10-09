cadastrolist = []
def cadastrar(cpf, nome, idade, telefone):
   cadastro = {'cpf': cpf, 'dados': [nome, idade, telefone]}
   return cadastro
op = 1
while op != 0:
   print('1 - Cadastrar')
   print('2 - Imprimir')
   print('0 - Sair')
   op = int(input('Informe opção: '))
   if op == 1:
      cpf = input('Informe CPF: ')
      nome = input('Indforme nome: ')
      idade = input('Informe idade: ')
      telefone = input('Informe telefone: ')
      cadastro = cadastrar(cpf,nome,idade, telefone)
      cadastrolist.append(cadastro)
   elif op == 2:
      for indice in cadastrolist:
            if indice['dados'][idade] < 18:
               print('cadastro removido')
               print(cadastrolist)
      print(cadastrolist)
