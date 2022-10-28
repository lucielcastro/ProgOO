
class Cliente:
   def __init__(self,nome, cpf, telefone):
      self.__nome = nome
      self.__cpf = cpf
      self.__telefone = telefone
      self.__contas = []

   @property
   def nome(self):
      return self.__nome
      
   @nome.setter
   def nome(self, nome):
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
   
   def insereConta(self,numConta, agencia, saldo):
      self.__contas.append(Conta(numConta, agencia, saldo))
   
   def listaContas(self):
      for conta in self.__contas:
         print(f'Agencia: {conta.agencia}, Conta: {conta.numConta}, Saldo: {conta.saldo}')

         
class Conta:
   def __init__(self,numConta, agencia, saldo):
      self.__numConta = numConta
      self.__agencia = agencia
      self.__saldo = saldo
      
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

c1 = Cliente('Nome','38784-44','9389-323')
c1.insereConta('1345-38','3232',344)
c1.listaContas()
