import sys

def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0 for x in range(n)] for x in range(n)]
    s = [[0 for x in range(n)] for x in range(n)]

    for i in range(n):
        m[i][i] = 0

    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            m[i][j] = sys.maxsize
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    return m[0][n - 1], s

def print_optimal_parens(s, i, j):
    if i == j:
        print(f"A{i+1}", end="")
    else:
        print("(", end="")
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j)
        print(")", end="")

if __name__ == '__main__':
    # Dimensions of matrices
    p = [10, 30, 5, 60]
    
    min_multiplications, s_matrix = matrix_chain_order(p)
    
    print("Matrix dimensions:", p)
    print("Minimum number of scalar multiplications:", min_multiplications)
    print("Optimal parenthesization:", end=" ")
    print_optimal_parens(s_matrix, 0, len(p)-2)
    print()
