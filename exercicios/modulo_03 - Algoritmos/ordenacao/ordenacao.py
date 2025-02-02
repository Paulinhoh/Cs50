# Bubble sort
def bubble_sort(lista:list) -> None:
    tamanho:int = len(lista)
    for j in range(tamanho-1):
        for i in range(tamanho-1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]

# Merge sort
def merge_sort(vetor:list, inicio:int=0, fim:int=None) -> None:
    if fim is None:
        fim = len(vetor)
    if (fim - inicio > 1):
        meio:int = (fim + inicio) // 2
        merge_sort(vetor, inicio, meio)
        merge_sort(vetor, meio, fim)
        merge(vetor, inicio, meio, fim)


def merge(vetor:list, inicio:int, meio:int, fim:int) -> None:
    left:list = vetor[inicio:meio]
    right:list = vetor[meio:fim]
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
def selection_sort(lista:list) -> list:
    tamanho:int = len(lista)
    for i in range(tamanho):
        min_index = i
        for j in range(i + 1, tamanho):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista
