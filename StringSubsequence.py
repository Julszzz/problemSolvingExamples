def count_subsequence(text, pattern):
    """
    Counts the number of times 'pattern' occurs as a subsequence in 'text'.

    Args:
        text: The string to search within.
        pattern: The subsequence to count.

    Returns:
        The number of occurrences of 'pattern' as a subsequence in 'text'.
    """
    text_len = len(text)
    pattern_len = len(pattern)

    # Initialize a 2D DP array to store counts
    dp = [[0] * (pattern_len + 1) for _ in range(text_len + 1)]

    # Base case: empty pattern occurs once in any string
    for i in range(text_len + 1):
        dp[i][0] = 1

    # Iterate through the text and pattern
    for i in range(1, text_len + 1):
        for j in range(1, pattern_len + 1):
            # If characters match, add count with and without the character
            if text[i - 1] == pattern[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            # If characters don't match, count is same as without the character
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[text_len][pattern_len]

print(count_subsequence('HERHRWS', 'HRW'))