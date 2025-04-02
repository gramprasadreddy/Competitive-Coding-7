#   https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        pq = []
        n = len(matrix)

        for i in range (n):
            for j in range(n):
                heapq.heappush(pq,-matrix[i][j])

                if (len(pq) > k):
                    heapq.heappop(pq)
        
        ans  = -heapq.heappop(pq)
        return ans

# TC: O(n^2 logk) 
# SC O(k)

#####################################   

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)        
        pq = []

        for i in range(n):
            heapq.heappush(pq,(matrix[i][0],i,0))
        
        for i in range(k):
            val,r,c = heapq.heappop(pq)
            if c+1 < n:
                heapq.heappush(pq,(matrix[r][c+1],r,c+1))
        
        return val

# TC: O(k log k) here I dont have to iterate over all the entries in matrix
# the matrix is row wise and col wise sorted so put the first row into heap first
# and then for upto k elements pop. lat ele is the ans

# SC: O(k)


########################################################################

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ans=-1
        left = matrix[0][0]
        n = len(matrix)
        right = matrix[n-1][n-1]
        while left <= right:
            mid = left + (right - left)//2
            if self.count_n(matrix,mid) >=k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans

    def count_n(self,matrix,mid):
        r = len(matrix)
        c = len(matrix[0])-1
        count = 0

        for i in range(r):
            while c >= 0 and matrix[i][c] > mid:
                c-=1
            count += (c + 1)

        return count

# BS TC: O(n log(max-min))
# SC: O(1)