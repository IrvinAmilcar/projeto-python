import os

print("Iniciar programa? (start)")
inicializador = input()
if inicializador == "start":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
    MENU___________________

    (1) Adicionar receitas
    (2) Visualisar receitas
    (3) Atualizar receitas
    (4) Remover receitas
    (5) Sair
    """)
    
    escolha = int(input("Escolha uma opção: "))
   
    if escolha == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""
        Opção selecionada: Adicionar
        """)
