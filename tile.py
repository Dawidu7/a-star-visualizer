from __future__ import annotations
import pygame
from settings import *

class Tile:
  def __init__(self, row: int, col: int, tile_size: int) -> None:
    self.row = row
    self.col = col
    self.tile_size = tile_size
    self._x = col * tile_size
    self._y = row * tile_size
    self.type = TileType.EMPTY
    self.cost = 1  # 

  @property
  def _color(self) -> tuple[int, int, int]:
    return TILE_COLORS[self.type]
  
  def _is_walkable(self) -> bool:
    return self.type != TileType.WALL
  
  def get_neighbours(self, grid: list[list[Tile]]) -> list[Tile]:
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    neighbours: list[Tile] = []

    for dx, dy in directions:
      row = self.row + dx
      col = self.col + dy
      if 0 <= row < len(grid) and 0 <= col < len(grid[self.row]):
        tile = grid[row][col]
        if tile._is_walkable():
          neighbours.append(tile)

    return neighbours

  def draw(self, screen: pygame.Surface) -> None:
    pygame.draw.rect(screen, self._color, (self._x, self._y, self.tile_size, self.tile_size))

  def __repr__(self) -> str:
    return f"Tile[{self.row}][{self.col}]"