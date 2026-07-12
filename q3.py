def multiply(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    return C


n = int(input("Enter the order of the matrix: "))

print("Enter the matrix:")
A = [list(map(int, input().split())) for _ in range(n)]

m = int(input("Enter the power: "))

# Identity matrix
result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

# Compute A^m
for _ in range(m):
    result = multiply(result, A)

print(f"A^{m} =")
for row in result:
    print(*row)