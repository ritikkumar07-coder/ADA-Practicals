def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    # To find which items are included
    res = K[n][W]
    w = W
    included_items = [0] * n
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == K[i-1][w]:
            continue
        else:
            included_items[i-1] = 1
            res = res - val[i-1]
            w = w - wt[i-1]

    return K[n][W], included_items

if __name__ == '__main__':
    profit = [60, 100, 120]
    weight = [10, 20, 30]
    W = 50
    n = len(profit)
    
    max_profit, vector = knapSack(W, weight, profit, n)
    
    print("Values:", profit)
    print("Weights:", weight)
    print("Knapsack capacity:", W)
    print("Maximum profit:", max_profit)
    print("Items included (vector):", vector)
