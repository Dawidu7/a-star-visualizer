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

  @property
  def _color(self) -> tuple[int, int, int]:
    return TILE_COLORS[self.type]

  def draw(self, screen: pygame.Surface) -> None:
    pygame.draw.rect(screen, self._color, (self._x, self._y, self.tile_size, self.tile_size))

class Visualizer:
  def __init__(self, cols: int, rows: int) -> None:
    self.cols = cols
    self.rows = rows
    self.tile_size = min(WIDTH // cols, HEIGHT // rows)
    self.width = cols * self.tile_size
    self.height = rows * self.tile_size

    self.grid = [[Tile(i, j, self.tile_size) for j in range(cols)] for i in range(rows)]

  def draw(self, screen: pygame.Surface) -> None:
    for row in self.grid:
      for tile in row:
        tile.draw(screen)

    for i in range(self.rows):
      pygame.draw.line(screen, BLACK, (0, i * self.tile_size), (self.width, i * self.tile_size))

    for j in range(self.cols):
      pygame.draw.line(screen, BLACK, (j * self.tile_size, 0), (j * self.tile_size, self.height))