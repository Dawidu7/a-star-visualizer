import pygame
import sys

WIDTH, HEIGHT = 800, 800
FPS = 60

WHITE = (255, 255, 255)

class Window:
  def __init__(self) -> None:
    pygame.init()

    self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("A*")

    self.clock = pygame.time.Clock()
    self.is_running = True

  def run(self) -> None:
    while self.is_running:
      dt = self.clock.tick(FPS) / 1000
      self._handle_events()
      self._update(dt)
      self._draw()

    pygame.quit()
    sys.exit(0)

  def _handle_events(self) -> None:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.is_running = False

  def _update(self, dt: float) -> None:
    pass

  def _draw(self) -> None:
    self.screen.fill(WHITE)

    pygame.display.flip()

if __name__ == "__main__":
  window = Window()
  window.run()