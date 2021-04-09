"""
15. 3Sum

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []


"""


def main():
    input = [-1, 0, 1, 2, -1, -4]
    input.sort()

    print(input)
    print("Output: [[-1,-1,2], [-1,0,1]]")

    # Build HashMap to Search index
    dict_map = {}
    for i, d in enumerate(input):
        dict_map[d] = i

    result = []
    for i, d in enumerate(input):
        target = -d
        #print("T: " + str(target))

        candidate = [d]
        # search target for two sum problem
        for j, nd in enumerate(input):
            if i == j:
                continue

            if nd == 0:
                candidate.append(nd)
                continue

            if target in dict_map:
                candidate.append(target)
                break
        print(candidate)



if __name__ == "__main__":
    main()
