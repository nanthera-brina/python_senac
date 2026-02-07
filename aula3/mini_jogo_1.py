# MINI-JOGO
'''Em um mundo de mistério...'''

class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
    
    def atacar(self):   # método genérico
        return 10
    
    def sofrer_dano(self, dano):   # reduz vida e impede valor negativo
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0
        print(f"{self.nome} sofre {dano} de dano.") 
        print(f"Vida agora: {self.vida}")

    def esta_vivo(self):  # verifica se o personagem ainda está vivo
        return self.vida > 0

'''...existem pessoas capazes de mudar tudo.'''

mago = Personagem("Mago", 50)
guerreira = Personagem("Guerreira", 30)
arqueiro = Personagem("Arqueiro", 20)

### escolha personagem ###

# persona = input("Escolha um personagem (mago, guerreira ou arqueiro): ").lower()

# match persona:
#     case "mago": 
#         print(vars(mago))

#     case "guerreira": 
#         print(vars(guerreira))

#     case "arqueiro": 
#         print(vars(arqueiro))

### testando métodos ###

print(f"Ataque do {mago.nome}: {mago.atacar()} de dano")
mago.sofrer_dano(45)
print(f"{mago.esta_vivo}")

