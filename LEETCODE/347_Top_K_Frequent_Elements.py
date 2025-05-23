class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        nums1 = set(nums)
        dict = {}
        
        # Initialize all unique elements with 0 frequency
        for num in nums1:
            dict[num] = 0

        # Count actual frequencies
        for i in range(len(nums)):
            dict[nums[i]] += 1

        # Sort the dictionary keys based on their values (frequencies)
        result = sorted(dict, key=dict.get, reverse=True)[:k]

        return result