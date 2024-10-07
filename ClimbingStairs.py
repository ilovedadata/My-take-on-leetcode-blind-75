class Solution(object):
    def ClimbingStairs(self, n:int) -> int:

        if n <=2 :
            return n

        curr_steps = 0
        two_steps_ago = 1
        one_steps_ago = 2
    
        for step in range(3, n+1): 

            curr_steps = one_steps_ago + two_steps_ago
            two_steps_ago = one_steps_ago
            one_steps_ago = curr_steps
        
        return curr_steps