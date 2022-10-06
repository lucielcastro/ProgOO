from multiprocessing.sharedctypes import Value
from unicodedata import name


listaCadastro = []
telefones = []
def cadastrarFuncionaro(nome, cpf, cargo, salario, telefone):
   cadastro = {'nome': nome, 'cpf':cpf, 'cargo':cargo, 'salario':salario, 'telefones':telefone}
   print('Funcionario cadastrado com sucesso! ')
   return cadastro

op = 1
while op != 0:
   print('1 - Cadastro de Funcionários\n2 - Pesquisar funcionário\n3 - Cadastrar novo telefone\n4 - Editar dados do Funcionário\n5 - Deletar funcionário\n0 - Sair')
   op = int(input('Informe opção: '))
   if op == 1:
      nome = input('Nome do funcionário: ')
      cpf = input('CPF: ')
      telefone = input('Telefones: ')
      telefones.append(telefone)
      cargo = input('Cargo: ')
      salario = float(input('Salario: '))
      funcionárioCadastrado = cadastrarFuncionaro(nome,cpf,cargo, salario,telefones)
      listaCadastro.append(funcionárioCadastrado)

   elif op == 2:
      def encontrarFuncionario(cpfencontrar):
         for indice in listaCadastro:
            if indice['cpf'] == cpfencontrar:
               print('funiconario encontrado na base de dados')
               print(indice)
               return indice
         print('Funiconario não cadastrado')
         cpfencontrar = input('Informar Cpf novamente: ')
         encontrarFuncionario(cpfencontrar)
         print(indice)
         return indice
      cpfbusca = input('Inoforme CPF do funcionario: ')
      cadastroBuscado = encontrarFuncionario(cpfbusca)

   elif op == 3:
      def encontrarFunCadastroTel(cpfencontrar):
         for indice in listaCadastro:
            if indice['cpf'] == cpfencontrar:
               print('funiconario encontrado na base de dados')
               telefone = input('Informe novo numero telefone:')
               indice['telefones'].append(telefone)
               print(indice)
               return indice
            elif indice['cpf'] != cpfencontrar:
               while indice['cpf'] != cpfencontrar:
                  print('Funiconario não cadastrado')
                  cpfencontrar = input('Informar Cpf novamente: ')
               print('funiconario encontrado na base de dados')
               telefone = input('Informe novo numero telefone:')
               indice['telefones'].append(telefone)
               print(indice)
               return indice
      cpfBuscaTelefone = input('Inoforme CPF do funcionario para cadastro de novo televone: ')
      cadastroBuscado = encontrarFunCadastroTel(cpfBuscaTelefone)

   elif op == 4:
      def editarCadastro(key):
         print('1 - Editar nome\n2 - Editar CPF\n3 - Editar cargo\n4 - Editar Salario\n5 - Editar telefofe')
         op2 = int(input('Escolha uma opção:'))
         if op2 == 1:
            key['nome'] = input('Informe nome')
            print(listaCadastro)
            return key
         elif op2 == 2:
            key['cpf'] = input('Informe cpf')
            print(listaCadastro)
            return key
         elif op2 == 3:
            key['cargo'] = input('Informe cargo')
            print(listaCadastro)
            return key
         elif op2 == 4:
            key['salario'] = input('Informe salario')
            print(listaCadastro)
            return key
         elif op2 == 5:
            key['telefones'] = input('Informe telefone')
            print(listaCadastro)
            return key
      cpfEditar2 = input('Inoforme CPF do funcionario para editar dados: ')
      editar = encontrarFuncionario(cpfEditar2)
      editarCadastro(editar)
   if op == 5:
      def removerFuncionário(cpfBusca):
         for i in listaCadastro:
            if i['cpf'] == cpfBusca:
               listaCadastro.remove(i)
               print('Funcionario excluido da base de dados')
               print(listaCadastro)
               return listaCadastro
      cpfExcluir = input('Inoforme CPF do funcionario para excluir dados: ')
      cadastroBuscado = removerFuncionário(cpfExcluir)
      
