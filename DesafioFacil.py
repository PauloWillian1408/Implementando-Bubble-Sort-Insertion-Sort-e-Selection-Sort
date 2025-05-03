import random

# Função Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Função Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Função Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

# Gerar array aleatório
array = [random.randint(1, 50) for _ in range(10)]
print("Array original:", array)

# Ordenando com Selection Sort
array_selection = array.copy()
print("Selection Sort:", selection_sort(array_selection))

# Ordenando com Bubble Sort
array_bubble = array.copy()
print("Bubble Sort:", bubble_sort(array_bubble))

# Ordenando com Insertion Sort
array_insertion = array.copy()
print("Insertion Sort:", insertion_sort(array_insertion))