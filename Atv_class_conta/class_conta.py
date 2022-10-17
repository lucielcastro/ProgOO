class Conta:
    def __init__(self, numConta, agencia, titular, saldo):
        self.conta = numConta
        self.agencia = agencia
        self.titular = titular
        self.saldo = saldo

    def ver_saldo(self):
        print(self.titular,', seu saldo é de R$',self.saldo)

    def depositar(self, valor):
        self.saldo += valor

    def transferir(self, valor, contaDestino):
        self.saldo -= valor
        contaDestino.depositar(valor)
c1 = Conta(numConta= '123-33', agencia='12-5', titular='Victor Pereira', saldo = 1500)
c2 = Conta(numConta='233-66', agencia='12-5', titular='João Carlos', saldo = 2500)
c1.ver_saldo()
c2.ver_saldo()
c1.transferir(300, c2)
c1.ver_saldo()
c2.ver_saldo()
#c2.transferir(800, c1)
#c2.ver_saldo()