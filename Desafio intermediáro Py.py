# letra = input("InfoRme a letra: ")
# alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# I = 1
# for posicao in alfabeto:
#     if letra.upper() == posicao:
#         print(I)
#     else:
#         I += 1

while True: 
    perna = input("Qual perna levantar?: ")
    try: 
           # TODO:  Programe aqui dentro as condições necessárias para satisfazer o problema
           # e imprima a saída de acordo com a situação das pernas do papagaio
        if perna == "esquerda":
            print("ingles")
            break
        elif perna == "direita":
            print("frances")
            break
        elif perna == "ambas":
            print("caiu")
            break
        else:
            print("portugues")
            break
    except EOFError: 
        break

