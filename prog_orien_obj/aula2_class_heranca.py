## EXEMPLO DE HERANÇA

# Super Classe

class Animal:
    def __init__(self, nome, idade, peso, raca, especie):    ##lembrar de dar espaço depois de def!!!
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.raca = raca
        self.especie = especie
    
    def __str__(self):
        return "SOM"

# Classes Filhos

class Cachorro(Animal):
    def __str__(self):
        return "Au Au"

class Gato(Animal):
    def __str__(self):
        return "Miau"

class Porco(Animal):
    def __str__(self):
        return "Ronc"

# Criar objetos

cachorro1 = Cachorro("Rex", 2, "5 kg", "Vira-lata", "Mamífero")
gato1 = Gato("Luna", 7, "2 kg", "Sem", "Mamífero")
porco1 = Porco("Rosa", 3, "100 kg", "Sem", "Mamífero")

print(cachorro1)
