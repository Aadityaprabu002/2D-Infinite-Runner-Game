import pygame
import GameFunctions
import time
import Asset

pygame.init()

if __name__ == '__main__':
    Asset.bg_music.play(-1)
    GAME = GameFunctions.GAME()
    GAME.new()
    while GAME.menu:
        Asset.bg_music.set_volume(1)
        GAME.CLOCK.tick(GAME.FPS)
        GAME.Move_Background()
        GAME.Move_Platform()
        GAME.player.run_()
        GAME.draw()
        GAME.is_cowboy_land_collision()
        GAME.show_menu()
        pygame.display.update()

        while GAME.game:

            GAME.CLOCK.tick(GAME.FPS)
            GAME.Move_Background()
            GAME.Move_Platform()
            GAME.show_score()
            GAME.player.direction = 'stay'

            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    GAME.game = False

                elif events.type == pygame.KEYDOWN:

                    if events.key == pygame.K_DOWN and not GAME.player.jump and GAME.player.onland:
                        GAME.player.slide = True
                        GAME.player.jump = False
                        GAME.player.run = False
                        Asset.slide.play()
                    if events.key == pygame.K_p:
                         pause = True
                         while pause:

                             GAME.CLOCK.tick(GAME.FPS)
                             GAME.draw()
                             text = pygame.font.SysFont("ARIAL", 180, True)
                             menutext = text.render("PAUSED", True, (255, 255, 255))
                             GAME.screen.blit(menutext, (370, 300))
                             GAME.instructions()
                             pygame.display.update()
                             for event in pygame.event.get():
                                 if event.type == pygame.QUIT:
                                     GAME.game = False
                                 elif event.type == pygame.KEYDOWN:
                                     if event.key == pygame.K_p:
                                         pause = False


                    elif events.key == pygame.K_SPACE and not GAME.player.slide and GAME.player.onland:
                        GAME.player.jump = True
                        GAME.player.run = False
                        GAME.player.slide = False
                        Asset.jump.play()

                    if events.key == pygame.K_RIGHT and not GAME.player.slide:
                        GAME.player.run = True
                        GAME.player.direction = 'r'

                    elif events.key == pygame.K_LEFT and not GAME.player.slide:
                        GAME.player.run = True
                        GAME.player.direction = 'l'

            GAME.is_cowboy_land_collision()
            if GAME.player.jump:
                GAME.player.jump_()
            if GAME.player.run:
                GAME.player.run_()
            if GAME.player.slide:
                GAME.player.slide_()

            GAME.Move_obstacle()
            GAME.draw()
            GAME.instructions()
            GAME.is_cowboy_obstacle_collision()
            pygame.display.update()

            if not GAME.game:
                GAME.delete_obstacles_and_reinitialize_player()
                time.sleep(2)
                Asset.bg_music.play(-1)

    pygame.quit()
