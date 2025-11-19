class Grafite:
    def __init__(self, calibreG: float, dureza: str, size: int, ):
        self.calibreG = calibreG
        self.dureza = dureza
        self.size = size

    def get_size(self):
        return self.size

    def get_calibreG(self):
        return self.calibreG 

    def get_dureza(self):
        return self.dureza

    def set_size (self, valor: int):
        self.size = valor

    def usoPorFolha(self):
        if self.dureza == "HB":
            return 1
        
        if self.dureza == "2B":
            return 2
        
        if self.dureza == "4B":
            return 4

        if self.dureza == "6B":
            return 6
        
    def __str__(self):
        return f'[{self.calibreG}:{self.dureza}:{self.size}]'


class Pencil:
    def __init__(self, calibre: float, bico: Grafite | None, tambor: Grafite | None):
        self.calibre = calibre
        self.bico: list[Grafite | None] = []
        self.tambor: list[Grafite | None] = []

    def get_calibre(self):
        return self.calibre
    
    def insert (self, grafite: Grafite):
        if self.calibre == grafite.get_calibreG():
            self.tambor.append(grafite)

        else: 
            print("fail: calibre incompatível")


    def remove (self):
        self.bico = [] 

    def pull(self):
        if len(self.bico) != 0:
            print("fail: ja existe grafite no bico")
            return
        else:
            ponta = self.tambor[0]
            self.bico.append(ponta)
            self.tambor.remove(ponta)

    def write (self):
        if self.bico == []:
            print("fail: nao existe grafite no bico")
            return
        elif self.bico[0].get_size() - 10 >= self.bico[0].usoPorFolha():
            self.bico[0].set_size(self.bico[0].get_size() - self.bico[0].usoPorFolha())
            return
        
        elif self.bico[0].get_size() - 10 != 0 and self.bico[0].get_size() - 10 != self.bico[0].usoPorFolha():
            print("fail: folha incompleta")
            self.bico[0].set_size(10)
            return
        
        else:
            print("fail: tamanho insuficiente")
            return

        
    def __str__(self):
            tambor = "".join([str(elem) for elem in self.tambor])
            bico = "".join([str(elem) for elem in self.bico])
            if self.tambor  and self.bico :
                return f'calibre: {self.calibre}, bico: {bico}, tambor: <{tambor}>'
            elif self.tambor  and not self.bico:
                return f'calibre: {self.calibre}, bico: [], tambor: <{tambor}>'
            elif not self.tambor and self.bico  :
                return f'calibre: {self.calibre}, bico: {bico}, tambor: <>'
            else:
                return f'calibre: {self.calibre}, bico: [], tambor: <>'

class main:
    pencil = Pencil(0.0, None, None)
    grafite = Grafite(0.0, " ", 0)
    while True:
        line = input()
        print("$"+ line)
        args: list[str] = line.split()
        if args[0] == "end":
            break
        if args[0] == "init":
            calibre = float(args[1])
            pencil = Pencil(calibre, None, None)
        if args[0] == "show":
            print(pencil)
        if args[0] == "insert":
            calibre = float(args[1])
            dureza = args[2]
            size = int(args[3]) 
            grafite = Grafite(calibre, dureza, size)
            pencil.insert(grafite)
        if args[0] == "remove":
            pencil.remove()
        if args[0] == "write":
            pencil.write()
        if args[0] == "pull":
            pencil.pull()



main()