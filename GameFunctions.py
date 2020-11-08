import pygame
import Asset
import GameSprites
import random

TEXT = pygame.font.SysFont("ARIAL", 50, True)


color = [(255, 0, 0),(255, 111, 0),(255, 234, 0) ,(0, 255, 26) ,(0, 255, 238),(68, 0, 255),(136, 0, 255)]
index = 0
class GAME:
    def __init__(self):
        self.obstacles_list = None
        pygame.init()
        self.screen = pygame.display.set_mode((Asset.I_W, Asset.I_H))
        self.CLOCK = pygame.time.Clock()
        self.FPS = 60
        self.game = False
        self.menu = True
        self.sx = 0
        self.obstacles = []
        self.platform_list = []
        self.obstaclestimer = 0
        self.obstaclesdeploytime = 0
        self.obstacles_endtime_set = False
        self.crate = None
        self.deletecrates = False
        self.score = 0
        self.menu=True

        self.block_list = pygame.sprite.Group()
        self.obstacle_list = pygame.sprite.Group()

        self.player = GameSprites.COWBOY()
        self.sprite_list = pygame.sprite.Group()
        self.sprite_list.add(self.player)


    def new(self):

        # Initialise cowboy



        for i in range(0, Asset.S_WIDTH, 50):
            blocks = GameSprites.PLATFORM(i, Asset.S_HEIGHT - 150, Asset.tile1_path)
            self.block_list.add(blocks)
            self.platform_list.append(blocks)

        for i in range(0, Asset.S_WIDTH, 50):

            blocks = GameSprites.PLATFORM(i, Asset.S_HEIGHT - 100, Asset.tile2_path)
            self.block_list.add(blocks)
            self.platform_list.append(blocks)
            if i == 750:
                blocks = GameSprites.PLATFORM(i, Asset.S_HEIGHT - 100, Asset.tile3_path)
                self.block_list.add(blocks)
                self.platform_list.append(blocks)

        for i in range(0, Asset.S_WIDTH, 50):

            blocks = GameSprites.PLATFORM(i, Asset.S_HEIGHT - 50, Asset.tile2_path)
            self.block_list.add(blocks)
            self.platform_list.append(blocks)

            if i == 350:
                blocks = GameSprites.PLATFORM(i, Asset.S_HEIGHT - 50, Asset.tile4_path)
                self.block_list.add(blocks)
                self.platform_list.append(blocks)

    def draw(self):

        self.block_list.draw(self.screen)
        self.sprite_list.draw(self.screen)
        self.obstacle_list.draw(self.screen)

    def is_cowboy_land_collision(self):

        blockhit = pygame.sprite.spritecollide(self.player, self.block_list, False)
        if blockhit:
            # print("Colliding with land")
            self.player.onland = True
        else:
            # print("Not Colliding with land")
            self.player.onland = False

        if not self.player.onland:
            self.player.gravity_pull()

    def is_cowboy_obstacle_collision(self):
        obstaclehit = pygame.sprite.spritecollide(self.player, self.obstacle_list, False, pygame.sprite.collide_mask)
        if obstaclehit:
            self.game = False
            Asset.hit.play()
            self.Move_Background()
            self.Move_Platform()
            self.draw()
            Asset.bg_music.stop()
            text = pygame.font.SysFont("ARIAL", 180, True)
            menutext = text.render("GAME OVER", True, (255, 255, 255))
            self.screen.blit(menutext, (150, 300))
            text = pygame.font.SysFont("ARIAL", 100, True)
            menutext = text.render("YOUR SCORE:"+str(self.score), True, (255, 255, 255))
            self.screen.blit(menutext, (240, 500))
            pygame.display.update()

        else:
            self.score += 1


    def Move_Background(self):

        self.sx -= 10
        if self.sx == -Asset.S_WIDTH:
            self.sx = 0

        self.screen.blit(Asset.STARS, (0, 0))
        self.screen.blit(Asset.ROCKS, (0, 0))
        self.screen.blit(Asset.BACKGROUND2, (self.sx, -25))
        self.screen.blit(Asset.BACKGROUND2, (Asset.S_WIDTH + self.sx, -25))
        rect = (Asset.S_WIDTH, 0, 500, Asset.S_HEIGHT)
        pygame.draw.rect(self.screen, (0, 0, 0), rect)

    def __Create_obstacle(self):

        if len(self.obstacles) == 0:
            self.deletecrates = False

        if len(self.obstacles) > 4:
            self.deletecrates = True

        else:
            if self.obstacles_endtime_set:
                self.obstaclestimer += 1
            else:
                self.obstaclesdeploytime = random.randrange(100, 110)
                self.obstacles_endtime_set = True

            if self.obstaclestimer == self.obstaclesdeploytime:
                self.obstaclestimer = 0
                self.obstacles_endtime_set = False
                ob_list = [GameSprites.BAT(), GameSprites.CRATES()]
                ob = ob_list[random.randint(0, 1)]
                self.obstacles.append(ob)
                self.obstacle_list.add(ob)

        print(len(self.obstacles))

    def Move_obstacle(self):


        self.__Create_obstacle()
        for obstacles in self.obstacle_list:
            if isinstance(obstacles, GameSprites.BAT):
                obstacles.flap()
                obstacles.rect.x -= 50
            else:
                obstacles.rect.x -= 25
            if obstacles.rect.x < -50 and not self.deletecrates:
                obstacles.rect.x = Asset.S_WIDTH -50
            elif obstacles.rect.x < -50 and self.deletecrates:
                self.obstacle_list.remove(obstacles)
                self.obstacles.remove(obstacles)

    def Move_Platform(self):
        for blocks in self.platform_list:
            blocks.rect.x -= 50
            if blocks.rect.x < 0:
                blocks.rect.x = Asset.S_WIDTH - 50

    def show_score(self):
        SCORE = TEXT.render("DISTANCE:" + str(self.score) + " m", True, (255, 255, 255))
        self.screen.blit(SCORE, (0,0))

    def show_menu(self):

        text = pygame.font.SysFont("ARIAL",120,True)
        menutext = text.render("PRESS P TO PLAY",True,(255,255,255))
        self.screen.blit(menutext,(150,300))
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.menu = False
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_p:
                    self.game = True

    def instructions(self):
        global index
        rect = (Asset.S_WIDTH, 0, 450, Asset.S_HEIGHT)
        pygame.draw.rect(self.screen, (255, 255, 255), rect, 2)
        instruct = pygame.font.SysFont("arial", 30, True)

        display = "INSTRUCTIONS:"
        t = instruct.render(display, True, (255, 255, 255))
        self.screen.blit(t, (Asset.S_WIDTH+10, 20))

        instruct = pygame.font.SysFont("arial", 20, True)
        display = "1.PRESS SPACE TO JUMP"
        t = instruct.render(display, True, (255, 255, 255))
        self.screen.blit(t, (Asset.S_WIDTH+10, 60))

        display = "2.PRESS DOWN ARROW KEY TO SLIDE"
        t = instruct.render(display, True, (255, 255, 255))
        self.screen.blit(t, (Asset.S_WIDTH+10, 90))

        display = "3.PRESS LEFT OR RIGHT ARROW KEY TO MOVE "
        t = instruct.render(display, True, (255, 255, 255))
        self.screen.blit(t, (Asset.S_WIDTH+10, 120))

        display = "4.PRESS 'P' TO PAUSE OR PLAY"
        t = instruct.render(display, True, (255, 255, 255))
        self.screen.blit(t, (Asset.S_WIDTH + 10, 150))

        instruct = pygame.font.SysFont("arial", 37, True)

        display = "DESIGNED AND DEVELOPED"
        t = instruct.render(display, True, color[index])
        self.screen.blit(t, (Asset.S_WIDTH + 10, 180))

        display = "BY"
        t = instruct.render(display, True, color[index])
        self.screen.blit(t, (Asset.S_WIDTH + 200, 250))

        display = "AADITYA PRABU K"
        t = instruct.render(display, True, color[index])
        self.screen.blit(t, (Asset.S_WIDTH + 80, 320))

        if index == len(color)-1:
            index = 0
        else:
            index+=1


    def delete_obstacles_and_reinitialize_player(self):

        for obstacles in self.obstacle_list:
            obstacles.kill()
            self.obstacle_list.remove(obstacles)
            self.obstacles.remove(obstacles)

        self.obstacle_list.clear(self.screen,pygame.Surface((Asset.S_WIDTH,Asset.S_HEIGHT)))
        self.player.rect.center = (100,-10)
        self.player.direction = 'stay'
        self.score = 0







