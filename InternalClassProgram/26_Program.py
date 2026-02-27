def find_median(arr):
    arr.sort()
    n = len(arr)

    mid = n // 2

    if n % 2 == 1:
        return arr[mid]
    else:
        return (arr[mid - 1] + arr[mid]) / 2