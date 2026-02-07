# Classe

class Pessoa:
    def __init__(self, nome, idade, cpf, funcao):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.funcao = funcao

    def __str__(self):
        return f"Olá, meu nome é {self.nome}."

# Objetos

aluno1 = Pessoa("Antônio", 35, "58473282", "aluno")
diretor = Pessoa("José", 19, "235252", "diretor")
professor1 = Pessoa("Maria", 44, "23234324", "professora")

# print(vars(aluno1))
# print(vars(diretor))
# print(vars(professor1))

print(aluno1)