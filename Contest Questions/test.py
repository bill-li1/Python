def binary_search(L, target):
    beginning = 0
    end = len(L) - 1
    while beginning <= end:
        mid = (beginning + end) // 2
        print(mid)
        if L[mid] == target:
            return True
        elif L[mid] > target:
            end = mid
        else:
            beginning = mid + 1
    return False


def sum_pair(L):
    total = 0
    for i in range(len(L)):
        total += L[i]
    if total % 2 != 0:
        return None
    total //= 2
    for i in range(len(L)):
        missing = total - L[i]
        if binary_search(L, missing):
            if L[i] > missing:
                return [missing, L[i]]
            else:
                return [L[i], missing]
    return None

print(sum_pair([1, 10, 5, 2, 4, 8]))
