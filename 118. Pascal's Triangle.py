class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        L = [[1]]
        if numRows == 1:
            print(L)

        for i in range(1,numRows):
            l = [1]*(i+1)

            if i==1:
                L.append(l)

            else:
                for j in range(1,len(l)-1):
                    l[j] = L[i-1][j-1]+L[i-1][j]
                L.append(l)
        return L
            