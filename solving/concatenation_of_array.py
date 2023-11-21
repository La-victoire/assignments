class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans: list[int] = []

        # Your code goes here.
        ans = []
        for num in nums:
            ans.append(num)
        for num in nums:
            ans.append(num)
 
        return ans
