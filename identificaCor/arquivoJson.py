import json

dataVermelho = {
    "Vermelho": [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
    ]
}

dataVerde = {
    "Verde": [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
    ]
}

dataLaranja = {
    "Laranja": [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
    ]
}

dataAzul = {
    "Azul": [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
    ]
}

dataBranco = {
    "Branco": [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
    ]
}

dataAmarelo = {
    "Amarelo": [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
    ]
}
def AdicionarJson(cor):
    if (cor == 0):
        data = dataVermelho
    elif (cor == 1):
        data = dataVerde
    elif (cor == 2):
        data = dataLaranja
    elif (cor == 3):
        data = dataAzul
    elif (cor == 4):
        data = dataBranco
    elif (cor == 5):
        data = dataAmarelo

    with open('cubo.json', 'w') as json_file:
        json.dump(data, json_file, indent=2)


cor=3
AdicionarJson(cor)


