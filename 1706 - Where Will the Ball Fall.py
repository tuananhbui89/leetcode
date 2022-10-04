class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        # Define Global Name 
        TL2BR = 1 # Top Left To Bottom Right 
        BL2TR = -1 # Bottom Left To Top Right 
        STUCK = -1 # Stuck in any position or fall out of the grid 
        m = len(grid)
        n = len(grid[0])
        
        def next_pos(pos, left, this, right): 
            """
            Find position of the ball in the next row 
            Args: 
                pos: current position in the current row, 0<= pos <= n-1 
                left: direction of the left cell of the current row 
                    if pos == 0, then left = TL2BR 
                right: direction of the right cell of the current row 
                    if pos == n-1 then right = BL2TR
            Doing: 
                if this == TL2BR and right == TL2BR: 
                    possible to move to the right. next_pos = pos + 1 
                if this == TL2BR and right == BL2TR:
                    stuck, next_pos = -1 
                if this == BL2TR and left == BL2TR: 
                    possible to move to the left. next_pos = pos - 1 
                if this == BL2TR and left == TL2BR: 
                    stuck, next_pos = -1 
            """
            if pos == 0: 
                left = TL2BR 
            elif pos == n - 1: 
                right = BL2TR 
            
            if this == TL2BR: 
                return pos+1 if right == TL2BR else STUCK 
            elif this == BL2TR: 
                return pos-1 if left == BL2TR else STUCK 
            else: 
                raise ValueError 
            
        
        def process_row(row_index): 
            """
            Given a row_index, return the position of the ball after this row.  
            row_index = 0, grid[0] = [1,1,1,-1,-1]
            return [1,2,-1,-1,3]
            Explain: 
                -ball, b0 in pos=0, can move to next_pos=1 
                -ball, b1 in pos=1, can move to next_pos=2 
                -ball, b2 in pos=2, cannot move because, it right == BL2TR, next_pos=-1 
            """
            assert(row_index <= m-1 and row_index >= 0)
            row = grid[row_index]
            output = []
            for pos in range(n): 
                left = row[pos-1] if pos >= 1 else TL2BR
                right = row[pos+1] if pos <= n-2 else BL2TR
                this = row[pos]
                output.append(next_pos(pos, left, this, right))
            
            return output 
        
        def merge_2rows(row1, row2): 
            """
            Given the position of two consecutive rows, merge two rows to only one row  
            Always assume the ball fall from the first row, 
            it means that row0 = [0,1,2,3,4]
            Example 1, 
                row1 = [0,1,2,3,4] --> position of ball in the first row 
                row2 = [1,2,-1,-1,3] --> position of ball in the second row 
                return output = [1,2,-1,-1,3] --> position of ball after the second row 
            Example 2, 
                row0 = [0,1,2,3,4]
                row1 = [1,2,-1,-1,3]
                row2 = [1,2,-1,-1,3] 
                return output = [-1,2,]
                    output[0] == 2  because row2[row1[row0[0]]] = 2
                    output[1] == -1 because row2[row1[row0[1]]] = -1 
            """
            output = []
            row2 = row2 + [-1]
            for pos in range(n): 
                output.append(row2[row1[pos]])
            return output 
        
        cur = process_row(0)
        for i in range(1,m): 
            next_row = process_row(i)
            cur = merge_2rows(cur, next_row)
            
        output = cur 
        return output 