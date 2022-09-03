class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        current = current.split(":")
        currentInt = int(current[0]) * 60 + int(current[1])

        correct = correct.split(":")
        correctInt = int(correct[0]) * 60 + int(correct[1])
        diff = correctInt - currentInt

        num = diff // 60
        rem = diff % 60

        if rem != 0:
            num += rem // 15
            rem = rem % 15
            if rem != 0:
                num += rem // 5
                rem = rem % 5
                if rem != 0:
                    num += rem // 1

        return num