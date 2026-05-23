meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "una respuesta a una broma",
            "SHEESH": "ligera desaprobación",
            "CREEPY": "aterrador, siniestro",
            "AGGRO": "ponerse agresivo/enojado"
            }

print("¡Hola!, este es un programa para ayudarte mejor a entender la jerga adolecente actual. Para usarlo, simplemente escribe la palabra que no entiendas que significa en mayusculas, ejemplo: LOL. Sin mas decir, espero que les sirva")

print("-----------------------------------------------")
for i in range(5):
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("ERROR: ¡no se encontro la palabra!")
