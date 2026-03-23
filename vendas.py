ARQUIVO_VENDAS = "vendas.txt"


def registrar_venda(produto, quantidade, total):

    with open(ARQUIVO_VENDAS, "a") as f:
        linha = f"{produto} - {quantidade} unidades - R${total}\n"
        f.write(linha)


def ver_historico():

    try:

        with open(ARQUIVO_VENDAS, "r") as f:

            print("\nHistórico de vendas:\n")
            print(f.read())

    except:

        print("Nenhuma venda registrada.")


def total_vendido():

    try:

        total = 0

        with open(ARQUIVO_VENDAS, "r") as f:

            for linha in f:

                partes = linha.split("R$")
                valor = float(partes[1])
                total += valor

        print("Total vendido: R$", total)

    except:

        print("Nenhuma venda registrada.")


def produto_mais_vendido():

    try:

        contagem = {}

        with open(ARQUIVO_VENDAS, "r") as f:

            for linha in f:

                produto = linha.split("-")[0].strip()

                contagem[produto] = contagem.get(produto, 0) + 1

        mais = max(contagem, key=contagem.get)

        print("Produto mais vendido:", mais)

    except:

        print("Nenhuma venda registrada.")
