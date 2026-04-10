def is_subset_sum(set, n, sum):
    # The value of subset[i][j] will be
    # true if there is a subset of
    # set[0..j-1] with sum equal to i
    subset = ([[False for i in range(sum + 1)]
            for i in range(n + 1)])

    # If sum is 0, then answer is true
    for i in range(n + 1):
        subset[i][0] = True

    # If sum is not 0 and set is empty,
    # then answer is false
    for i in range(1, sum + 1):
        subset[0][i] = False

    # Fill the subset table in bottom up manner
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if j < set[i-1]:
                subset[i][j] = subset[i-1][j]
            if j >= set[i-1]:
                subset[i][j] = (subset[i-1][j] or
                                subset[i-1][j-set[i-1]])

    # Find the subsets
    if not subset[n][sum]:
        print("No subset with given sum")
        return

    result = []
    def find_subsets(i, j, current_subset):
        if i == 0 and j == 0:
            result.append(list(current_subset))
            return
        if subset[i-1][j]:
            find_subsets(i-1, j, current_subset)
        if j >= set[i-1] and subset[i-1][j-set[i-1]]:
            current_subset.append(set[i-1])
            find_subsets(i-1, j-set[i-1], current_subset)
            current_subset.pop()

    find_subsets(n, sum, [])
    print("Subsets with the given sum:", result)


if __name__ == '__main__':
    set = [3, 34, 4, 12, 5, 2]
    sum = 9
    n = len(set)
    is_subset_sum(set, n, sum)
