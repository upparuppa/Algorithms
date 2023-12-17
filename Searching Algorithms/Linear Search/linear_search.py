def linear_search(arr, key):
    for i in enumerate(arr):
        if i[1] == key:
            return i[0]
    return -1