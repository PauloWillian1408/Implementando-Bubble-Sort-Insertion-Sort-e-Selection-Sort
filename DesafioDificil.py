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

# Testar os algoritmos em diferentes tipos de arrays
tamanhos = [10, 100, 1000]
for tamanho in tamanhos:
    print(f"\nTestando com arrays de tamanho {tamanho}:")

    # Totalmente desordenado
    array_desordenado = [random.randint(1, 1000) for _ in range(tamanho)]
    print("\nArray totalmente desordenado:")
    print(array_desordenado)
    array_selection = array_desordenado.copy()
    tempo_selection = medir_tempo(selection_sort, array_selection)
    print(f"Selection Sort: {tempo_selection:.6f} segundos")

    array_bubble = array_desordenado.copy()
    tempo_bubble = medir_tempo(bubble_sort, array_bubble)
    print(f"Bubble Sort: {tempo_bubble:.6f} segundos")

    array_insertion = array_desordenado.copy()
    tempo_insertion = medir_tempo(insertion_sort, array_insertion)
    print(f"Insertion Sort: {tempo_insertion:.6f} segundos")

    # Já ordenado
    array_ordenado = sorted(array_desordenado, reverse=True)
    print("\nArray já ordenado:")
    print(array_ordenado)
    array_selection = array_ordenado.copy()
    tempo_selection = medir_tempo(selection_sort, array_selection)
    print(f"Selection Sort: {tempo_selection:.6f} segundos")

    array_bubble = array_ordenado.copy()
    tempo_bubble = medir_tempo(bubble_sort, array_bubble)
    print(f"Bubble Sort: {tempo_bubble:.6f} segundos")

    array_insertion = array_ordenado.copy()
    tempo_insertion = medir_tempo(insertion_sort, array_insertion)
    print(f"Insertion Sort: {tempo_insertion:.6f} segundos")

    # Parcialmente ordenado (5 primeiros fora de ordem)
    array_parcialmente_ordenado = array_ordenado.copy()
    random.shuffle(array_parcialmente_ordenado[:5])  # Embaralha os 5 primeiros
    print("\nArray parcialmente ordenado (5 primeiros fora de ordem):")
    print(array_parcialmente_ordenado)
    array_selection = array_parcialmente_ordenado.copy()
    tempo_selection = medir_tempo(selection_sort, array_selection)
    print(f"Selection Sort: {tempo_selection:.6f} segundos")

    array_bubble = array_parcialmente_ordenado.copy()
    tempo_bubble = medir_tempo(bubble_sort, array_bubble)
    print(f"Bubble Sort: {tempo_bubble:.6f} segundos")

    array_insertion = array_parcialmente_ordenado.copy()
    tempo_insertion = medir_tempo(insertion_sort, array_insertion)
    print(f"Insertion Sort: {tempo_insertion:.6f} segundos")