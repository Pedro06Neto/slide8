dicionario_sentimentos = {
    "alegria": "Positivo",
    "tristeza": "Negativo",
    "entusiasmo": "Positivo",
    "raiva": "Negativo",
    "confusão": "Neutro"
}

lista = ["feliz", "amei", "feliz", "triste", "raiva", "triste",
         "fome", "preguiça", "desmotivado", "feliz"]

positivos = 0
negativos = 0
neutros = 0
nao_identificados = 0

for palavra in lista:
    resultado = dicionario_sentimentos.get(palavra.lower().strip(), None)
    if resultado == "Positivo":
        positivos += 1
    elif resultado == "Negativo":
        negativos += 1
    elif resultado == "Neutro":
        neutros += 1
    else:
        nao_identificados += 1

print("--- Resultado da Análise da Lista ---")
print(f"Positivas : {positivos}")
print(f"Negativas : {negativos}")
print(f"Neutras   : {neutros}")
print(f"Não identificadas: {nao_identificados}")


#--- Resultado da Análise da Lista ---
#Negativas : 2
#Neutras   : 0
#Não identificadas: 8