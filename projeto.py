import os

def menu_principal():
    print("""

    Menu Principal______________

    (1) Cadastrar novas receitas
    (2) Consultar receitas
    (3) Atualizar receitas
    (4) Excluir receitas 
    (5) Sugerir uma receita
    (6) Sair
    """)
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        Cadastrar_Receitas()
    elif opcao == 2:
        Visualizar_receitas()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Opção inválida")
        print("__PROGRAMA ENCERRADO__")

def Cadastrar_Receitas():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Opção selecionada: Cadastros de receitas!")
    while True:
        nome_receita = input("Digite o nome da receita: ")
        pais_de_origem = input("Digite o país de origem da receita: ")
        ingredientes = input("Digite os ingredientes da receita (separados por vírgula): ")
        preparo = input("Digite o modo de preparo da receita: ")

        with open("Receitas.txt", "a", encoding="utf-8") as f:
            f.write(f"Receita: {nome_receita}\n")
            f.write(f"País de origem: {pais_de_origem}\n")
            f.write(f"Ingredientes: {ingredientes}\n")
            f.write(f"Modo de preparo: {preparo}\n\n")

        print("Receita adicionada com sucesso!")
        continuar = input("Deseja cadastrar outra receita? (s/n): ")
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""
        Opção selecionada: Adicionar
        """)
        while True:
            escolha ==
