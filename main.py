import sys
import pygame
from settings import *
from visualizer import Visualizer

class Window:
  def __init__(self) -> None:
    pygame.init()

    self.visualizer = Visualizer(30, 30)
  
    screen_size = (self.visualizer.width, self.visualizer.height)
    self.screen = pygame.display.set_mode(screen_size)
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
      match event.type:
        case pygame.QUIT:
          self.is_running = False
        case pygame.KEYDOWN:
          match event.key:
            case pygame.K_SPACE:
              self.visualizer.start()

    is_left_clicked, _, is_right_clicked = pygame.mouse.get_pressed()

    if is_left_clicked or is_right_clicked:
      self.visualizer.handle_click(is_left_clicked, is_right_clicked)

  def _update(self, dt: float) -> None:
    pass

  def _draw(self) -> None:
    self.screen.fill(WHITE)

    self.visualizer.draw(self.screen)

    pygame.display.flip()

if __name__ == "__main__":
  window = Window()
  window.run()