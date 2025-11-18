import requests
import html

def traduzir(texto):
    url = "https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=auto&tl=pt-BR&q=" + html.unescape(texto)
    r = requests.get(url)

    if r.status_code == 200:
        try:
            return r.json()[0][0]
        except:
            return texto
    return texto

print("=== JOGO DE TRIVIA ===")
print("Escolha a dificuldade:")
print("1 - Fácil")
print("2 - Médio")
print("3 - Difícil")


opc = input("Digite: ")

if opc == "1":
    dificuldade = "easy"
elif opc == "2":
    dificuldade = "medium"
elif opc == "3":
    dificuldade = "hard"
else:
    
    dificuldade = "medium"

url = f"https://opentdb.com/api.php?amount=5&difficulty={dificuldade}&type=multiple"
resp = requests.get(url)

dados = resp.json()["results"]

pontos = 0  
num = 1     