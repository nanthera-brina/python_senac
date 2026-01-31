import random

class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
    
    def atacar(self):
        return random.randint(1, 25)
    
    def ataque_critico(self):
        return random.randint(25, 50)
    
    def sofrer_dano(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0
        print(f"{self.nome} sofre {dano} de dano.") 
        print(f"Vida agora: {self.vida}")

    def esta_vivo(self):
        return self.vida > 0
    
class Guerreira(Personagem):
    def __init__(self, nome, vida, forca):
        super().__init__(nome, vida)
        self.forca = forca
        
        def atacar(self):
            print(f"{self.nome} ataca com a espada!")
            return self.forca
        
class Mago(Personagem):
    def __init__(self, nome, vida, mana):
        super().__init__(nome, vida)
        self.mana = mana
        
        def atacar(self):
            if self.mana >= 10:
                self.mana -= 10
                print(f"{self.nome} lança magia!")
                print(f"Mana restante: {self.mana}")
                return 25
            else: print(f"{self.nome} ataque fraco! Mana insuficiente.")
            return 5

class Arqueiro(Personagem):
    def __init__(self, nome, vida, flechas):
        super().__init__(nome, vida)
        self.flechas = flechas
        
        def atacar(self):
            if self.flechas > 0:
                self.flechas -= 1
                print(f"{self.nome} ataca com flecha!")
                return 15
            else: print(f"{self.nome} sem flecha, sem ataque!")
            return 0

# CRIANDO PERSONAGENS

mago = Mago("Gandalf", 125, 100)
guerreira = Guerreira("Atenas", 130, 60)
arqueiro = Arqueiro("Arqueiro-Verde", 80, 30)

# TESTANDO MÉTODOS

# print(f"Ataque do {mago.nome}: {mago.atacar()} de dano")
# mago.sofrer_dano(45)
# print(f"{mago.esta_vivo()}")

# print(f"Ataque do {arqueiro.nome}: {arqueiro.atacar()} de dano")
# arqueiro.sofrer_dano(10)
# print(f"{arqueiro.esta_vivo()}")

# print(f"Ataque da {guerreira.nome}: {guerreira.atacar()} de dano")
# guerreira.sofrer_dano(10)
# print(f"{guerreira.esta_vivo()}")
# print(f"{guerreira.ataque_critico()}")

##### FUNÇÃO DE COMBATE

def combate(p1, p2):
    turno = 1

    while p1.esta_vivo() and p2.esta_vivo():
        print(f"\n--- Turno {turno} ---")

        dano = p1.atacar()
        p2.sofrer_dano(dano)

        if not p2.esta_vivo():
            print(f"{p2.nome} foi derrotada!")
            break

        dano = p2.atacar()
        p1.sofrer_dano(dano)
        
        if not p1.esta_vivo():
            print(f"{p1.nome} foi derrotado!")
            break

        turno += 1

combate(mago, guerreira)


        