class Solution:
    def missingNum(self, arr):
        # code here
        n = len(arr)
        
        actual_sum = (n+1)*(n+2)// 2
        
        curr_sum = sum(arr)
        
        return actual_sum - curr_sum