#  https://leetcode.com/problems/meeting-rooms-ii/

# Time Complexity: O(n log n)
# Space Complexity: O(n)

def solve(Lists):
    pq = []
    for l in Lists:
        if len(pq) == 0:
            heapq.heappush(pq,l[1])
        elif pq[0] > l[0]:
            heapq.heappush(pq,l[1])
        else:
            heapq.heappop(pq)
            heapq.heappush(pq,l[1])
    
    print(len(pq))

#Lists = [[0,30],[5,10],[20,30]]
Lists = [[0,10],[5,25],[25,30],[20,25]]
Lists.sort()
print(Lists)
solve(Lists)
