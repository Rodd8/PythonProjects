from tile import Tile
from piece import Piece
from typing import List

BLACK = (0,0,0)
WHITE = (255,255,255)

class Board:
    def __init__(self) -> None:
        self.tiles = self.__create_board()
        
    def __create_board(self):
        board = []
        for i in range(8):
            row = []
            for j in range(8):
                tile = Tile(BLACK, i, j) if (i + j) % 2 == 0 else Tile(WHITE, i, j)

                if (i+j) % 2 == 0:
                    if i < 3:
                        tile.piece = Piece(WHITE)
                    elif i > 4:
                        tile.piece = Piece(BLACK)

                row.append(tile)
            board.append(row)
        return board

    
    def display_board(self):
        for i in range(8):
            for j in range(8):
                tile = self.tiles[i][j]
                color = tile.color

                if tile._is_occupied():
                    piece_color = tile.piece.color
                    print("⚫", end ="") if piece_color == BLACK else print("⚪", end="")
                else:                
                    print("⬛", end="") if color == BLACK else print("⬜", end="")
            print()