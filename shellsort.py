def shellSort(collection):
    gap = len(collection) // 2

    while gap > 0:
        print(collection)
        for i in range(gap, len(collection)):
            var = collection[i]
            j = i
            while j >= gap and collection[j - gap] > var:
                collection[j] = collection[j - gap]
                j -= gap
            collection[j] = var
        gap //= 2
    return collection

a = [8,5,6,3,10,21,3,2]
print(shellSort(a))
