from typing import Collection


from typing import Tuple

class Piece:
    def __init__(self, color:Tuple[int, int, int]) -> None:
        self.color = color
        self.is_queen = False
        
    def promote(self) -> None:
        self.is_queen = True