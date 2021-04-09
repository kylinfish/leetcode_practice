from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if len(nums) < 1 or len(nums) > 2 * pow(10, 4):
            return False

        if k < 0 or k >= pow(10, 5):
            return False

        split = len(nums) - k

        first = nums[split:len(nums)]
        second = nums[:split]

        nums[:k] = first
        nums[k:len(nums)] = second
        print(nums)





if __name__ == "__main__":
    s = Solution()
    print(s.rotate([1,2,3,4,5,6,7], k = 3))
    print(s.rotate([-1,-100,3,99], k = 2))


