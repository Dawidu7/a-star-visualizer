from queue import PriorityQueue
from tile import Tile

class AStar:
  def __init__(self, grid: list[list[Tile]]) -> None:
    self.grid = grid

  def find_path(self, start_tile: Tile, end_tile: Tile) -> list[Tile]:
    count = 0
    open_queue: PriorityQueue[tuple[float, int, Tile]] = PriorityQueue()
    open_queue.put((0, count, start_tile))
    open_hash: set[Tile] = {start_tile}
    g_score: dict[Tile, float] = {start_tile: 0}
    f_score: dict[Tile, float] = {start_tile: self._heuristic((start_tile.row, start_tile.col), (end_tile.row, end_tile.col))}
    came_from: dict[Tile, Tile] = {}

    while not open_queue.empty():
      _, _, current_tile = open_queue.get()
      open_hash.remove(current_tile)
      neighbours = current_tile.get_neighbours(self.grid)

      if current_tile == end_tile:
        return self._reconstruct_path(came_from, current_tile)
      
      for neighbour in neighbours:
        g = g_score[current_tile] + neighbour.cost
        if g < g_score.get(neighbour, float("inf")):
          g_score[neighbour] = g
          h = self._heuristic((neighbour.row, neighbour.col), (end_tile.row, end_tile.col))
          f_score[neighbour] = g + h
          came_from[neighbour] = current_tile

          if not neighbour in open_hash:
            count += 1
            open_queue.put((f_score[neighbour], count, neighbour))
            open_hash.add(neighbour)
            
    return []

  def _heuristic(self, a: tuple[int, int], b: tuple[int, int]) -> float:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
  
  def _reconstruct_path(self, came_from: dict[Tile, Tile], current_tile: Tile) -> list[Tile]:
    path = [current_tile]

    while current_tile in came_from:
      current_tile = came_from[current_tile]
      path.append(current_tile)

    path.reverse()
    return path