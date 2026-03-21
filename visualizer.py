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
    self.start_tile: Tile | None = None
    self.end_tile: Tile | None = None

  def handle_click(self, is_left_clicked: bool, is_right_clicked: bool) -> None:
    pos = pygame.mouse.get_pos()
    row = pos[1] // self.tile_size
    col = pos[0] // self.tile_size
    selected_tile = self.grid[row][col]

    if is_left_clicked:
      if selected_tile == self.start_tile or selected_tile == self.end_tile:
        return

      if not self.start_tile:
        selected_tile.type = TileType.START
        self.start_tile = selected_tile
      elif not self.end_tile:
        selected_tile.type = TileType.END
        self.end_tile = selected_tile
      else:
        selected_tile.type = TileType.WALL

    elif is_right_clicked:
      if selected_tile == self.start_tile:
        self.start_tile = None
      elif selected_tile == self.end_tile:
        self.end_tile = None

      selected_tile.type = TileType.EMPTY

  def draw(self, screen: pygame.Surface) -> None:
    for row in self.grid:
      for tile in row:
        tile.draw(screen)

    for i in range(self.rows):
      pygame.draw.line(screen, BLACK, (0, i * self.tile_size), (self.width, i * self.tile_size))

    for j in range(self.cols):
      pygame.draw.line(screen, BLACK, (j * self.tile_size, 0), (j * self.tile_size, self.height))