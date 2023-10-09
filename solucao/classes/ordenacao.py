def giraFace(face, sentido="antiorario", n=1):
    
    if sentido == "antiorario":
        for _ in range(n):
            # Transformar as linhas em colunas
            face = list(map(list, zip(*[list(reversed(linha)) for linha in face])))
    else:
        for _ in range(n):
            # Transformar as linhas em colunas sem inverter
            face = [list(linha) for linha in zip(*face[::-1])]

    return face

def ordena(cubo, ordem_leitura):
    for i, item in enumerate(ordem_leitura):
        sentido = 'antiorario'
        giros = 1

        if(i == 1):
            continue
        elif(i == 2):
            sentido = "horario"
        elif(i == 3):
            giros = 2

        cubo[item] = giraFace(cubo[item],  sentido, giros)
    return cubo