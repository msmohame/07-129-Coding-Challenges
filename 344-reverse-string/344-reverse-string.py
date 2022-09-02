class Solution:
    def reverseString(self, s: List[str]) -> None:
        j = len(s) - 1
        for i in range(len(s) // 2):
            tmp = s[i]
            s[i] = s[j]
            s[j] = tmp
            j = j - 1
        