## PROBLEMA: 
# GUARDAR ITENS -> sistema de armazenar informações sobre os itens comprados
# GUARDAR VALORES -> sistema deve registrar valores associados a cada item 
# SOMA TOTAL ->
# AVISAR SE PASSAR DO LIMITE -> alerta se as compras passarem do limite


### Itens

itens = {                       # dicionário, código, nome e valor (cod, 0, 1) -> ordem do dicionário
    1: ("Caderno", 25.00),
    2: ("Lápis", 1.50),
    3: ("Caneta", 2.50),
    4: ("Estojo", 12.00),
    5: ("Borracha", 3.00)
} 

### Funções

def produtos():   # função para mostrar os itens e valores
    print("\nProdutos disponíveis na loja:")

    for cod in itens:   # o cod é criado agora, vai informar qual é o cod do dicionario, depois expõe o nome (0) e o valor (1)
        nome = itens[cod][0]
        valor = itens [cod][1]
        print(f"{cod} - {nome} | R$ {valor}")

def comprar(soma_total): # função para comprar item
    produtos()
    codigo = int(input("\nDigite código do item que você deseja comprar: "))
    
    if codigo in itens:  # se o codigo tiver no itens, vai mostrar nome e valor
        nome, valor = itens[codigo]
        soma_total += valor     # a soma dos itens vai ocorrer a partir da soma que a pessoa tem (0 -> definido no menu)
        print(f"{nome} adicionado ao carrinho.")
        print(f"Soma atual da compra: R${soma_total}")
    else:
        print("Item não existe!")

    return soma_total
 
# Menu

def menu_loja(): # função do menu da loja

    limite = float(input("Digite o seu limite de gasto: "))

    soma_total = 0 > limite # valor definido

    while True:  # se verdade o while continua, se falso ele repete o menu
        print("Bem vindo/a a loja")
        print("\nMENU")
        print("1 - Ver itens da loja")
        print("2 - Comprar itens")
        print("3 - Sair")

        escolha = input("\nEscolha uma opção: ")

        if escolha == "1":
            produtos()
        elif escolha == "2":
            soma_total = comprar(soma_total)
        elif escolha == "3":
            print("\nRelatório do pedido")
            print(f"Total a pagar: R$ {soma_total}")
            print("\nCompra finalizada.")
            break
        else:
            print("Opção inválida!")

menu_loja ()
