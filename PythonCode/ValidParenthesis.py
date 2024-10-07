class Solution(object):
    def isValid(self, s:str) -> bool:
        my_stack = []
        hash_map = {')':'(', ']': '[', '}': '{'}

        for par in s:
            if par in hash_map.values():
                my_stack.append(par)
            elif my_stack and hash_map[par] == my_stack[-1]:
                my_stack.pop()
            else:
                return False
        
        return my_stack == []