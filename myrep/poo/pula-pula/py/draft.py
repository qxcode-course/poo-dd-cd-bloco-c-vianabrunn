class Kid:
    def __init__(self, name: str, age: int):
        self.age = age
        self.name = name

    def getAge(self):
        return self.age
    
    def getName(self):
        return self.name
    
    def __str__(self):
        return f'{self.name}:{self.age}'

class Trampoline:
    def __init__(self):
        self.playing: list[Kid] = []
        self.waiting: list[Kid] = []

    def remove(self, nome: str):
        kid_encontrado = None
        for kid in self.waiting[:]:
            if kid.name == nome:
                kid_encontrado = kid
                self.waiting.remove(kid)
                return
        for kid in self.playing[:]:
            if kid.name == nome:
                kid_encontrado = kid
                self.playing.remove(kid)
                return
        
        if kid_encontrado == None:
                    print(f"fail: {nome} nao esta no pula-pula")
        
        

    def leave(self):
        if len(self.playing) == 0:
            return
        else:
            kid = self.playing[-1]
            self.waiting.insert(0, kid)
            self.playing.remove(kid)
        

    def enter(self):
        if len(self.waiting) == 1:
            kid = self.waiting[0]
            self.playing.append(kid)
            self.waiting.remove(kid)
            self.playing.sort(key= lambda k: k.age)
        else:
            kid = self.waiting[-1]
            self.playing.append(kid)
            self.waiting.remove(kid)
            self.playing.sort(key= lambda k: k.age)

    def arrive(self, kid: Kid):
        self.waiting.append(kid)
        self.waiting.sort(key= lambda k: k.age)

    def __str__(self):
        waiting = ", ".join([str(elem) for elem in self.waiting])
        playing = ", ".join([str(elem) for elem in self.playing])
        return f'[{waiting}] => [{playing}]'
    
    
class main:
    kid = Kid("",0)
    trampoline = Trampoline()
    while True:
        line = input()
        print("$"+ line)
        args: list[str] = line.split()
        if args[0] == "end":
            break  
        if args[0] == "show":
            print (trampoline)
        if args[0] == "arrive":
            name = args[1]
            age = int(args[2])
            kid = Kid(name, age)
            trampoline.arrive(kid)
        if args[0] == "enter":
            trampoline.enter()
        if args[0] == "leave":
            trampoline.leave()
        if args[0] == "remove":
            nome = args[1]
            trampoline.remove(nome)


main()

