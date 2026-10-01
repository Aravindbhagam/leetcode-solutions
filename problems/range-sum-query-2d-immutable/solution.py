class NumMatrix:

    def __init__(self, matrix):
        if not matrix or not matrix[0]:
            return
        
        m, n = len(matrix), len(matrix[0])
        self.pre = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.pre[i][j] = (
                    matrix[i-1][j-1]
                    + self.pre[i-1][j]
                    + self.pre[i][j-1]
                    - self.pre[i-1][j-1]
                )

    def sumRegion(self, row1, col1, row2, col2):
        return (
            self.pre[row2 + 1][col2 + 1]
            - self.pre[row1][col2 + 1]
            - self.pre[row2 + 1][col1]
            + self.pre[row1][col1]
        )
