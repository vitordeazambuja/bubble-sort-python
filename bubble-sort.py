import random
import matplotlib.pyplot as plt
import time

def bubble_sort(number):
    n = len(number)

    for i in range(n - 1):
        for j in range(0, n - 1 - i):
            if number[j] > number[j + 1]:
                aux = number[j]
                number[j] = number[j + 1]
                number[j + 1] = aux

def measure_time(array):
    start_time = time.time()
    bubble_sort(array)
    end_time = time.time()
    return end_time - start_time

# Criação das listas
sizes = [10, 100, 1000, 10000]
times = []

for size in sizes:
    array = [random.randint(0, 100) for _ in range(size)]
    times.append(measure_time(array))

# Leitura de arquivo
with open("arquivo.txt", "r") as arquivo:
    linhas = arquivo.readlines()

# Criação da lista do arquivo
arquivo_array = [int(linha.strip()) for linha in linhas]
arquivo_time = measure_time(arquivo_array)
sizes.append(len(arquivo_array))
times.append(arquivo_time)

# Plotagem do gráfico
plt.plot(sizes, times, marker='o')
plt.title('Desempenho do Bubble Sort')
plt.xlabel('Tamanho do Array')
plt.ylabel('Tempo de Execução (s)')
plt.grid(True)
plt.show()
