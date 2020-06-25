# the grid describes the surface of a ball


import random

class Cell:
     
    def __init__(self, location):
        
        self.location = location
        
        self.age = 0
        
        self.alive = False
        self.color = "black"
        
        self.up = None
        self.up_right = None
        self.up_left = None
        
        self.down = None
        self.down_right = None
        self.down_left = None
        
        self.right = None
        self.left = None
        
        self.neighbors = 0
        
    def count_neighbors(self):
        
        counter = 0
        
        for cell in [self.up_left, self.up, self.up_right, self.left, self.right, self.down_left, self.down, self.down_right]:
            
            if cell != None:
                
                if cell.alive:
                    
                    counter += 1
        
        self.neighbors = counter
                
         
    def survive(self):
        
        if self.alive:
            
            if self.neighbors < 2 or self.neighbors > 3:
                
                self.alive = False
                self.age = 0
                
            # elif self.age > 80:
                
            #     if random.random() < self.age/100:
                    
            #         self.alive = False
            #         self.age = 0
                    
            else:
                
                self.age += 1
        else:
            
            if self.neighbors == 3:
                
                self.alive = True
                self.age = 0


class GridBall:
    
    def __init__(self, rows, columns):
        
        self.rows = rows
        self.columns = columns
        
        # to save memory
        self.grid = [[0]*self.columns]*self.rows
        
    def create_grid(self):
        
        # initialize the cells
        for row in range(self.rows):
    
            self.grid[row] = [Cell([row,column]) for column in range(self.columns)]
        
        # connect the cells
        for row in range(self.rows):
        
            for column in range(self.columns):
                
                if row == 0:
                    
                    self.grid[0][column].up = self.grid[self.rows -1][column]
                
                    if column == 0:
                        
                        self.grid[0][0].up_left = self.grid[self.rows -1][self.columns -1]
                        
                    else:
                        
                        self.grid[0][column].up_left = self.grid[self.rows -1][column -1]
                        
                    if column == self.columns - 1:
                        
                        self.grid[0][self.columns - 1].up_right = self.grid[self.rows -1][0]
                    
                    else:
                        
                        self.grid[0][column].up_right = self.grid[self.rows - 1][column + 1]
                        
        
                else:
            
                    self.grid[row][column].up = self.grid[row - 1][column]
                        
                    if column == 0:
                        
                        self.grid[row][column].up_left = self.grid[row - 1][self.columns - 1]
                            
                    else:
                            
                        self.grid[row][column].up_left = self.grid[row - 1][column - 1]
                        
                    if column == self.columns - 1:
                        
                        self.grid[row][column].up_right = self.grid[row - 1][0]
                        
                    else:
                            
                        self.grid[row][column].up_right = self.grid[row - 1][column + 1]
                        
                if row == self.rows - 1:
                    
                    self.grid[row][column].down = self.grid[0][column]
                
                    if column == 0:
                        
                        self.grid[row][0].down_left = self.grid[0][self.columns - 1]  
                        
                    else: 
                        
                        self.grid[row][column].down_left = self.grid[0][column - 1]
                        
                    if column == self.columns - 1:
                        
                        self.grid[row][column].down_right = self.grid[0][0]
                        
                    else:
                        
                        self.grid[row][column].down_right = self.grid[0][column + 1]
                        
                            
                else:
            
                    self.grid[row][column].down = self.grid[row + 1][column]
                
                    if column == 0:
                        
                        self.grid[row][column].down_left = self.grid[row + 1][self.columns - 1] 
                        
                    else:
                            
                        self.grid[row][column].down_left = self.grid[row + 1][column - 1]
                        
                    if column == self.columns - 1:
                        
                        self.grid[row][column].down_right = self.grid[row + 1][0]
                    
                    else:
                            
                        self.grid[row][column].down_right = self.grid[row + 1][column + 1]
                        
                    
                if column == 0:
            
                    self.grid[row][column].left = self.grid[row][self.columns - 1]
                
                else: 
                    
                    self.grid[row][column].left = self.grid[row][column - 1]
                    
                
                if column == self.columns - 1:
                    
                    self.grid[row][column].right = self.grid[row][0]
                       
                else:
            
                    self.grid[row][column].right = self.grid[row][column + 1]
                    
                    
    def grid_count_neighbors(self):
        
        for row in range(self.rows):
            
            for column in range(self.columns):
                
                self.grid[row][column].count_neighbors()
                
    def grid_survive(self):
        
        for row in range(self.rows):
            
            for column in range(self.columns):
                
                self.grid[row][column].survive()
            
                
    def grid_create_image(self):
        
        array = [[0]*self.columns]*self.rows
        
        for index, row in enumerate(self.grid):
            
            array[index] = [cell.alive for cell in row]
            
        array = np.asarray(array)
    
        return array
    
    def grid_random_state(self):
        
        for row in self.grid:
            
            for cell in row:
                
                if random.random() > 0.8:
                    
                    cell.alive = True
        