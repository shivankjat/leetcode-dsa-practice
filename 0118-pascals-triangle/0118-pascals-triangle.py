class Solution:
    def nCr(n, r):
        res = 1
        for i in range(r):
            res = res * (n - i)
            res = res // (i + 1)
        return int(res)

    def generate(self, numRows):
        n = numRows
        ans = []
        for row in range(1, n + 1):
            tempLST = []
            for col in range(1, row + 1):
                tempLST.append(Solution.nCr(row - 1, col - 1))  # Call using class name
            ans.append(tempLST)
        return ans