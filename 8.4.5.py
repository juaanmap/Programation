def binary_search_insert(lst, element):
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == element:
            return mid
        elif lst[mid] < element:
            left = mid + 1
        else:
            right = mid - 1

    lst.insert(left, element)
    return left

