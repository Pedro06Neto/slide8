dicionario_sentimentos = {
    "alegria": "Positivo",
    "tristeza": "Negativo",
    "entusiasmo": "Positivo",
    "raiva": "Negativo",
    "confusão": "Neutro"
}

print("--- Analisador de Emoções ---")
print(f"Sentimentos já conhecidos: {list(dicionario_sentimentos.keys())}")

palavra = input("\nDigite uma palavra para análise: ").lower().strip()

resultado = dicionario_sentimentos.get(palavra, None)

if resultado:
    print(f"\nA palavra '{palavra}' tem o sentimento: {resultado}")
else:
    print(f"\nSentimento não identificado no dicionário.")
    inserir = input("Deseja inserir este sentimento? (sim/não): ").lower().strip()
    if inserir == "sim":
        valor = input("Qual o valor (positivo, negativo, neutro): ").lower().strip()
        dicionario_sentimentos[palavra] = valor.capitalize()
        print(f"'{palavra}' inserido com sucesso!")

print("\n--- Conhecimento Atual da IA ---")
for termo, sent in dicionario_sentimentos.items():
    print(f"* {termo}: {sent}")