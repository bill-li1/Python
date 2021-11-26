from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        index = 0
        for num in nums:
            missing = target-num
            if missing in hashmap:
                return [hashmap[missing], index]
            hashmap[num] = index
            index += 1
        return []

