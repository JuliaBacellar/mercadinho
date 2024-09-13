import json

# Lista de produtos disponíveis
produtos = [
    {"nome": "chá de curumim", "preco": 4.99, "estoque": 83},
    {"nome": "frutas secas", "preco": 15.99, "estoque": 58},
    {"nome": "miojo de café da manhã", "preco": 2.50, "estoque": 34},
    {"nome": "pé de galinha", "preco": 8.50, "estoque": 49},
    {"nome": "café descafeinado", "preco": 10.00, "estoque": 48},
    {"nome": "pipoca", "preco": 5.00, "estoque": 90},
    {"nome": "salsicha vegana", "preco": 12.00, "estoque": 68},
    {"nome": "pistache", "preco": 20.00, "estoque": 34},
    {"nome": "feijão em lata", "preco": 6.00, "estoque": 28},
    {"nome": "brownie", "preco": 4.50, "estoque": 5},
    {"nome": "lagosta", "preco": 50.00, "estoque": 87},
    {"nome": "fuçinho de porco", "preco": 9.99, "estoque": 10},
    {"nome": "leite de cabra", "preco": 7.50, "estoque": 10}
]

# Função para mostrar a lista de produtos
def mostrar_produtos():
    print("\nProdutos disponíveis:")
    for idx, produto in enumerate(produtos, 1):
        print(f"{idx}. {produto['nome']} - R${produto['preco']} - {produto['estoque']} unidades em estoque")

# Função para obter o índice do produto passando por cada produto e convertendo para minusculo
def obter_produto(nome):
    for produto in produtos: 
        if produto['nome'].lower() == nome.lower():
            return produto
    return None #caso o produto não seja encontrado

# Função para salvar nota fiscal em um arquivo txt
def salvar_nota_fiscal(nome_cliente, compras, valor_final, desconto_aplicado):
    with open('nota_fiscal.txt', 'w') as nota_fiscal:
        nota_fiscal.write(f"Cliente: {nome_cliente}\n")
        nota_fiscal.write("Produtos comprados:\n")
        for compra in compras:
            nota_fiscal.write(f"{compra['nome']} - {compra['quantidade']} unidades - R${compra['preco'] * compra['quantidade']:.2f}\n")
        nota_fiscal.write(f"Total da compra: R${valor_final:.2f}\n")
        if desconto_aplicado:
            nota_fiscal.write("Desconto de 5% aplicado (Clube Mercadinho da Vila)\n")
        nota_fiscal.write("Obrigada pela compra!\n")

# Função principal
def mercadinho():
    print("Olá, seja bem-vindo ao Mercadinho da Vila!")
    nome_cliente = input("Qual seria seu nome? ")
    
    compras = []
    valor_total = 0
    desconto_aplicado = False

    while True:
        mostrar_produtos()
        nome_produto = input("\nDigite o nome do produto que deseja comprar (ou 'sair' para finalizar): ").strip()

        if nome_produto.lower() == 'sair':
            break

        produto = obter_produto(nome_produto)

        if produto is None:
            print("Erro: Produto não existe!")
            continue

        quantidade = int(input(f"Quantas unidades de {produto['nome']} deseja comprar? "))

        if quantidade > produto['estoque']:
            print("Quantidade Insuficiente: A quantidade solicitada é maior do que a disponível em estoque. Por favor, escolha uma quantidade menor.")
            continue

        if quantidade > 10:
            print("Erro: Você não pode comprar mais de 10 unidades do mesmo produto.")
            continue

        # Atualizar estoque e valor total
        produto['estoque'] -= quantidade
        valor_produto = produto['preco'] * quantidade
        compras.append({"nome": produto['nome'], "quantidade": quantidade, "preco": produto['preco']})
        valor_total += valor_produto

        print(f"{quantidade} unidades de {produto['nome']} adicionadas ao carrinho.")

        # Verificar se o cliente deseja adicionar mais produtos
        adicionar_mais = input("Deseja adicionar mais algum produto? (sim/não): ").strip().lower()
        if adicionar_mais == 'não':
            break

    # Aplicar desconto se o cliente for membro do clube
    clube_resposta = input("Você é membro do Clube Mercadinho da Vila? (sim/não): ").strip().lower()
    if clube_resposta == 'sim':
        cpf = input("Por favor, insira seu CPF para o desconto: ")
        desconto = valor_total * 0.05
        valor_total -= desconto
        desconto_aplicado = True

    # Exibir o valor final e finalizar a compra
    print(f"Sua compra ficou no total de R${valor_total:.2f}.")
    finalizar = input("Deseja finalizar sua compra? (sim/não): ").strip().lower()
    
    if finalizar == 'sim':
        salvar_nota_fiscal(nome_cliente, compras, valor_total, desconto_aplicado)
        print("Compra finalizada! Sua nota fiscal foi gerada em 'nota_fiscal.txt'.")
        print("Obrigada pela compra!:)")
    else:
        print("Compra cancelada.")

# Executar o mercadinho
mercadinho()
