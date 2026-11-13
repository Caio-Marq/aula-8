import json

def carrregar_produtos():
    arquivo = open("Produtos.json", "r", encoding="utf-8")
    produtos = json.load(arquivo)
    arquivo.close()
    return produtos

def salvar_produtos(produtos):
    arquivo = open("produtos.json", "w", encoding="utf-8")
    json.dump(produtos, arquivo, indent=4, ensure_ascii=False)
    arquivo.close()

produtos = carrregar_produtos()

def entrada_estoque():
    id = int(input("ID do produto:   "))
    nome = input("Nome do produto:   ")
    categoria = input("Ctegoria produto:   ")
    preco = int(input("Preco:      "))
    estoque = int(input("Estoque:       "))

    produtos.append({
        "id": id,
        "nome": nome,
        "categoria": categoria,
        "preco": preco,
        "estoque": estoque
    })
    print(f"\n {nome} adicionado!")
    salvar_produtos(produtos=produtos)

def ver_estoque():
    print("\n--- RELATÓRIO DE ESTOQUE ---")
    for produto in produtos:
        print(produto)
        # print(f"ID: {produto['id']} | {produto['nome']} | Estoque: {produto['estoque']}")

def saida_estoque():
    id_produto = int(input("Digite o ID do produto para SAÍDA: "))
    quantidade = int(input("Digite a quantidade de saída: "))
    for produto in produtos:
        if produto['id'] == id_produto:
            produto['estoque'] -= quantidade
            print(f"Saída registrada! Estoque atual de {produto['nome']}: {produto['estoque']}")









while True:
    print("       SIstema de estoque         ")
    print("      1. Registrar Entrada        ")
    print("      2. Registrar Saida          ")
    print("      3. Ver estoque              ")
    print("      4. Sair                     ")

    opcao = input("    Escolha uma opcao        ")

    if opcao == "1":
        entrada_estoque()

    elif opcao == "2":
        saida_estoque()

    elif opcao == "3":
        ver_estoque()

    elif opcao == "4":
        print("Saindo do Sistema...")
        break
