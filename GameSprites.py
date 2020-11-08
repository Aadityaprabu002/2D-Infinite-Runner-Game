import pygame
import Asset

pygame.init()


class COWBOY(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # COW BOY DATA

        self.vy = 50
        self.gravity = 25
        self.direction = 'stay'

        # COW BOY ACTION VARIABLES
        self.jump = False
        self.run = True
        self.slide = False
        self.onland = False

        # COW BOY SPRITES AND DATA
        self.__spritesize = [150, 150]
        self.image = pygame.image.load(Asset.run_path + "\\" + Asset.COWBOY_RUN[0])
        self.image = pygame.transform.scale(self.image, self.__spritesize)
        self.rect = self.image.get_rect()
        self.rect.center = (100, -10)
        self.mask = pygame.mask.from_surface(self.image)

        self.run_frame = 0
        self.jump_frame = 0
        self.slide_frame = 0
        self.slide_timer = 0


    def set_player_coordinates(self, x, y, action):

        if action == 'r':
            if self.rect.centerx <=100 and x < 0:
                pass
            elif self.rect.centerx >=700 and x > 0:
                pass
            else:
                self.rect.centerx += x

        elif action == 'j':
            self.rect.centery -= y

        elif action == 's':
            self.rect.centerx = x
            self.rect.centery = y

    def get_player_coordinates(self):

        return self.rect.centerx, self.rect.centery

    def run_(self):

        self.set_player_sprite('r')
        
        x, y = self.get_player_coordinates()
        if self.direction == 'r':
            self.set_player_coordinates(20, y, 'r')
        elif self.direction == 'l':
            self.set_player_coordinates(-20, y, 'r')

        if not self.jump:
            self.run_frame += 1
            if self.run_frame >= len(Asset.COWBOY_RUN):
                self.run_frame = 0

    def jump_(self):

        self.set_player_sprite('j')

        x, y = self.get_player_coordinates()

        if self.jump_frame < 5:
            self.set_player_coordinates(x, self.vy, 'j')

        self.jump_frame += 1
        if self.jump_frame >= len(Asset.COWBOY_JUMP):
            self.jump = False
            self.run = True
            self.slide = False
            self.jump_frame = 0

    def slide_(self):

        self.set_player_sprite('s')

        x, y = self.get_player_coordinates()

        if self.slide_timer == 0:
            self.set_player_coordinates(x, y + 20, 's')

        self.slide_frame += 1
        if self.slide_frame >= len(Asset.COWBOY_SLIDE):
            self.slide_frame = 0

        self.slide_timer += 1
        if self.slide_timer == 5:
            self.slide_timer = 0
            self.jump = False
            self.run = True
            self.slide = False
            self.set_player_coordinates(x, y - 20, 's')
        # else:
        # player.jump = False

    def set_player_sprite(self,  action):
        sprite = None

        if action == 'j':
            sprite = pygame.image.load(Asset.jump_path + "\\" + Asset.COWBOY_JUMP[self.jump_frame])
            sprite = pygame.transform.scale(sprite, self.__spritesize)

        elif action == 's':
            sprite = pygame.image.load(Asset.slide_path + "\\" + Asset.COWBOY_SLIDE[self.slide_frame])
            sprite = pygame.transform.scale(sprite, (130, 130))

        elif action == 'r':
            sprite = pygame.image.load(Asset.run_path + "\\" + Asset.COWBOY_RUN[self.run_frame])
            sprite = pygame.transform.scale(sprite, self.__spritesize)

        self.image = sprite

    def gravity_pull(self):
        self.rect.centery += self.gravity

    def __del__(self):
        pygame.quit()


class PLATFORM(pygame.sprite.Sprite):

    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image, [50, 50])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class CRATES(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(Asset.crates)
        self.image = pygame.transform.scale(self.image, [50, 50])
        self.rect = self.image.get_rect()
        self.rect.x = Asset.S_WIDTH -50
        self.rect.y = Asset.S_HEIGHT - 190
        self.mask = pygame.mask.from_surface(self.image)


class BAT(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(Asset.bat_path1)
        self.image = pygame.transform.scale(self.image, [50, 50])
        self.rect = self.image.get_rect()
        self.rect.x = Asset.S_WIDTH - 50
        self.rect.y = Asset.S_HEIGHT - 310
        self.frame = 1
        self.mask = pygame.mask.from_surface(self.image)

    def flap(self):
        if self.frame == 1:
            self.frame = 2
            self.image = pygame.image.load(Asset.bat_path2)
            self.image = pygame.transform.scale(self.image, [50, 50])
        else:
            self.frame = 1
            self.image = pygame.image.load(Asset.bat_path1)
            self.image = pygame.transform.scale(self.image, [50, 50])

