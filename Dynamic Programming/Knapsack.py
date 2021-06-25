def knapsack_recursion(m, w, v, n):
    # BASE CASE
    if m == 0 or n == 0:
        return 0
    if w[n-1] > m:
        return knapsack_recursion(m, w, v, n-1)
    else:
        return max(knapsack_recursion(m, w, v, n-1), v[n-1] + knapsack_recursion(m-w[n-1], w, v, n-1))
print(knapsack_recursion(10, [2, 4, 5], [5, 6, 7], 3))