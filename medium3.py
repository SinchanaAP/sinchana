def maximalSquare(matrix):
    if not matrix or not matrix[0]:
        return 0

    m, n = len(matrix), len(matrix[0])
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    # Variable to track the maximum side length of the square submatrix
    max_side = 0
    # Iterate through the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if matrix[i - 1][j - 1] == '1':
                # If the current element is '1', update the dp array
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                max_side = max(max_side, dp[i][j])
     # The result is the area of the largest square (side length squared)
    return max_side * max_side

# Get user input for the matrix
rows = int(input("Enter the number of rows in the matrix: "))
cols = int(input("Enter the number of columns in the matrix: "))

matrix = []
for i in range(rows):
    row = input("Enter row {i + 1}): ").split()
    matrix.append(row)

# Call the function with the user-input matrix and print the result
output = maximalSquare(matrix)

print("Output:", output)
