def adicionar ():
    file = open("Receitas.txt","a", encoding= "utf8")
    file.write(input("Adicione a teste..."))
    file.close()
    



















while True:
    print("""
    Adicionar receitas  (1)
    Remover receitas    (2)
    Visualizar receitas (3)
    Atualizar receitas  (4)
    Filtras por país    (5)
    Lista de favoritos  (6)
    Receita aleatória   (7)
    (função especial)   (8)
    Sair                (0)
    """)
    escolha = int(input("Escolha uma opção: "))
    if escolha == 0:
        break
    elif escolha == 1:
        adicionar()

