
class Cliente:
   def __init__(self,nome, cpf, telefone):
      self.__nome = nome
      self.__cpf = cpf
      self.__telefone = telefone
      self.__contas = []
      self.__chaves = []

   @property
   def get_nome(self):
      return self.__nome
      
   @get_nome.setter
   def set_nome(self, nome):
      self.__nome = nome
   
   @property
   def get_cpf(self):
      return self.__cpf
   
   @get_cpf.setter
   def set_cpf(self, cpf):
      self.__cpf = cpf
   
   @property
   def get_telefone(self):
      return self.__telefone
   
   @get_telefone.setter
   def set_telefone(self, telefone):
      self.__telefone = telefone
   
   #composição Conta
   def insereConta(self,numConta, agencia, saldo):
      self.__contas.append(Conta(numConta, agencia, saldo))
   
   def listaContas(self):
      for conta in self.__contas:
         print(f'Agencia: {conta.agencia}, Conta: {conta.numConta}, Saldo: {conta.saldo}')
   
   def ver_saldo(self):
      for conta in self.__contas:
         print(f'{self.__nome}, seu saldo é de R${conta.saldo}')

   def depositar(self, valor):
      for conta in self.__contas:
         conta.saldo += valor

   def transferir(self, valor, contaDestino):
      for conta in self.__contas:
         conta.saldo -= valor
         contaDestino.depositar(valor)
   
   #Composição Chave
   def insereChave(self, chave_pix):
      self.__chaves.append(ChavePix(chave_pix))
   
   def listaChaves(self):
      for chave in self.__chaves:
         print(f'Chave Pix{chave.chave_pix}')

   def __del__(self):
      print(f'{self.__nome} foi apagado')

         
class Conta:
   def __init__(self,numConta, agencia, saldo):
      self.__numConta = numConta
      self.__agencia = agencia
      self.__saldo = saldo
      
   @property
   def get_numConta(self):
      return self.__numConta
   
   @get_numConta.setter
   def set_numconta(self, numconta):
      self.__numConta = numconta
   
   @property
   def get_agencia(self):
      return self.__agencia
   
   @get_agencia.setter
   def set_agencia(self, agencia):
      self.__agencia = agencia
   
   @property
   def get_saldo(self):
      return self.__saldo
   
   @get_saldo.setter
   def set_saldo(self, saldo):
      self.__saldo = saldo
   

class ChavePix:
   def __init__(self, chave_pix):
      self.__chave_pix = chave_pix
   
   @property
   def get_chave_pix(self,):
      return self.__chave_pix

   @get_chave_pix.setter
   def set_chave_pix(self, chave_pix):
      self.__chave_pix = chave_pix

c1 = Cliente('Daniela','38784-44','9389-33')
c1.insereConta('1345-38','3232',344)
c1.insereChave('lucas@gmail.com')
print(c1.nome)
c1.listaContas()
c1.listaChaves()
c1.ver_saldo()
c1.depositar(10)
c1.ver_saldo()

c2 = Cliente('Junior','9398-323','3232-33')
c2.insereConta('233-3','434',200)
c2.insereChave('junior@gmail.com')
print(c2.nome)
c2.listaContas()
c2.listaChaves()
c2.ver_saldo()
c2.depositar(10)
c2.ver_saldo()

valor = float(input('Valor a transferir: '))
c1.transferir(valor, c2)
c1.ver_saldo()
c2.ver_saldo()

