class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        out = []
        height = len(matrix)
        width = len(matrix[0])
        count = height * width
        
        top = 0 
        bot = height-1 
        left = 0 
        right = width-1 
        
        def moving(row,col,direction): 
            if direction == 'l2r': 
                return row,col+1 
            elif direction == 't2b': 
                return row+1,col 
            elif direction == 'r2l': 
                return row,col-1
            elif direction == 'b2t': 
                return row-1,col 
        
        def new_direction(row,col,direction,top,bot,left,right): 
            if (direction == 'l2r') & (col == right): 
                return 't2b',top+1,bot,left,right
            elif (direction == 't2b') & (row == bot): 
                return 'r2l',top,bot,left,right-1
            elif (direction == 'r2l') & (col == left):
                return 'b2t',top,bot-1,left,right 
            elif (direction == 'b2t') & (row == top): 
                return 'l2r',top,bot,left+1,right 
            else: 
                return direction,top,bot,left,right
        
        direction = 'l2r'
        row=0
        col=0 
        while count > 0:
            print(row,col)
            out.append(matrix[row][col])
            count -= 1 
            direction,top,bot,left,right = new_direction(row,col,direction,top,bot,left,right)
            row,col = moving(row,col,direction)
        
        return out