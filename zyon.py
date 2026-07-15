import random
print("Zyon online.")
respostas = ["Interessante.", "Sei...", "Conta mais.", "Uhum, sei."]
while True:
    mensagem = input("Voce: ").strip()
    if mensagem.lower() == "sair":
        print("Zyon: Ja vai? Tinha acabado de ficar interessante.")
        break
    resposta = random.choice(respostas)
    print(f"Zyon: {resposta}")


