import os
from time import sleep
import random


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
        cadastrar_Receitas()
    elif opcao == 2:
        visualizar_receitas()
    elif opcao == 3:
        atualizar_receitas()
    elif opcao == 4:
        excluir_receitas()
    elif opcao == 5:
        receitasAleatórias()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Opção inválida")
        sleep(1.5)
        print("Retornando ao menu. . .")
        sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        menu_principal()


def cadastrar_Receitas():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Opção selecionada: Cadastros de receitas!")
    while True:
        nome_receita = input("Digite o nome da receita: ")
        pais_de_origem = input("Digite o país de origem da receita: ")
        ingredientes = input(
            "Digite os ingredientes da receita (separados por vírgula): ")
        preparo = input("Digite o modo de preparo da receita: ")

        with open("Receitas.txt", "a", encoding="utf-8") as f:
            f.write(f"Receita: {nome_receita}\n")
            f.write(f"País de origem: {pais_de_origem}\n")
            f.write(f"Ingredientes: {ingredientes}\n")
            f.write(f"Modo de preparo: {preparo}\n\n")

        print("Receita adicionada com sucesso!")
        continuar = input("Deseja cadastrar outra receita? (s/n): ")
        os.system('cls' if os.name == 'nt' else 'clear')
        if continuar.lower() != "s":

            print("Deseja voltar ao menu (1) ou encerrar o programa (2)?")
            escolha_c = int(input())
            if escolha_c == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                menu_principal()
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Programa ENCERRADO!")
            break


def visualizar_receitas():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Opção selecionada: Visualizar receitas!")
    print("\nVisualizar todas as receitas (1)")
    print("Visualizar receitas por nome (2)")
    print("Visualizar receitas por país de origem (3)\n")
    escolha_v = (input("Escolha uma operação ou 'sair' para voltar ao menu: "))
    if escolha_v == 'sair':
        os.system('cls' if os.name == 'nt' else 'clear')
        menu_principal()
    elif escolha_v == '1':
        with open("Receitas.txt", "r", encoding="utf-8") as f:
            os.system('cls' if os.name == 'nt' else 'clear')
            for linha in f:
                print(linha.strip())
        escolha_v1 = int(
            input("Deseja voltar ao menu (1) ou encerrar o programa (2): "))
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

        escolha_v1 = input(
            "Deseja voltar ao menu (1) ou encerrar o programa (2): ")
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
    elif escolha_v == '3':
        os.system('cls' if os.name == 'nt' else 'clear')
        palavra_chave = input("Informe o nome do país: ").lower()
        print()
        try:
            with open("Receitas.txt", "r", encoding="utf-8") as f:
                linhas = f.readlines()
                found = False
                for e in range(len(linhas)):
                    if palavra_chave.lower() in linhas[e].lower():
                        found = True
                        for g in range(e-1, len(linhas)):
                            if linhas[g].strip() == "":
                                break
                            print(linhas[g].strip())
                        print()

                if not found:
                    print("País não encontrado!")
        except FileNotFoundError:
            print("Arquivo 'Receitas.txt' não encontrado!")
        while True:
            escolha_v1 = input(
                "Deseja voltar ao menu (1) ou encerrar o programa (2): ")
            if escolha_v1 == '1':
                os.system('cls' if os.name == 'nt' else 'clear')
                menu_principal()
            elif escolha_v1 == '2':
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Programa ENCERRADO!")
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Opção inválida!\nDigite uma das opções informadas.")
                sleep(2)
                continue
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Opção inválida!")
        visualizar_receitas()


def atualizar_receitas():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""Opção selecionada: Atualização de receitas\n
    Atualizar nome da receita (1)
    Atualizar país da receita (2)
    Atualizar ingredientes (3)
    Atualizar modo de preparo (4)""")
    escolha_a = input(
        "\nSelecione uma operação ou 'sair' para retornar ao menu: ")
    
    if escolha_a == '1':
        atualizar_nome_receita()
    elif escolha_a == '2':
        atualizar_pais_receita()
    elif escolha_a == '3':
        atualizar_ingredientes_receita()
    elif escolha_a == '4':
        atualizar_modo_preparo_receita()
    elif escolha_a == 'sair':
        os.system('cls' if os.name == 'nt' else 'clear')
        menu_principal()
    else:
        print("Opção inválida!")
        sleep(1)
        atualizar_receitas()

def atualizar_nome_receita():
    while True:
        nome_receita_atualizar = input("Digite o nome da receita que deseja atualizar: ")
        novo_nome = input("Digite o novo nome da receita: ")

        try:
            with open("Receitas.txt", "r", encoding="utf-8") as f:
                linhas = f.readlines()

            found = False
            with open("Receitas.txt", "w", encoding="utf-8") as f:
                for linha in linhas:
                    if nome_receita_atualizar.lower() in linha.lower():
                        f.write(linha.replace(nome_receita_atualizar, novo_nome))
                        found = True
                    else:
                        f.write(linha)

            if found:
                print("Receita atualizada.")
            else:
                print("Receita não encontrada.")

        except FileNotFoundError:
            print("Arquivo 'Receitas.txt' não encontrado.")

        escolha = input("\nDeseja atualizar outro nome de receita? (sim/n): ")
        if escolha.lower() != 'sim':
            break

def excluir_receitas():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Opção selecionada: Excluir receitas!')
    while True:
        nome_receita_excluir = input("Digite o nome da receita que deseja excluir: ")

        try:
            with open("Receitas.txt", "r", encoding="utf-8") as f:
                linhas = f.readlines()

            found = False
            with open("Receitas.txt", "w", encoding="utf-8") as f:
                for linha in linhas:
                    if nome_receita_excluir.lower() not in linha.lower():
                        f.write(linha)
                    else:
                        found = True

            if found:
                print("Receita excluída.")
            else:
                print("Receita não encontrada.")

        except FileNotFoundError:
            print("Arquivo 'Receitas.txt' não encontrado.")

        escolha = input("\nDeseja excluir outra receita? (sim/n): ")
        if escolha.lower() != 'sim':
            break



def receitasAleatórias():
    os.system('cls' if os.name == 'nt' else 'clear')
    numero = random.randint(1, 3)
    with open("receitasAleatórias.txt", "r", encoding="utf8") as file:
        for i in range(numero):
            receita_aleatoria = file.readline()
            receita_aleatoria2 = receita_aleatoria.split("//")
        for c in receita_aleatoria2:
            print(f"{c}")
        file.seek(0)
    while True:
        escolha = input(
            "Deseja escolher outra receita aleatória ou voltar ao menu principal?\nDigite [escolher] para escolher outra receita\nDigite [voltar] para voltar ao menu principal\n")
        if escolha == "escolher":
            os.system('cls' if os.name == 'nt' else 'clear')
            receitasAleatórias()
        elif escolha == "voltar":
            os.system('cls' if os.name == 'nt' else 'clear')
            menu_principal()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Digite uma opção dentre as informadas\n")
            continue


print("Deseja iniciar o programa? (start)")

inicializador = input()
os.system('cls' if os.name == 'nt' else 'clear')

if inicializador == 'start':
    menu_principal()
else:
    print("O programa nem iniciou e ja encerrou")
