def range_mat(num):
    if len(num) < 3:
        return "Invalid input"

    return max(num) - min(num)


ls1 = list(map(int, input().split()))
print(range_mat(ls1))