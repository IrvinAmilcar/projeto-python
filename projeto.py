import os
from time import sleep

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
    sleep(0.5)
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        Cadastrar_Receitas()
    elif opcao == 2:
        Visualizar_receitas()
    elif opcao == 3:
        Atualizar_receitas()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Opção inválida")
        sleep(1.5)
        print("Retornando ao menu. . .")
        sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        menu_principal()

        
        

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
    print("\nVisualizar todas as receitas (1)")
    print("Visualizar receitas por nome (2)\n")
    escolha_v = (input("Escolha uma operação ou 'sair' para voltar ao menu: "))
    if escolha_v == 'sair':
        os.system('cls' if os.name == 'nt' else 'clear')
        menu_principal()
    elif escolha_v == '1':
        with open("Receitas.txt", "r", encoding="utf-8") as f:
            os.system('cls' if os.name == 'nt' else 'clear')
            for linha in f:
                print(linha.strip())
        escolha_v1 = int(input("Deseja voltar ao menu (1) ou encerrar o programa (2): "))
        if escolha_v1 == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            menu_principal()
        elif escolha_v1 == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Programa ENCERRADO!")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Opção inválida!")
            print("Programa ENCERRADO")
    elif escolha_v == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        palavra_chave = input("Informe o nome da receita: ")
        try:
            with open("Receitas.txt", "r", encoding="utf-8") as f:
                linhas = f.readlines()
                found = False
                for e in range(len(linhas)):
                    if palavra_chave.lower() in linhas[e].lower():
                        found = True
                        print(linhas[e].strip())
                        for b in range(e + 1, len(linhas)):
                            if linhas[b].strip() == "":
                                break
                            print(linhas[b].strip())
                        break
                if not found:
                    print("Receita não encontrada!")
        except FileNotFoundError:
            print("Arquivo 'Receitas.txt' não encontrado!")

        escolha_v1 = input("Deseja voltar ao menu (1) ou encerrar o programa (2): ")
        if escolha_v1 == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            menu_principal()
        elif escolha_v1 == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Programa ENCERRADO!")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Opção inválida!")
            print("Programa ENCERRADO")
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Opção inválida!")
        Visualizar_receitas()

def Atualizar_receitas():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Opção selecionada: Atualização de receitas\n")
    print("Atualizar nome da receita (1)")
    print("Atualizar ingredientes (2)")
    print("Atualizar modo de preparo (3)")
    escolha_a = input("\nSelecione uma operação ou 'sair' para retornar ao menu: ")
    if escolha_a == 'sair':
        os.system('cls' if os.name == 'nt' else 'clear')
        menu_principal()

   



    

    
        

    
    
    
        
    




print("Deseja iniciar o programa? (start)")

inicializador = input()
os.system('cls' if os.name == 'nt' else 'clear')

if inicializador == 'start':
    menu_principal()
else:
    print("O programa nem iniciou e ja encerrou")
