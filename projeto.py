import os

def menu_principal():
    print("""

    Menu Principal______________

    (1) Cadastrar novas receitas
    (2) Visualizar receitas
    (3) Atualizar receitas
    (4) Excluir receitas 
    (5) Sugerir uma receita
    (6) Favoritos
    (7) Sair
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
        if continuar.lower()!= "s":
            
            print("Deseja voltar ao menu (1) ou encerrar o programa (2)?")
            escolha_c = int(input())
            if escolha_c == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                menu_principal()
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Programa ENCERRADO!")
            break

def Visualizar_receitas():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Opção selecionada: Visualizar receitas!")
    metodo_de_visualizacao = input("""Você deseja pesquisar por que método?
Digite [P] para ser por país de origem
Digite [F] para ser por favoritos
Digite [D] para ser por pesquisa direta\n""").lower()
    os.system('cls' if os.name == 'nt' else 'clear')
    if metodo_de_visualizacao == "p":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Opção escolhida: País de origem")
    elif metodo_de_visualizacao == "f":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Opção escolhida: Favoritos")
    elif metodo_de_visualizacao == "d":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Opção escolhida: Pesquisa direta")
    

    
        

    
    
    
        
    




print("Deseja iniciar o programa? (start)")

inicializador = input()
os.system('cls' if os.name == 'nt' else 'clear')

if inicializador == 'start':
    menu_principal()
else:
    print("O programa nem iniciou e ja encerrou")
