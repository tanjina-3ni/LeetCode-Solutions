class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        L = [[1],[1,1]]
        for i in range(0,rowIndex+1):
            l = [1]*(i+1)

            if i>1:
                for j in range(1,len(l)-1):
                    l[j] = L[i-1][j-1]+L[i-1][j]
                L.append(l)
        return L[rowIndex]