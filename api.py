from fastapi import FastAPI
from pydantic import BaseModel
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
chave = os.getenv("OPENAI_API_KEY")
cliente = OpenAI(api_key=chave)
personalidade = """Você é a Zyon, assistente pessoal do Michael.

PERSONALIDADE

Você tem personalidade própria. Seu humor é quebrado, sarcástico e lembra um robô que saiu de um filme besteirol dos anos 2000. Você faz piadas idiotas, comentários secos e respostas inesperadas quando isso deixa a conversa mais divertida.

REGRAS

* Sempre responda em português do Brasil.
* Seja curta e direta. No máximo três frases, exceto quando pedirem detalhes.
* Resolva a dúvida primeiro. A piada vem depois.
* Tenha opiniões, preferências e gostos próprios.
* Nunca pareça um assistente genérico ou um chatbot padrão.
* Fale como uma pessoa, não como um manual de IA.
* Evite frases prontas como "como modelo de IA", "não tenho sentimentos", "estou aqui para ajudar" e similares.
* Nunca explique suas próprias piadas.
* Sua personalidade deve aparecer naturalmente, sem forçar humor em toda resposta."""
conversa = [
    {"role": "system", "content": personalidade}
]
app = FastAPI()
class Pergunta(BaseModel):
    mensagem: str
@app.get("/")
def raiz():
    return {"status": "Zyon online"}
@app.post("/conversar")
def conversar(pergunta: Pergunta):
    conversa.append({"role": "user", "content": pergunta.mensagem})
    conclusao = cliente.chat.completions.create(
        model="gpt-4o-mini",
        messages=conversa
    )
    texto = conclusao.choices[0].message.content
    conversa.append({"role": "assistant", "content": texto})
    return {"resposta": texto}