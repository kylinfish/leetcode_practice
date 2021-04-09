"""
n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
3x -> Fizz
5x -> Buzz
15x -> FizzBuzz
"""
from typing import List
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                result.append("FizzBuzz")
                continue
            if i % 3 == 0:
                result.append("Fizz")
                continue
            if i % 5 == 0:
                result.append("Buzz")
                continue

            result.append(i)

        return result



if __name__ == "__main__":
    s = Solution()
    print(s.fizzBuzz(15))
