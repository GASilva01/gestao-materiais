estoque = []
proximo_id = 1000


def cadastrar_item():
    global proximo_id
    material = {}
    atual_id = proximo_id
    material["codigo"] = atual_id

    while True:
        nome = input("Informe o nome do material: ").strip().lower()
        if nome == "":
            print("Erro: Nome inválido.")
        else:
            material["nome"] = nome
            break

    while True:
        try:
            quantidade = int(input(f"Informe a quantidade de {material['nome']}: "))
            if quantidade > 0 and quantidade < 5000:
                material["quantidade"] = quantidade
                print(
                    f"\nCadastro realizado com sucesso. Código do material: {atual_id}"
                )
                proximo_id += 1
                break
            else:
                print("Erro: Quantidade inválida.")
        except ValueError:
            print("Erro: Informe apenas números.")

    return material


def visualizar_estoque_geral(estoque):
    if not estoque:
        print("\nErro: Nenhum material cadastrado ainda.")
        return

    print(f"\n{'='*21} VISÃO GERAL {'='*21}")
    print(f"{'Código':<10} | {'Material':<20} | {'Quantidade':<20}")
    print("-" * 55)
    for material in estoque:
        print(
            f"{material['codigo']:<10} | {material['nome']:<20} | {material['quantidade']:<20}"
        )
    print("-" * 55)


def alterar_quantidade(estoque):
    if not estoque:
        print("\nErro: Nenhum material cadastrado ainda.")
        return

    busca = (
        input("Informe o código ou nome do material que deseja alterar a quantidade: ")
        .strip()
        .lower()
    )
    encontrado = False
    for material in estoque:
        if material["nome"] == busca or str(material["codigo"]) == busca:
            encontrado = True
            print(
                f"Quantidade atual de {material['nome']} (COD: {material['codigo']}): {material['quantidade']} peças."
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
    if not encontrado:
        print(f"Erro: '{busca}' não encontrado no estoque.")


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
        material = cadastrar_item()
        estoque.append(material)
    elif opcao == "2":
        visualizar_estoque_geral(estoque)
    elif opcao == "3":
        alterar_quantidade(estoque)
    else:
        print("Erro: Opção invalida.")
