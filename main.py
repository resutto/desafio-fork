import math


# Função para calcular a média
def calcular_media(lista):
    # TODO: implementar a soma dos elementos e dividir pelo tamanho da lista
    media = 0
    itens = len(lista)
    for i in range(len(lista)):
        media = media + int(lista[i])
    return media / itens


# Função para calcular a mediana
def calcular_mediana(lista):
    lista.sort()
    if len(lista) % 2 == 0:
        numero1 = lista[math.ceil(len(lista) / 2) - 1]
        numero2 = lista[(math.ceil(len(lista) / 2))]
        return (numero1 + numero2) / 2
    else:
        return lista[math.ceil(len(lista) / 2) - 1]
    # TODO: ordenar a lista e encontrar o elemento do meio
    # 💡 Dica: se o tamanho for par, tire a média dos dois elementos centrais


# Função para calcular a moda
def calcular_moda(lista):
    lista1 = []
    lista.sort()
    for i in range(len(lista)):
        lista1.append(lista.count(lista[i]))
    maior = 0
    posicao = 0
    for i in range(len(lista1)):
        if lista1[i] > maior:
            maior = lista1[i]
            posicao = i

    return lista[posicao]
    # TODO: encontrar o valor que mais aparece
    # 💡 Dica: use um dicionário para contar as ocorrências


def main():
    try:
        numeros = [10, 20, 20, 30, 40, 40, 40, 50]
        print("📊 Calculadora Estatística")
        calcular_media(numeros)
        # print(numeros)
        # print(f"Lista de números: {numeros}")
        print(f"Média: {calcular_media(numeros)}")
        print(f"Mediana: {calcular_mediana(numeros)}")
        print(f"Moda: {calcular_moda(numeros)}")
    except Exception as e:
        print(f"⚠️ Ocorreu um erro: {e}")


if __name__ == "__main__":
    main()
