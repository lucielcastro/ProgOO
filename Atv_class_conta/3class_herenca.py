
class Cliente:
   def __init__(self,nome:str, cpf, telefone):
      self.__nome = nome
      self.__cpf = cpf
      self.__telefone = telefone
      self.conta = None
      self.conta_cc = None
      self.conta_cp = None

   @property
   def nome_(self):
      return self.__nome
      
   @nome_.setter
   def nome_(self, nome):
      self.__nome = nome
   
   @property
   def cpf(self):
      return self.__cpf
   
   @cpf.setter
   def cpf(self, cpf):
      self.__cpf = cpf
   
   @property
   def telefone(self):
      return self.__telefone
   
   @telefone.setter
   def telefone(self, telefone):
      self.__telefone = telefone
   
   #composição Conta
   def criar_conta(self,numConta, agencia, saldo):
      self.conta=(Conta(numConta, agencia, saldo))

   def criar_conta_cc(self,numConta_, agencia_, saldo_):
      self.conta_cc=(ContaCorrente(numConta_, agencia_, saldo_))
   
   def criar_conta_cp(self,numConta_p, agencia_p, saldo_p):
      self.conta_cp=(ContaPoupanca(numConta_p, agencia_p, saldo_p))
   
   def imprimir_dados_pessoas(self):
      print(f'\nNome: {self.__nome} CPF: {self.__cpf}, Telefone: {self.__telefone}')
   
   def imprimir_dados_conta(self):
         print(f'Conta: {self.conta.numConta}, Agencia: {self.conta.agencia}')
   
   def imprimir_dados_conta_c(self):
         print(f'Conta: {self.conta_cc.numConta_}, Agencia: {self.conta_cc.agencia_}')

   def imprimir_dados_conta_p(self):
         print(f'Conta: {self.conta_cp.numConta}_p, Agencia: {self.conta_cp.agencia_p}')

   
class Conta:
   def __init__(self,numConta, agencia, saldo):
      self.__numConta = numConta
      self.__agencia = agencia
      self.__saldo = saldo
      self.chaves = []
    
   @property
   def numConta(self):
      return self.__numConta
   
   @numConta.setter
   def numconta(self, numconta):
      self.__numConta = numconta
   
   @property
   def agencia(self):
      return self.__agencia
   
   @agencia.setter
   def agencia(self, agencia):
      self.__agencia = agencia
   
   @property
   def saldo(self):
      return self.__saldo
   
   @saldo.setter
   def saldo(self, saldo):
      self.__saldo = saldo
   
   def criar_chave_pix(self, chave_pix):
      self.chaves.append(ChavePix(chave_pix))
   
   def listaChaves(self):
      for chave in self.chaves:
         print(f'Chave Pix: {chave.chave_pix}')
   
   def ver_saldo(self):
      #for conta in self.contas:
         print(f'Seu saldo é de R$ {self.__saldo}')
   
   def depositar(self, valor):
      self.__saldo += valor
      print('Deposito realizado com sucesso!')
   

   def transferir(self, valor, contaDestino):
      self.__saldo -= valor
      self.__saldo -= valor * .1
      contaDestino.depositar(valor)
      print('Transferência realizado com sucesso!')

class ContaCorrente(Conta):
   def __init__(self, numConta, agencia, saldo):
      super().__init__(numConta, agencia, saldo)
   def transferir(self, valor, contaDestino):
      taxa = .1
      self.saldo -= valor
      self.saldo -= valor * taxa * 5
      contaDestino.depositar(valor)
      print('Transferência realizado com sucesso!')
      super().ver_saldo()
      


class ContaPoupanca(Conta):
   def __init__(self, numConta, agencia, saldo):
      super().__init__(numConta, agencia, saldo)
   def transferir(self, valor, contaDestino):
      taxa = .1
      self.saldo -= valor
      self.saldo -= valor * taxa * 1.25
      contaDestino.depositar(valor)
      print('\n\nTransferência realizado com sucesso!')
      super().ver_saldo()
   
class ChavePix:
   def __init__(self, chave_pix):
      self.__chave_pix = chave_pix
   
   @property
   def chave_pix(self):
      return self.__chave_pix

   @chave_pix.setter
   def set_chave_pix(self, chave_pix):
      self.__chave_pix = chave_pix

cliente1 = Cliente('Daniela','38784-44','9389-33')
cliente1.criar_conta('1345-38','3232',900)
cliente1.conta.criar_chave_pix('lucas@gmail.com')
cliente1.imprimir_dados_pessoas()
cliente1.imprimir_dados_conta()
cliente1.conta.listaChaves()
cliente1.conta.ver_saldo()
cliente1.conta.depositar(100)
cliente1.conta.ver_saldo()


cliente2 = Cliente('Luciel','12784-44','0089-33')
cliente2.criar_conta('4434-38','656',800)
cliente2.conta.criar_chave_pix('luciel@gmail.com')

cliente2.imprimir_dados_pessoas()
cliente2.imprimir_dados_conta()
cliente2.conta.listaChaves()
cliente2.conta.ver_saldo()
cliente2.conta.depositar(200)
cliente2.conta.ver_saldo()


#valor = float(input('\nValor a transferir: '))
cliente1.conta.transferir(40, cliente2.conta)
cliente1.conta.ver_saldo()
cliente2.conta.ver_saldo()


cliente3 = Cliente('Carlos','38784-44','9389-33')
cliente3.criar_conta_cc('1345-38','3232',900)
#cliente3.conta.criar_chave_pix('lucas@gmail.com')
cliente3.imprimir_dados_pessoas()
#cliente3.imprimir_dados_conta_c()
#cliente3.conta.listaChaves()
cliente3.conta_cc.ver_saldo()
cliente3.conta_cc.depositar(100)
cliente3.conta_cc.ver_saldo()


cliente4 = Cliente('Lucas','12784-44','0089-33')
cliente4.criar_conta_cc('4434-38','656',800)
#cliente4.conta_cc.criar_chave_pix('luciel@gmail.com')

cliente4.imprimir_dados_pessoas()
#cliente4.imprimir_dados_conta_c()
#cliente4.conta_cc.listaChaves()
cliente4.conta_cc.ver_saldo()
cliente4.conta_cc.depositar(200)
cliente4.conta_cc.ver_saldo()


#valor = float(input('\nValor a transferir: '))
cliente3.conta_cc.transferir(30, cliente4.conta_cc)
cliente3.conta_cc.ver_saldo()
cliente4.conta_cc.ver_saldo()




