# import math

class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean_text = "".join(char for char in s if char.isalnum()).lower()
        print(clean_text)
        for i in range(math.floor(len(clean_text)/2)):
            # print(i)
            if clean_text[i] != clean_text[-1-i]:
                # print(clean_text[i-1])
                # print(clean_text[-1-i])
                return False
        return True

        # left_index = 0
        # right_index = len(s)
        # print(ord("a"))
        # print(ord("z"))
        # print(ord("A"))
        # print(ord("Z"))
        # while left_index < right_index:
        #     # get the next letter
        #     if ord(s[left_index]) >= ord("a") and ord(s[left_index]) <= ord("Z") :
        #         left_letter = min(s[left_index], s)
        #     elif ord
        #     if ord(s[lef]) 
