def merge_sort_iterative(data):
    n = len(data)
    width = 1
    while width < n:
        for i in range(0, n, 2 * width):
            left = data[i:i + width]
            right = data[i + width:i + 2 * width]
            merged = merge(left, right)
            data[i:i + len(merged)] = merged
        width *= 2

def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged

if __name__ == "__main__":
    data = [38, 27, 43, 3, 9, 82, 10]
    print("Original data:", data)
    merge_sort_iterative(data)
    print("Sorted data:", data)
