
class Cliente:
   def __init__(self,nome:str, cpf, telefone):
      self.__nome = nome
      self.__cpf = cpf
      self.__telefone = telefone
      self.contas = None

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
      self.contas=(Conta(numConta, agencia, saldo))
   
   def imprimir_dados_pessoas(self):
      print(f'\nNome: {self.__nome} CPF: {self.__cpf}, Telefone: {self.__telefone}')
   
   def imprimir_dados_conta(self):
         print(f'Conta: {self.contas.numConta}, Agencia: {self.contas.agencia}')

   
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
         contaDestino.depositar(valor)
         
         print('Transferência realizado com sucesso!')

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
cliente1.criar_conta('1345-38','3232',344)
cliente1.contas.criar_chave_pix('lucas@gmail.com')

cliente1.imprimir_dados_pessoas()
cliente1.imprimir_dados_conta()
cliente1.contas.listaChaves()
cliente1.contas.ver_saldo()
cliente1.contas.depositar(10)
cliente1.contas.ver_saldo()


cliente2 = Cliente('Luciel','12784-44','0089-33')
cliente2.criar_conta('4434-38','656',100)
cliente2.contas.criar_chave_pix('luciel@gmail.com')

cliente2.imprimir_dados_pessoas()
cliente2.imprimir_dados_conta()
cliente2.contas.listaChaves()
cliente2.contas.ver_saldo()
cliente2.contas.depositar(60)
cliente2.contas.ver_saldo()


#valor = float(input('\nValor a transferir: '))
cliente1.contas.transferir(40, cliente2.contas)
cliente1.contas.ver_saldo()
cliente2.contas.ver_saldo()

