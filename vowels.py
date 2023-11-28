def count_sorted_vowel_strings(n):
    dp = [[0] * 5 for _ in range(n + 1)]
    for j in range(5):
        dp[1][j] = 1
        for i in range(2, n + 1):
            for j in range(5):
                dp[i][j] = sum(dp[i - 1][k] for k in range(j + 1))
                result = sum(dp[n])
    return result
n = 2
result = count_sorted_vowel_strings(n)
print(f"The number of lexicographically sorted vowel strings of length {n} is: {result}")

 
