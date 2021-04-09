class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < 0 or len(needle) >= 5 * pow(10, 4):
            return 0

        if needle =="":
            return 0

        needle_len = len(needle)

        for i in range(0, len(haystack)):
            if needle == (haystack[i:i+needle_len]):
                return i

        return -1





if __name__ == "__main__":
    s = Solution()
    print(s.strStr("aaaaa", "bba"))
    #print(s.strStr("", ""))
    #print(s.strStr("hello", "ll"))
    #print(s.strStr("hello", "ll"))
