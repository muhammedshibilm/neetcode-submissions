class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_dict = {}
        flag = False

        for val in nums:
            if count_dict.get(val):
                count_dict[val] += 1
                flag = True
                break
            else:
                count_dict[val] = 1
        
        return flag
