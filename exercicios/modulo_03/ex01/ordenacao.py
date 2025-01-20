# Bubble sort
def bubble_sort(lista):
    tamanho = len(lista)
    for j in range(tamanho-1):
        for i in range(tamanho-1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]

# Merge sort
def merge_sort(vetor, inicio=0, fim=None):
    if fim is None:
        fim = len(vetor)
    if (fim - inicio > 1):
        meio = (fim + inicio) // 2
        merge_sort(vetor, inicio, meio)
        merge_sort(vetor, meio, fim)
        merge(vetor, inicio, meio, fim)


def merge(vetor, inicio, meio, fim):
    left = vetor[inicio:meio]
    right = vetor[meio:fim]
    topo_left, topo_right = 0, 0
    for k in range(inicio, fim):
        if topo_left >= len(left):
            vetor[k] = right[topo_right]
            topo_right += 1
        elif topo_right >= len(right):
            vetor[k] = left[topo_left]
            topo_left += 1
        elif left[topo_left] < right [topo_right]:
            vetor[k] = left[topo_left]
            topo_left += 1
        else:
            vetor[k] = right[topo_right]
            topo_right += 1

# Selection sort
def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista
