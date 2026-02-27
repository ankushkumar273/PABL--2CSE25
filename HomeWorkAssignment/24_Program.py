def min_swaps_to_group(arr, k):
    n = len(arr)

    # Count elements <= k
    window_size = sum(1 for x in arr if x <= k)

    # If no or all elements satisfy condition
    if window_size == 0 or window_size == n:
        return 0

    # Count bad elements in first window
    bad = sum(1 for i in range(window_size) if arr[i] > k)

    min_swaps = bad

    # Slide the window
    for i in range(window_size, n):
        if arr[i] > k:
            bad += 1
        if arr[i - window_size] > k:
            bad -= 1

        min_swaps = min(min_swaps, bad)

    return min_swaps