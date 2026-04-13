estoque = {}
proximo_id = 1000


def cadastrar_item():
    global proximo_id

    while True:
        nome = input("Informe o nome do material: ").strip().lower()
        if nome == "":
            print("Erro: Nome inválido.")
        else:
            break

    while True:
        try:
            quantidade = int(input(f"Informe a quantidade de {nome}: "))
            if quantidade > 0 and quantidade < 5000:
                codigo = proximo_id
                estoque[codigo] = {"nome": nome, "quantidade": quantidade}

                print(f"\nCadastro realizado com sucesso. Código do material: {codigo}")
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
    print(f"{'Código':<10} | {'Material':<20} | {'Quantidade':<20}")
    print("-" * 55)
    for codigo, dados in estoque.items():
        print(f"{codigo:<10} | {dados['nome']:<20} | {dados['quantidade']:<20}")
    print("-" * 55)


def alterar_quantidade():
    if not estoque:
        print("\nErro: Nenhum material cadastrado ainda.")
        return

    busca = input(
        "Informe o código do material que deseja alterar a quantidade: "
    ).strip()
    if not busca.isdigit():
        print("Erro: Informe um código válido (número).")
        return
    codigo = int(busca)

    if codigo in estoque:
        material = estoque[codigo]

        print(
            f"Quantidade atual de {material['nome']} (COD: {codigo}): {material['quantidade']} peças."
        )
        while True:
            try:
                nova_quantidade = int(
                    input(f"Informe a nova quantidade de {material['nome']}: ")
                )
                if nova_quantidade > 0 and nova_quantidade < 5000:
                    material["quantidade"] = nova_quantidade
                    print("Quantidade alterada com sucesso.")
                    break
                else:
                    print("Erro: Quantidade inválida.")
            except ValueError:
                print("Erro: Informe apenas números.")
    else:
        print(f"Erro: Código '{codigo}' não encontrado no estoque.")


while True:
    print(
        "\n--- Gestão de Materiais ---"
        "\n\n1. Cadastrar material."
        "\n2. Visão geral do estoque."
        "\n3. Alterar quantidade de materiais."
        "\n4. Sair.\n"
    )
    opcao = input("Escolha uma opção: ")
    if opcao == "4":
        print("Encerrando o sistema...")
        break
    elif opcao == "1":
        cadastrar_item()
    elif opcao == "2":
        visualizar_estoque_geral()
    elif opcao == "3":
        alterar_quantidade()
    else:
        print("Erro: Opção invalida.")
