def find_pairs(arr, target):
    seen = set()
    pairs = []

    for num in arr:
        complement = target - num

        if complement in seen:
            pairs.append((complement, num))

        seen.add(num)

    return pairs


arr = [2, 4, 3, 5, 7, 8, 1]
target = 9

print(find_pairs(arr, target))