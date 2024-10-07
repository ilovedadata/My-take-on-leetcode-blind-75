class Solution:
    def meetingrooms(self, meetings:list[tuple]) -> bool:
        meetings.sort()

        for i in range(1, len(meetings)):

            if meetings[i-1][1] > meetings[i][0]:
                return False
        
        return True