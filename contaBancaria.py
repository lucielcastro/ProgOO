
from ast import Num
from operator import contains
from os import remove

contasList = []

def cadastrar(titular, numero, senha, saldo):
   conta = {'titular': titular, 'numero':numero, 'senha':senha, 'saldo':saldo}
   return conta
op = 1
while op != 0:
   print('1 - Cadastrar conta')
   print('2 - Encontrar na conta')
   print('0 - Sair')
   op = int(input('Informe opção: '))

   if op == 1:
      titular = input('Nome do titular: ')
      numero = input('Numero da conta: ')
      senha = input('Senha: ')
      saldo = int(input('Saldo: '))
      contaCadastrada = cadastrar(titular,numero,senha, saldo)
      contasList.append(contaCadastrada)

   elif op == 2:
      def encontrar(num, senha):
         for contaIndice in contasList:
            if contaIndice['numero'] == num and contaIndice['senha'] == senha:
               exibirNome = contaIndice['titular']
               print(f'Olá, {exibirNome}!')
               return contaIndice
            elif contaIndice['numero'] !=num or contaIndice['senha'] != senha:
               print('Conta não encontrada ou senha inválida')
               num = input('Informar numero novamente: ')
      def encontrarContaTransferir(num):
         for contaIndice in contasList:
            if contaIndice['numero'] == num:
               return contaIndice
            elif contaIndice['numero'] !=num or contaIndice['senha'] != senha:
               print('Conta não encontrada ou senha inválida')
               num = input('informe')
      def remover(n, s):
         for i in contasList:
            if i['numero'] == n and i['senha'] == s:
               contasList.remove(i)
               #print(contas)
               return contasList
      def depositar(contaD):
         valor = float(input('Informe valor: '))
         if valor<=0:
            print('Valor inválido!')
         else:
            contaD['saldo'] += valor
            print('Operação realizada com sucesso!')
         return contaD
      def exibirSaldo(contaOne):
         saldo = contaOne['saldo']
         return saldo
      num = input('Inoforme numero da conta: ')
      passw = input('Inoforme senha: ')
      cont1 = encontrar(num, passw)
      #print(f'{encontrar(num, passw)}')
      op2 = 1
      while op2 != 0:
         print('1 - Remover conta')
         print('2 - Realizar Transferencia')
         print('3 - Exibir Valor')
         print('4 - Depositar')
         print('0 - Sair')
         op2 = int(input('Informe opção: '))
         if op2 == 1:
            num = input('Inoforme numero da conta: ')
            passw = input('Inoforme senha: ')
            print(f'{remover(num, passw)}')
         elif op2 == 2:
            def transferencia(conta1, conta2):
               if conta1['numero'] == conta2['numero']:
                  print('Operação inválida')
               else:
                  valor = float(input('Informe valor: '))
                  if valor <= conta1['saldo']:
                     conta1['saldo'] -= valor
                     conta2['saldo'] += valor
                     return cont1, cont2
                  else:
                     print('Saldo insuficiente!')
               print('Saldo insuficiente ou operação inválida')
            num = input('Inoforme numero da conta para transferencia: ')
            cont2 = encontrarContaTransferir(num)
            print(f'{transferencia(cont1, cont2)}')
            print('Operação realizada!')
         elif op2 == 3:
            contaExibir = cont1['numero']
            print(f'Saldo na conta {contaExibir} é de R$ {exibirSaldo(cont1)}')
         elif op2 == 4:
            namber = input('Inoforme numero da conta para Depósito: ')
            contaDeposito = encontrarContaTransferir(namber)
            depositar(contaDeposito)
   #elif op == 3:
      #print(f'Contas: {contas}')
   elif op == 0:
      print(f'OPERAÇÃO ENCERRADA!')



      



