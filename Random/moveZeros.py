def moveZeros(arr):
    i, j = 0, 0
    n = len(arr)
    while j < n:
        if arr[j] != 0:
            arr[i] = arr[j]
            i += 1
            j += 1
        else:
            j += 1
    while i < n:
        arr[i] = 0
        i += 1
    return arr