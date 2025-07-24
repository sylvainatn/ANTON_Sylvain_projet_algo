def tri_selection(tab):
    n = len(tab)
    comparaisons = 0
    echanges = 0
    arr = tab.copy()
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            comparaisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            echanges += 1
    return arr, comparaisons, echanges


def tri_insertion(tab):
    n = len(tab)
    comparaisons = 0
    decalages = 0
    arr = tab.copy()
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            comparaisons += 1
            arr[j + 1] = arr[j]
            decalages += 1
            j -= 1
        # Pour la dernière comparaison qui fait sortir de la boucle
        if j >= 0:
            comparaisons += 1
        arr[j + 1] = key
        decalages += 1
    return arr, comparaisons, decalages


def tri_fusion(tab):
    arr = tab.copy()
    comparaisons = [0]
    def fusion(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            comparaisons[0] += 1
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    def merge_sort(lst):
        if len(lst) <= 1:
            return lst
        mid = len(lst) // 2
        left = merge_sort(lst[:mid])
        right = merge_sort(lst[mid:])
        return fusion(left, right)
    sorted_arr = merge_sort(arr)
    return sorted_arr, comparaisons[0]


def tri_rapide(tab):
    arr = tab.copy()
    comparaisons = [0]
    echanges = [0]
    def quick_sort(lst):
        if len(lst) <= 1:
            return lst
        pivot = lst[0]
        left = []
        right = []
        for x in lst[1:]:
            comparaisons[0] += 1
            if x < pivot:
                left.append(x)
            else:
                right.append(x)
        # Compter l'échange du pivot (sauf si déjà à sa place)
        if len(left) > 0 or len(right) > 0:
            echanges[0] += 1
        return quick_sort(left) + [pivot] + quick_sort(right)
    sorted_arr = quick_sort(arr)
    return sorted_arr, comparaisons[0], echanges[0]
