class Cliente:
    def __init__(self, id: str, phone: int):
        self.id = id
        self.phone = phone

    def getId (self):
        return self.id
    
    def getPhone (self):
        return self.phone
    
    def __str__(self):
        return f'{self.id}:{self.phone}'

class Sala:
    def __init__(self, capacidade: int):
        self.assentos: list [Cliente | None] = []
        for _ in range(capacidade):
            self.assentos.append(None)

    def __procurarC(self, cliente: str):
        for cli in self.assentos[:]:
            if  cli != None and cli.getId() == cliente:
                print("fail: cliente ja esta no cinema")
                return True
        return False
    
    def __verificarA(self, assento: int):
        if len(self.assentos)<= assento :
            print("fail: cadeira nao existe")
            return True
        return False

    def reservar(self, cliente: Cliente, assento: int):
        if self.__verificarA(assento):
            return True
        if self.assentos[assento] != None:
            print('fail: cadeira ja esta ocupada')
            return
        self.__procurarC(cliente.getId())
        
        self.assentos[assento] = cliente

    def cancel(self, cliente: str):
        for i in range(len(self.assentos)):
            if self.assentos [i] != None and self.assentos [i].getId() == cliente:
                self.assentos[i] = None
                return True
        print("fail: cliente nao esta no cinema")
        return False

    
    def __str__(self):
        lista = [elem for elem in self.assentos]
        for _ in range(len(lista)):
            if lista[_] == None:
                lista[_] = "-"
        assentos = " ".join([str(elem) for elem in lista])
        if assentos:
            return f'[{assentos}]'
        else:
            return f'[]'

class main:
    sala = Sala(0)
    while True:
        line = input()
        print("$"+ line)
        args: list[str] = line.split()
        if args[0] == "end":
            break
        if args[0] == "init":
            capacidade = int(args[1])
            sala = Sala(capacidade)
        if args[0] == "show":
            print(sala)
        if args[0] == "reserve":
            id = args[1]
            phone = args[2]
            cliente = Cliente(id, phone)
            assento = int(args[3])
            sala.reservar(cliente, assento)
        if args[0] == "cancel":
            cliente = args[1]
            sala.cancel(cliente)

main()