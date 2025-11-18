class Pessoa:
    def __init__(self, nome: str ):
        self.nome = nome
    def __str__(self):
        return self.nome

class Budega:
    def __init__(self, numCaixas: int):
        self.caixas: list[Pessoa | None] = []
        for _ in range(numCaixas):
            self.caixas.append(None)
        self.espera: list[Pessoa] = []


    def arrive(self, pessoa: Pessoa):
        self.espera.append(pessoa)

    def call (self, num: int):
        if num >= len(self.caixas):
            print("fail: caixa inexistente")
            return
        if len(self.espera) == 0:
            print("fail: sem clientes")
            return
        if self.caixas[num] == None:
            self.caixas[num] = self.espera[0]
            del self.espera[0]
            return
        
        else:
            print("fail: caixa ocupado")
            return

    def finish(self, num: int):
        if num >= len(self.caixas):
            print("fail: caixa inexistente")
            return
        
        if self.caixas[num] == None:
            print("fail: caixa vazio")
            return

        else:
            self.caixas[num] = None
            return

    def __str__(self):
        lista = [elem for elem in self.caixas]
        for _ in range(len(lista)):
            if lista[_] == None:
                lista[_] = "-----"
        caixas = ", ".join([str(elem) for elem in lista])
        espera = ", ".join([str(elem) for elem in self.espera])
        return f"Caixas: [{caixas}]\nEspera: [{espera}]"
    
class main:
    pessoa = Pessoa("Maria")
    budega = Budega(0)
    while True:
        line = input()
        print("$"+ line)
        args: list[str] = line.split()
        if args[0] == "end":
            break
        if args[0] == "init":
            budega = Budega(int(args[1]))
        if args[0] == "show":
            print (budega)
        if args[0] == "arrive":
            budega.arrive(Pessoa(args[1]))
        if args[0] == "call":
            fila = int(int(args[1]))
            budega.call(fila)
        if args[0] == "finish":
            pess = int(args[1])
            budega.finish(pess)
        

main()