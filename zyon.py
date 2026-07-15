import random
import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
chave = os.getenv("OPENAI_API_KEY")
cliente = OpenAI(api_key=chave)
print("Zyon online.")
respostas = ["Interessante.", "Sei...", "Conta mais.", "Uhum, sei."]
while True:
    mensagem = input("Voce: ").strip()
    if mensagem.lower() == "sair":
        print("Zyon: Ja vai? Tinha acabado de ficar interessante.")
        break
    conclusao = cliente.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": mensagem}
        ]
    )
    texto = conclusao.choices[0].message.content
    print(f"Zyon: {texto}")


