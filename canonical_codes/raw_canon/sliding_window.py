class Solution:
    
    def longest_string(self, s):
        
        # Step 1: Initialize - Dict for Subset

        letters = {}
        ans = 0
        i = 0
        j = 0

        # Step 2: While neither pointer hits end
        while i < len(s) and j < len(s):

            # Step 3: New letter? Add, move j up, save max
            if s[j] not in letters:
                letters[s[j]] = 1
                ans = max(ans, j-i+1)
                j += 1
            # Step 4: Not new? Remove letter of and move up first pointer
            else:
                letters.pop(s[i], None)
                i += 1
            #print((i,j,ans, letters))

        return ans


a = Solution()
#s = 'abcabcbb'
s = 'bbbbbb'
print(a.longest_string(s))