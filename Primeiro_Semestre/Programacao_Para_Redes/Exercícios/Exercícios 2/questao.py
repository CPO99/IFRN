from datetime import datetime

print("ANALISANDO ARQUIVO DE LOG\n")

log = open("apache_logs.txt", "r")

hd = {}

for i in log:
    posInicio = i.find("[")
    posFim = i.find("]", posInicio+1)
    
    data_hora = i[posInicio+1:posFim]
    
    ano = data_hora[data_hora.find("/",data_hora.find("/") + 1) + 1:data_hora.find(":")] 
    mes = 5 if data_hora[data_hora.find("/") + 1:data_hora.find("/",data_hora.find("/") + 1)] == "May" else 0
    dia = data_hora[0:2]
    hora = data_hora[data_hora.find(":") + 1:data_hora.find(":", data_hora.find(":") + 1)]
    minuto = data_hora[data_hora.find(":", data_hora.find(":") + 1) + 1:data_hora.find(":", data_hora.find(":") + 1) + 3]
    print(minuto)

    """
    

    hd[]
    print(quase)
    """
