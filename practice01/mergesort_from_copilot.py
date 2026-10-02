print("Hello, world!, 29 September, evening session")
def merge(left, right):
    merged = []
    i = j = 0

    # Merge until one list is exhausted
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Add leftovers
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def mergesort(lst):
    # Base case
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = mergesort(lst[:mid])
    right = mergesort(lst[mid:])

    return merge(left, right)


list_for_mergesort = [12, 13, 43, 62, 24, 51, 87, 69, 91, 3, 46, 53, 38, 99, 23,
                      72, 41, 85, 21, 73, 68, 52, 33, 28, 16, 19, 2, 94, 39]

sorted_list = mergesort(list_for_mergesort)
print(sorted_list)
