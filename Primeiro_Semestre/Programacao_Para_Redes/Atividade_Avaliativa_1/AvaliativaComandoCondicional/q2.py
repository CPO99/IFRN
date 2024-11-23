print("VERIFICANDO SITUAÇÃO DE MEDIA EM DISCIPLINA\n")

N1 = float(input("Informe a nota 1: "))
N2 = float(input("Informe a nota 2: "))


MEDIA = (2*N1 + 3*N2) / 5 #primeiro calculo da media

SITUACAO = "APROVADO" #considerando por padrão como aprovado

if 20<=MEDIA<60: #verificando se a media necessita de prova final
    print("\nMEDIA ATUAL:",MEDIA)
    NF = float(input("\nInforme a nota da prova final: "))
    MDF1 = (MEDIA + NF) / 2

    MDF2 = (2*NF + 3*N2) / 5

    MDF3 = (2*N1 + 3*NF) / 5

    if MDF1 > MDF2 and MDF1 > MDF3: #segundo calculo de media
        MEDIA = MDF1
    elif MDF2 > MDF1 and MDF2 > MDF3: #terceiro calculo de media
        MEDIA = MDF2
    else:
        MEDIA = MDF3

    if MEDIA < 60:
        SITUACAO = "REPROVADO"
elif 20>MEDIA: #reprovação direta, primeira media abaixo de 20
    SITUACAO = "REPROVADO"

print("\nSituação:",SITUACAO)
print("Media final:",MEDIA)
