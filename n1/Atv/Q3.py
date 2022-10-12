
dicionarioPrincipal = []
dicionarioBackup = []

def cadastrar(cpf, nome, idade, sexo, peso):
	cadastro = {'cpf': cpf, 'nome':nome, 'idade':idade,'sexo':sexo, 'peso':peso}
	return cadastro
op = None
while(op != 0):
   print('1-Cadastrar\n0-Sair')
   op = int(input('Informe um opçao: '))
   
   if op == 1:
      cpf = input('CPF: ')
      nome = input('Nome: ')
      idade = int(input('Idade: '))
      sexo = input('Sexo: ')
      peso = float(input('Peso: '))
      dicionarioPrincipal.append(cadastrar(cpf, nome, idade, sexo, peso))
      
      if len(dicionarioPrincipal) == 5:
         copia = dicionarioPrincipal.copy()
         dicionarioBackup.append(copia)
         dicionarioPrincipal.clear()
      print('Dicionário Principal: ', dicionarioPrincipal)
      print('Dicionário Backup: ', dicionarioBackup)