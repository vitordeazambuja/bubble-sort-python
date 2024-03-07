import random

arraySmall = [random.randint(0, 100) for _ in range(10)]
arrayLarge = [random.randint(0, 100) for _ in range(100)]
arrayLarger = [random.randint(0, 100) for _ in range(1000)]
arrayLargest = [random.randint(0, 100) for _ in range(10000)]


def bubble_sort(number):
    n = len(number)

    for i in range(n - 1):
        for j in range(0, n - 1 - i):
            if number[j] > number[j + 1]:
                aux = number[j]
                number[j] = number[j + 1]
                number[j + 1] = aux


bubble_sort(arraySmall)
print(arraySmall)
