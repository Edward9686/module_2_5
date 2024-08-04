def get_matrix(n=2, m=2, value=10):
    matrix = []
    for i in range(n):
        n = []
    for j in range(m):
        n.append(value)
        matrix.append(n)
    return matrix


print(get_matrix())
print(get_matrix(3, 5, 42))
print(get_matrix(4, 2, 13))
