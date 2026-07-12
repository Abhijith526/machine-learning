def find_pairs():
    ls = [2, 7, 4, 1, 3, 6]
    ls.sort()

    pairs = []
    i = 0
    j = len(ls) - 1

    while i < j:
        if ls[i] + ls[j] == 10:
            pairs.append((ls[i], ls[j]))
            i += 1
            j -= 1
        elif ls[i] + ls[j] < 10:
            i += 1
        else:
            j -= 1

    return pairs


print(len(find_pairs()))
print(find_pairs())