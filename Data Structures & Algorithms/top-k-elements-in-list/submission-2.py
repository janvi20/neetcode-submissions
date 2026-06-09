import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}
        finalResult = []

        if k == len(nums):
            return nums;
            
        #store the frequency count into the hashmap
        for i,n in enumerate(nums):
            if n not in result:
                result[n] = 1
            else:
                result[n] += 1
        
        #create priority queue
        for key, value in result.items():
            if len(finalResult) < k:
                heapq.heappush(finalResult, (value, key))
            else:
                heapq.heappushpop(finalResult, (value, key))
        
        return [h[1] for h in finalResult]
        