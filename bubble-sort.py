import random
import matplotlib.pyplot as plt

# Criação das listas

# 35 ms
arraySmall = [random.randint(0, 100) for _ in range(10)]

# 34 ms
arrayLarge = [random.randint(0, 100) for _ in range(100)]

# 111 ms
arrayLarger = [random.randint(0, 100) for _ in range(1000)]

# 4842 ms
arrayLargest = [random.randint(0, 100) for _ in range(10000)]

# 92 ms
dinamicList = []

for i in range(1000):
    dinamicList.append(random.randint(0,1000))

# Leitura de arquivo
with open("arquivo.txt", "r") as arquivo:
  linhas = arquivo.readlines()
# Criação da lista do arquivo
# 170 ms
listaArquivo = [int(linha.strip()) for linha in linhas]


def bubble_sort(number):
    n = len(number)

    for i in range(n - 1):
        for j in range(0, n - 1 - i):
            if number[j] > number[j + 1]:
                aux = number[j]
                number[j] = number[j + 1]
                number[j + 1] = aux


bubble_sort(listaArquivo)
print(listaArquivo)

# Plotagem do gráfico