import pygame
from settings import *
from tile import Tile, TileHistory
from pathfinder import AStar

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

    self.pathfinder = AStar()
    self.is_animating = False
    self.history: TileHistory | None = None

  def start(self) -> None:
    if not self.start_tile or not self.end_tile:
      return
    
    if self.is_animating:
      return

    self._reset_grid()
    start_tile = self.start_tile
    end_tile = self.end_tile
    path, self.history = self.pathfinder.find_path(self.grid, start_tile, end_tile)
    self.is_animating = True

    print(path)

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

  def update(self) -> None:
    if not self.history:
      if self.is_animating:
        self.is_animating = False
      return
    
    tile, type = self.history.pop(0)
    tile.type = type

  def draw(self, screen: pygame.Surface) -> None:
    for row in self.grid:
      for tile in row:
        tile.draw(screen)

    for i in range(self.rows):
      pygame.draw.line(screen, BLACK, (0, i * self.tile_size), (self.width, i * self.tile_size))

    for j in range(self.cols):
      pygame.draw.line(screen, BLACK, (j * self.tile_size, 0), (j * self.tile_size, self.height))

  def clear_grid(self) -> None:
    if self.is_animating:
      return
    
    for row in self.grid:
      for tile in row:
        tile.type = TileType.EMPTY

    self.start_tile = None
    self.end_tile = None

  def _reset_grid(self) -> None:
    for row in self.grid:
      for tile in row:
        if tile.type not in (TileType.EMPTY, TileType.WALL, TileType.START, TileType.END):
          tile.type = TileType.EMPTY