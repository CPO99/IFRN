print("CALCULANDO O IMC\n")

P = float(input("Informe o seu peso (kg): "))
A = float(input("Informe a sua altura (cm): "))

IMC = round(P / (A / 100)**2, 2) #calculo do IMC, a razão do peso pelo quadrado da altura

print("\nIMC calculado:",IMC,"\n")

print("SITUAÇÃO\n")

if IMC <= 18.5:
    print("- Abaixo do peso: Procure um médico. Algumas pessoas têm um baixo peso por características do seu organismo e tudo bem. Outras podem estar enfrentando problemas, como a desnutrição. É preciso saber qual é o caso.")
elif 18.5<IMC<=24.9:
    print("- Normal: Que bom que você está com o peso normal! E o melhor jeito de continuar assim é mantendo um estilo de vida ativo e uma alimentação equilibrada.")
elif 24.9<IMC<=29.9:
    print("- Sobrepeso: Ele é, na verdade, uma pré-obesidade e muitas pessoas nessa faixa já apresentam doenças associadas, como diabetes e hipertensão. Importante rever hábitos e buscar ajuda antes de, por uma série de fatores, entrar na faixa da obesidade pra valer.")
elif 29.9<IMC<=34.9:
    print("- Obesidade grau I: Sinal de alerta! Chegou na hora de se cuidar, mesmo que seus exames sejam normais. Vamos dar início a mudanças hoje! Cuide de sua alimentação. Você precisa iniciar um acompanhamento com nutricionista e/ou endocrinologista.")
elif 34.9<IMC<=39.9:
    print("- Obesidade grau II: Mesmo que seus exames aparentem estar normais, é hora de se cuidar, iniciando mudanças no estilo de vida com o acompanhamento próximo de profissionais de saúde.")
else:
    print("- Obesidade grau III: Aqui o sinal é vermelho, com forte probabilidade de já existirem doenças muito graves associadas. O tratamento deve ser ainda mais urgente.")
