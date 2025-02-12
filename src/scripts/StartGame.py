import pygame

from typing import Literal

from scripts.scenes.Menu import Menu
from scripts.scenes.Game import Game
from scripts.scenes.GameOver import GameOver
from scripts.scenes.Cutscenes import Cutscene

import sys

from scripts.settings import FPS, WIDTH, HEIGHT, TITLE, BG_COLOR
from scripts.utils.EventHandler import EventHandler

class StartGame:

    def __init__(self) -> None:
        
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()
        pygame.display.set_caption(TITLE)
        pygame.display.init()

        # It must be called before any Scene
        self.display = pygame.display.set_mode([WIDTH, HEIGHT])

        # Controls the gaming loop
        self.running = True

        # Locks the FPS
        self.clock = pygame.time.Clock()
        # The desired FPS
        self.target_fps = FPS

        # All possible scenarios
        self.scene: Literal["menu","cutscene", "game", "gameover"] = "cutscene"
        self.current_scene = Cutscene()


    # Game Loop
    def run(self):

        print(self.scene)

        while self.running:

            if self.scene == "menu" and self.current_scene.active == False:
                self.scene = "cutscene"

                self.current_scene = Cutscene()

            elif self.scene == "cutscene" and self.current_scene.active == False:

                self.scene = "game"

                self.current_scene = Game()

            elif self.scene == "game" and self.current_scene.active == False:

                self.scene = "gameover"

                self.current_scene = GameOver()

            elif self.scene == "gameover" and self.current_scene.active == False:

                self.scene = "menu"
                self.current_scene = Menu()

            EventHandler.poll_events()
            for event in EventHandler.events:

                if event.type == pygame.QUIT:

                    pygame.quit()
                    sys.exit()

                if event.type == pygame.K_e:

                    self.scene = "game"

                self.current_scene.events(event)

            self.clock.tick(self.target_fps)

            self.current_scene.draw()
            self.current_scene.update()

            pygame.display.flip()            