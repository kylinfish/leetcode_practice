from typing import List

class Solution:
    def main(self, s: List[str]) -> None:
        if len(s) < 1 or len(s) >= pow(10, 5):
            return false

        end_i = len(s)
        middle = int(len(s) / 2) - 1
        for i in range(0, len(s)):
            end_i -=1

            swap = s[end_i]
            s[end_i] = s[i]
            s[i] = swap
            print(i, end_i, s)

            if i >= middle:
                return s
        return s


if __name__ == "__main__":
    s = Solution()
    print(s.main(["h","e","l","l","o"]))
