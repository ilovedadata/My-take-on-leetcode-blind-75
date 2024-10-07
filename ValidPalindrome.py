class Solution(object):
    def is_alpha_num(self, char:str) -> bool:
        return (ord(char) >= ord('a') and ord(char) <= ord('z') or 
                ord(char) >= ord('A') and ord(char) <= ord('Z') or 
                ord(char) >= ord('0') and ord(char) <= ord('9'))

    def isPalindrome(self, word:str) -> bool:
        word_listed = []

        for char in word:
            if self.is_alpha_num(char):
                word_listed.append(char.lower()) 

        return word_listed == word_listed[::-1]