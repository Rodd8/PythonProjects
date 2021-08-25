from typing import Tuple, List

def find_next_empty(grid: List[List[int]]) -> Tuple[int, int]:
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                return (row, col)
    return None


def print_grid(grid: List[List[int]]) -> None:
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-------+--------+-------")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end='')
            if j == 8:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + " ", end="")


def is_valid_number(grid: List[List[int]], number: int, pos: Tuple[int, int]) -> bool:
    row = pos[0]
    col = pos[1]
    
    for x in range(len(grid[0])):
        if grid[row][x] == number and col != x:
            return False
            
    for x in range(len(grid)):
        if grid[x][col] == number and row != x:
            return False
    
    square_x = col // 3
    square_y = row // 3
    for i in range(square_y*3, square_y*3 + 3):
        for j in range(square_x*3, square_x*3 + 3):
            if grid[i][j] == number and (i,j) != pos:
                return False
    
    return True
    
def solve(grid) -> bool:
    next_empty = find_next_empty(grid)
    if not next_empty:
        return True
    else:
        row, col = next_empty
        
    for n in range(1,10):
        if is_valid_number(grid, n, (row, col)):
            grid[row][col] = n
            
            if solve(grid):
                return True

            grid[row][col] = 0
            
    return False


def main():
    print_grid(sudoku_grid)
    solve(sudoku_grid)
    print("\n\n")
    print_grid(sudoku_grid)
    


if __name__ == "__main__":
    sudoku_grid = [
        [5,0,0, 0,8,6, 0,0,1],
        [0,0,2, 7,0,1, 6,0,0],
        [0,7,1, 0,0,0, 2,5,0],
        [9,1,0, 0,2,0, 0,7,0],
        [3,0,0, 1,4,5, 0,0,6],
        [0,6,0, 0,9,0, 0,2,4],
        [0,5,3, 0,0,0, 4,6,0],
        [0,0,8, 9,0,3, 5,0,0],
        [2,0,0, 5,1,0, 0,0,7]
    ]
      
    main()