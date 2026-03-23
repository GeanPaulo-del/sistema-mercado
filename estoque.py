import json

ARQUIVO_PRODUTOS = "produtos.json"


def carregar_produtos():

    try:
        with open(ARQUIVO_PRODUTOS, "r") as f:
            return json.load(f)

    except:
        return {}


def salvar_produtos(produtos):

    with open(ARQUIVO_PRODUTOS, "w") as f:
        json.dump(produtos, f, indent=4)


def ver_produtos(produtos):

    print("\nProdutos disponíveis:")

    for nome in produtos:

        estoque = produtos[nome]["estoque"]
        preco = produtos[nome]["preco"]

        print(nome, "- estoque:", estoque, "- preço: R$", preco)


def adicionar_produto(produtos):

    nome = input("Nome do produto: ").lower()

    preco = float(input("Preço: "))
    estoque = int(input("Quantidade: "))

    produtos[nome] = {
        "preco": preco,
        "estoque": estoque
    }

    salvar_produtos(produtos)

    print("Produto adicionado com sucesso!")
