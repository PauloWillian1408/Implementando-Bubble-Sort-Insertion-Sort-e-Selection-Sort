import random
import time

# Função Selection Sort (ordem decrescente)
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        max_idx = i
        for j in range(i+1, n):
            if arr[j] > arr[max_idx]:  # Alteração para ordem decrescente
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr

# Função Bubble Sort (ordem decrescente)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j+1]:  # Alteração para ordem decrescente
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Função Insertion Sort (ordem decrescente)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:  # Alteração para ordem decrescente
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

# Função para medir o tempo de execução
def medir_tempo(algoritmo, arr):
    inicio = time.time()
    algoritmo(arr)
    fim = time.time()
    return fim - inicio

# Testar com arrays de diferentes tamanhos
tamanhos = [10, 100, 1000]
for tamanho in tamanhos:
    print(f"\nArray com {tamanho} elementos:")
    array = [random.randint(1, 1000) for _ in range(tamanho)]

    # Medir tempo para Selection Sort
    array_selection = array.copy()
    tempo_selection = medir_tempo(selection_sort, array_selection)
    print(f"Tempo do Selection Sort: {tempo_selection:.6f} segundos")
    print(f"Array ordenado (Selection Sort): {array_selection}")

    # Medir tempo para Bubble Sort
    array_bubble = array.copy()
    tempo_bubble = medir_tempo(bubble_sort, array_bubble)
    print(f"Tempo do Bubble Sort: {tempo_bubble:.6f} segundos")
    print(f"Array ordenado (Bubble Sort): {array_bubble}")

    # Medir tempo para Insertion Sort
    array_insertion = array.copy()
    tempo_insertion = medir_tempo(insertion_sort, array_insertion)
    print(f"Tempo do Insertion Sort: {tempo_insertion:.6f} segundos")
    print(f"Array ordenado (Insertion Sort): {array_insertion}")
