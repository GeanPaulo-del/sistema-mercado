import json

# PRODUTOS PADRÃO
produtos = {
    "maçã": {"estoque": 3, "preco": 2},
    "banana": {"estoque": 2, "preco": 3},
    "pão": {"estoque": 5, "preco": 4},
    "leite": {"estoque": 4, "preco": 5}
}

carrinho = []


# SALVAR PRODUTOS
def salvar_produtos():
    with open("produtos.json", "w") as arquivo:
        json.dump(produtos, arquivo)


# CARREGAR PRODUTOS
def carregar_produtos():
    global produtos
    try:
        with open("produtos.json", "r") as arquivo:
            produtos = json.load(arquivo)
    except:
        print("Arquivo de produtos não encontrado. Usando padrão.")


def ver_produtos():
    print("\nProdutos disponíveis:")
    for produto, info in produtos.items():
        print(produto, "- estoque:", info["estoque"], "- preço: R$", info["preco"])


def comprar_produto():

    nome = input("Digite o produto que deseja comprar: ").strip().lower()

    if nome in produtos:

        if produtos[nome]["estoque"] > 0:

            carrinho.append(nome)
            produtos[nome]["estoque"] -= 1
            salvar_produtos()

            print("Produto adicionado ao carrinho!")

        else:
            print("Produto sem estoque!")

    else:
        print("Produto não encontrado!")


def ver_carrinho():

    print("\nCarrinho:")

    resumo = {}
    total = 0

    for item in carrinho:
        if item in resumo:
            resumo[item] += 1
        else:
            resumo[item] = 1

    for produto in resumo:
        quantidade = resumo[produto]
        preco = produtos[produto]["preco"]
        subtotal = quantidade * preco

        print(produto, "-", quantidade, "unidades - R$", subtotal)

        total += subtotal

    print("Total da compra: R$", total)


def remover_produto():

    nome = input("Digite o produto que deseja remover: ").strip().lower()

    if nome in carrinho:

        carrinho.remove(nome)
        produtos[nome]["estoque"] += 1
        salvar_produtos()

        print("Produto removido do carrinho!")

    else:
        print("Esse produto não está no carrinho!")


def adicionar_produto():

    nome = input("Nome do produto: ").strip().lower()

    if nome in produtos:
        print("Produto já existe!")
        return

    preco = float(input("Preço do produto: R$ "))
    estoque = int(input("Quantidade em estoque: "))

    produtos[nome] = {
        "estoque": estoque,
        "preco": preco
    }

    salvar_produtos()

    print("Produto adicionado com sucesso!")


def finalizar_compra():

    if len(carrinho) == 0:
        print("Carrinho vazio!")
        return

    print("\n===== RECIBO =====")

    resumo = {}
    total = 0

    for item in carrinho:
        if item in resumo:
            resumo[item] += 1
        else:
            resumo[item] = 1

    for produto in resumo:

        quantidade = resumo[produto]
        preco = produtos[produto]["preco"]
        subtotal = quantidade * preco

        print(produto, "-", quantidade, "unidades - R$", subtotal)

        total += subtotal

    print("\nTotal:", total)

    pagamento = float(input("Valor pago: R$ "))

    if pagamento < total:
        print("Valor insuficiente!")
        return

    troco = pagamento - total

    print("Troco: R$", troco)
    print("Obrigado pela compra!")

    with open("vendas.txt", "a") as arquivo:

        arquivo.write("===== VENDA =====\n")

        for produto in resumo:
            quantidade = resumo[produto]
            preco = produtos[produto]["preco"]
            subtotal = quantidade * preco

            arquivo.write(f"{produto} - {quantidade} unidades - R$ {subtotal}\n")

        arquivo.write(f"Total: R$ {total}\n")
        arquivo.write("---------------------\n")

    carrinho.clear()


def ver_historico():

    try:
        with open("vendas.txt", "r") as arquivo:
            print("\n===== HISTÓRICO DE VENDAS =====")
            print(arquivo.read())

    except:
        print("Nenhuma venda registrada ainda.")


def total_vendido():

    total_geral = 0

    try:
        with open("vendas.txt", "r") as arquivo:

            for linha in arquivo:

                if "Total:" in linha:

                    valor = linha.split("R$")[1]
                    total_geral += float(valor)

        print("\nTotal vendido no sistema: R$", total_geral)

    except:
        print("Nenhuma venda registrada ainda.")


def produto_mais_vendido():

    vendas = {}

    try:
        with open("vendas.txt", "r") as arquivo:

            for linha in arquivo:

                if " - " in linha and "unidades" in linha:

                    partes = linha.split(" - ")

                    produto = partes[0]
                    quantidade = int(partes[1].split()[0])

                    if produto in vendas:
                        vendas[produto] += quantidade
                    else:
                        vendas[produto] = quantidade

        if vendas:

            mais_vendido = max(vendas, key=vendas.get)

            print("\nProduto mais vendido:", mais_vendido)
            print("Quantidade vendida:", vendas[mais_vendido])

        else:
            print("Nenhuma venda registrada.")

    except:
        print("Nenhuma venda registrada.")


# CARREGAR PRODUTOS
carregar_produtos()


while True:

    print("\n1 - Ver produtos")
    print("2 - Comprar produto")
    print("3 - Ver carrinho")
    print("4 - Remover produto")
    print("5 - Finalizar compra")
    print("6 - Sair")
    print("7 - Adicionar produto")
    print("8 - Ver histórico de vendas")
    print("9 - Total vendido")
    print("10 - Produto mais vendido")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        ver_produtos()

    elif opcao == "2":
        comprar_produto()

    elif opcao == "3":
        ver_carrinho()

    elif opcao == "4":
        remover_produto()

    elif opcao == "5":
        finalizar_compra()

    elif opcao == "6":

       confirmar = input("Tem certeza que deseja sair? (s/n): ").lower()

    if confirmar == "s":
        print("Sistema encerrado")
        break

    elif opcao == "7":
        adicionar_produto()

    elif opcao == "8":
        ver_historico()

    elif opcao == "9":
        total_vendido()

    elif opcao == "10":
        produto_mais_vendido()

    else:
        print("Opção inválida!")

print("Programa finalizado.")
