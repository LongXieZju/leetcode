class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        def find(x):
            if x!= father[x]:
                father[x] = find(father[x])
            return father[x]
        
        def union(x, y):
            x, y = father[x], father[y]
            if x < y:
                father[x] = y
            else:
                father[y] = x

        length = len(row)
        father = [0]*length
        for i in range(0, length, 2):
            father[i] = i
            father[i+1] = i
        print(father)
        for i in range(0, length, 2):
            if find(row[i]) != find(row[i+1]):
                union(row[i], row[i+1])

        count = {}
        print(father)
        for i in range(len(father)):
            if find(i) in count.keys():
                count[find(i)] += 1
            else:
                count[find(i)] = 1

        print(count)
        res = 0
        for value in count.values():
            res += value/2-1

        return res

row = [5,3,4,2,1,0]    
s = Solution()
result = s.minSwapsCouples(row)
print(result)
