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


