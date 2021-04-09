#coding=UTF-8
"""
Two Pointers
利用交換指標的方式
在以排序的 array 中，計算兩兩(i and i -1)不同的值有幾個 count

"""

def main(nums):
    if len(nums) < 0 or len(nums) >= 3 * pow(10, 4):
        return 0

    lens = 1
    for i in range(1, len(nums)):
        if nums[i-1] != nums[i]:
            nums[lens] = nums[i]
            lens += 1


    return lens


if __name__ == '__main__':
    print(main([0]))
    print(main([1, 2]))
    print(main([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
