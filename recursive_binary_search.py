def recursive_binary_search(lst, target):
    if len(lst) == 0:
        return False
    else:
        mdipoint = (len(lst)) // 2

        if lst[mdipoint] == target:
            return True
        else:
            if lst[mdipoint] < target:
                return recursive_binary_search(lst[mdipoint + 1:], target)
            else:
                return recursive_binary_search(lst[:mdipoint], target)


def verify(result):
    print("Target found ", result)


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = recursive_binary_search(numbers, 12)
verify(result)

result = recursive_binary_search(numbers, 6)
verify(result)
