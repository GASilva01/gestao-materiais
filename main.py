import json

estoque = {}
proximo_id = 1000


def salvar_estoque():
    with open("estoque.json", "w", encoding="utf-8") as arquivo:
        json.dump(estoque, arquivo, ensure_ascii=False, indent=4)


def carregar_estoque():
    global estoque, proximo_id
    try:
        with open("estoque.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

            estoque = {}
            for chave, valor in dados.items():
                chave_inteira = int(chave)
                estoque[chave_inteira] = valor

            if estoque:
                proximo_id = max(estoque.keys()) + 1  # estoque.keys retorna os codigos existentes,
    #                                                    # max() pega o maior existente
    #                                                    # +1 garante que o proximo codigo cadastrado será novo
    #                                                    # keys é função nativa que retorna as chaves de um dicionario
    except (FileNotFoundError, json.JSONDecodeError):
        estoque = {}  # se o estoque nao existir, aqui ele é criado


def cadastrar_item():
    global proximo_id

    while True:
        nome = input("Informe o nome do material: ").strip().capitalize()
        if nome == "":
            print("Erro: Nome inválido.")
        else:
            break
    unidades = {"1": "Pc", "2": "Kg", "3": "Lt"}
    while True:
        print("\n--- Unidades de medida ---")
        for chave, valor in unidades.items():
            print(f"{chave}. {valor}")

        opcao = input(f"Informe a unidade de medida para o material {nome}: ")

        if opcao in unidades:
            un = unidades[opcao]
            break
        else:
            print("Opção inválida")

    while True:
        try:
            quantidade = int(input(f"Informe a quantidade de {nome}: "))
            if quantidade > 0 and quantidade < 5000:
                codigo = proximo_id
                estoque[codigo] = {"nome": nome, "quantidade": quantidade, "unidade": un}
                print(f"\nCadastro realizado com sucesso. Código do material: {codigo}")
                salvar_estoque()
                proximo_id += 1
                break
            else:
                print("Erro: Quantidade inválida.")
        except ValueError:
            print("Erro: Informe apenas números.")


def visualizar_estoque_geral():
    if not estoque:
        print("\nErro: Nenhum material cadastrado ainda.")
        return

    print(f"\n{'='*21} VISÃO GERAL {'='*21}")
    print(f"{'Código':<10} | {'Material':<20} | {'Quantidade':<10} | {'Unidade':<5} ")
    print("-" * 55)
    for codigo, dados in estoque.items():
        print(f"{codigo:<10} | {dados['nome']:<20} | {dados['quantidade']:<10} | {dados['unidade']:<5}")
    print("-" * 55)


def alterar_quantidade():
    if not estoque:
        print("\nErro: Nenhum material cadastrado ainda.")
        return
    try:
        codigo = int(input("Informe o código do material que deseja alterar a quantidade: "))
        if codigo in estoque:
            material = estoque[codigo]

            print(f"Quantidade atual de {material['nome']} (COD: {codigo}): {material['quantidade']} peças.")
            while True:
                try:
                    nova_quantidade = int(input(f"Informe a nova quantidade de {material['nome']}: "))
                    if nova_quantidade > 0 and nova_quantidade < 5000:
                        material["quantidade"] = nova_quantidade
                        print("Quantidade alterada com sucesso.")
                        salvar_estoque()
                        break
                    else:
                        print("Erro: Quantidade inválida.")
                except ValueError:
                    print("Erro: Informe apenas números.")
        else:
            print(f"Erro: Código '{codigo}' não encontrado no estoque.")
    except ValueError:
        print("Erro: Código inválido.")


def excluir_material():
    if not estoque:
        print("\nErro: Nenhum material cadastrado ainda.")
        return

    busca = input("Informe o código do material que deseja excluir: ").strip()

    if not busca.isdigit():
        print("Erro: Informe um código válido (número).")
        return

    codigo = int(busca)

    if codigo in estoque:
        material = estoque[codigo]
        confirmacao = (
            input(f"Tem certeza que deseja excluir '{material['nome']}' (COD: {codigo})? (s/n): ").strip().lower()
        )

        if confirmacao == "s":
            del estoque[codigo]
            print("Material excluído.")
            salvar_estoque()
        else:
            print("Operação cancelada.")
    else:
        print(f"Erro: Código '{codigo}' não encontrado no estoque.")


carregar_estoque()
while True:
    print(
        "\n--- Gestão de Materiais ---"
        "\n\n1. Cadastrar material."
        "\n2. Visão geral do estoque."
        "\n3. Alterar quantidade de materiais."
        "\n4. Excluir material."
        "\n5. Sair.\n"
    )
    opcao = input("Escolha uma opção: ")
    if opcao == "5":
        print("Encerrando o sistema...")
        break
    elif opcao == "1":
        cadastrar_item()
    elif opcao == "2":
        visualizar_estoque_geral()
    elif opcao == "3":
        alterar_quantidade()
    elif opcao == "4":
        excluir_material()
    else:
        print("Erro: Opção invalida.")
