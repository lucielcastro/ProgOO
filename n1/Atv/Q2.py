agenda = []
menorIdade = []

def cadastrar(cpf, nome, idade):
    cadastro = {'cpf': cpf, 'nome': nome, 'idade': idade}
    return cadastro

def removerMenorIdade():
    for busca in agenda:
        if busca['idade'] < 18:
            print('Pessoa com menos de 18 anos')
            menorIdade.append(busca)
            print('Pessoa transferida para a agenda de menores de 18 anos')
            agenda.remove(busca)

op = None
while (op != 0):
   print('1- Cadastrar\n0-Sair')
   op = int(input('Informe uma opção: '))
   
   if op == 1:
        cpf = input('CPF: ')
        nome = input('Nome: ')
        idade = int(input('Idade: '))
        cadastro = cadastrar(cpf, nome, idade)
        agenda.append(cadastro)
        print(f'Agenda: {agenda}')
        print(f'Agenda menor idade{menorIdade}')
        removerMenorIdade()
        print(f'Agenda: {agenda}')
        print(f'Agenda menor idade{menorIdade}')