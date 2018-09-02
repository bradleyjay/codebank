class algo:
    def maxSubArray(self, nums):
        """
        i: given some list of integers "nums"
        o: maximum sum of any subarray
        """
        S = []
        total = 0
        
        # Step 1: Compute rolling sum for all values in nums
        for i, val in enumerate(nums):
            total += nums[i]
            S.append(total)
        
        best = nums[0]
        
        # Step 2: Find max. Any subarray A[i,j] is then
        # S[j] - S[i-1], since they're sums, except when i
        # is 0. Then, the 'S[-1]' term should simply read 0,
        # as it's the total of no array terms.
        
        for i in range(0,len(nums)):
            for j in range(i, len(nums)):
                if i == 0:
                    A = S[j]
                else:
                    A = S[j] - S[i-1]
                
                if A > best:
                    best = A
                    
        return best