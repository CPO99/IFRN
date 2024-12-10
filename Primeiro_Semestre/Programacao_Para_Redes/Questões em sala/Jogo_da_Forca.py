import random

print("----------------------")
print("    JOGO DA FORCA")
print("----------------------\n")

PALAVRAS = ["ABACATE", "ABACAXI",
            "MARACUJA", "MANGA",
            "GOIABA"]

SORT = random.choice(PALAVRAS)

CONT = 0
CONT2 = 0

PALPITE_LETRAS = []

print("➜ PALAVRA:","-" * len(SORT), end="")

while CONT < len(SORT):
    LETRA = input("\n\nInforme uma letra: ")

    if LETRA in PALPITE_LETRAS:
        print("\nLETRA JÁ INFORMADA ANTERIORMENTE, TENTE NOVAMENTE...", end="")
    else:
        print("\n➜ PALAVRA: ",end="")
        PALPITE_LETRAS.append(LETRA)

        CONT2 = 0
        
        for i in SORT:
            if i in PALPITE_LETRAS:
                print(i,end="")
                CONT2 += 1
            else:
                print("-",end="")

        if CONT2 == len(SORT):
            print("\n\nPARABÉNS!!! VOCÊ CONCLUIU!")
            break
        
    

