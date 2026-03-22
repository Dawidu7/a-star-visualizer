from enum import Enum

WIDTH, HEIGHT = 800, 800
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)

class TileType(Enum):
  EMPTY = 0
  WALL = 1
  START = 2
  END = 3
  OPEN = 4
  CLOSED = 5
  PATH = 6
  PATH_START = 7
  PATH_END = 8

TILE_COLORS = {
  TileType.EMPTY: WHITE,
  TileType.WALL: BLACK,
  TileType.START: ORANGE,
  TileType.END: PURPLE,
  TileType.OPEN: GREEN,
  TileType.CLOSED: RED,
  TileType.PATH: BLUE,
  TileType.PATH_START: BLUE,
  TileType.PATH_END: BLUE,
}