from enum import Enum
from typing import NamedTuple, List
import random

#enum is used for better code readability
class Cell(str,Enum):   #enum consists of group of variables of same or different data types
    start  = 'S'
    end = 'E'
    block = 'X'
    empty = ' '
    path = '*'

#to locate individual position in maze
# NamedTupple is used for code readability and to refer items with name instead of index 
class Maze_Location(NamedTuple):
    row: int
    column: int


#to generate random maze
class Maze:
    def __init__(self,row:int = 10,column:int=10, start= Maze_Location(0,0), end = Maze_Location(9,9)
                 , randmness:float = 0.2) -> None:
        self._rows:int = row
        self._columns:int = column
        self.start:Maze_Location = start
        self.end:Maze_Location = end
        #to create a grid of empty spaces
        self._grid: List[List[Cell]] = [[Cell.empty for c in range(column)]for r in range(row)]
        #generate a maze
        self._random_filling_(row,column,randmness)
        #fill the start and end in the maze(_grid)
        self._grid[end.row][start.column] = Cell.start
        self._grid[start.row][end.column] = Cell.end

        

    def _random_filling_(self,row:int,column:int,randomness:float):
        for r in range(row):
            for c in range(column):
                if random.uniform(0,1.0) < randomness:
                    self._grid[r][c] = Cell.block
    
    # #we need a function to print the maze in proper format
    # __str__ is a special method used to print str version of object
    # def __str__(self) -> str:
    #     output:str = ''
    #     for row in self._grid:
    #         output += ''.join([c.value for c in row]) + '\n'
    #     return output
    
    def __repr__(self) -> str:
        output:str = ''
        for row in self._grid:
            output += ''.join([c.value for c in row]) + '\n'
        return output
    

maze:Maze = Maze()
print(repr(maze))



    