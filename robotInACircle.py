# Time :O(n)
# Space:O(1)
# Leetcode:Yes
# Issues:No


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dirs = [(0,1),(1,0),(0,-1),(-1,0)] # clockwise N W E S
        # dirs = [(0,-1),(-1,0),(0,1),(1,0)] # anticlock

        x,y = 0,0
        idx = 0 #// North
        
        # for i in range(4):
        for c in instructions:
            if c == 'G':
                x += dirs[idx][0]
                y += dirs[idx][1]
            elif c == 'R':
                idx = (idx+1) %4            # move 1 dir to right
            elif c == 'L':
                idx = (idx+3) %4            # move 3 dir to right

        return (x == 0 and y == 0) or idx != 0  #  origin or not north