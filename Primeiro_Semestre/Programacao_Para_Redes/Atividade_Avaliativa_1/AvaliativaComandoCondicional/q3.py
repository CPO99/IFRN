import random

print("TENTANDO ADVINHAR NÚMERO EM ATÉ 4 TENTATIVAS\n")

try:
    SORT = random.randint(1, 100)

    INI = 1
    FIM = 100
    
    print("Intervalo para tentativa entre",INI,"e",FIM)
    N = int(input("Primeira tentativa: "))

    if INI > N or FIM < N:
        print("[ERRO] - Informar intervalo entre 1 e 100. Tente novamente!")
    else:
        if N == SORT:
            print("\nPARABÉNS!!! Você acertou de primeira")
        else:
            print("\n-------------------------------------------\n")
            print("Ainda não foi dessa vez... vamos para a segunda tentativa\n")
            if SORT > N:
                INI = N + 1
            else:
                FIM = N + 1 
                
            print("Intervalo para tentativa entre",INI,"e",FIM)

            N = int(input("Segunda tentativa: "))

            if INI > N or FIM<N:
                print("\n[ERRO] - Informar intervalo entre",INI,"e",FIM)
            else:
                if N == SORT:
                    print("\nPARABÉNS!!! Você acertou!")
                else:
                    print("\n-------------------------------------------\n")
                    print("Ainda não foi dessa vez... vamos para a terceira tentativa\n")
                    if SORT > N:
                        INI = N + 1
                    else:
                        FIM = N + 1
                    
                    print("Intervalo para tentativa entre",INI,"e",FIM)

                    N = int(input("Terceira tentativa: "))

                    if INI > N or FIM<N:
                        print("\n[ERRO] - Informar intervalo entre",INI,"e",FIM,"\n")
                    else:
                        if N == SORT:
                            print("\nPARABÉNS!!! Você acertou!")
                        else:
                            print("\n-------------------------------------------\n")
                            print("Ainda não foi dessa vez... vamos para a quarta tentativa\n")
                            if SORT > N:
                                INI = N + 1
                            else:
                                FIM = N + 1

                            print("Intervalo para tentativa entre",INI,"e",FIM)

                            N = int(input("Quarta tentativa: "))

                            if INI > N or FIM<N:
                                print("\n[ERRO] - Informar intervalo entre",INI,"e",FIM,"\n")
                            else:
                                if N == SORT:
                                    print("\nPARABÉNS!!! Você acertou!")
                                else:
                                    print("\n-------------------------------------------\n")
                                    print("SUAS TENTATIVAS ESGOTARAM! Sinto muito. O número sorteado era",SORT)               
except:
    print("\n[ERRO] - INFORME UM NÚMERO VÁLIDO")



