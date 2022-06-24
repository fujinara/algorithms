def moveZeros(arr):
    i, j = 0, 0
    while j < len(arr):
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
        else:
            j += 1
    return arr