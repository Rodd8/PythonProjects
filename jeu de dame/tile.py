from typing import Tuple
from piece import Piece

class Tile:
    def __init__(self, color: Tuple[int, int, int], row :int, col: int, piece: Piece = None) -> None:
        self.color = color
        self.row = row
        self.col = col
        self.id = str(row)+str(col)
        self.piece = piece
        
    def _switch_occupiance(self) -> None:
        self.is_occupied = not self.is_occupied
        
    def _is_occupied(self) -> bool:
        return self.piece != None