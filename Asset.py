import os
import pygame
from pygame import mixer

pygame.init()
# PICTURES
run_path = "SPRITES\\COWBOY\\RUN"
COWBOY_RUN = os.listdir(run_path)
jump_path = "SPRITES\\COWBOY\\JUMP"
COWBOY_JUMP = os.listdir(jump_path)
slide_path = "SPRITES\\COWBOY\\SLIDE"
COWBOY_SLIDE = os.listdir(slide_path)
bg_path = "SPRITES\\BG TILESET\\png\\bg1.png"

S_HEIGHT, S_WIDTH = 700, 1400
I_W , I_H = S_WIDTH+450,S_HEIGHT
BACKGROUND = pygame.image.load(bg_path, "BACKGROUND")
BACKGROUND = pygame.transform.scale(BACKGROUND, (S_WIDTH, S_HEIGHT))
BACKGROUND2 = pygame.image.load("SPRITES\\BG TILESET\\png\\bg2.png")
BACKGROUND2 = pygame.transform.scale(BACKGROUND2, (S_WIDTH, S_HEIGHT))
STARS = pygame.image.load("SPRITES\\BG TILESET\\png\\sky.png")
STARS = pygame.transform.scale(STARS, (S_WIDTH, S_HEIGHT))
ROCKS = pygame.image.load("SPRITES\\BG TILESET\\png\\rocks.png")
ROCKS = pygame.transform.scale(ROCKS, (S_WIDTH, S_HEIGHT))

tile1_path = "SPRITES\\BG TILESET\\png\\Tiles\\Tile (2).png"
tile2_path = "SPRITES\\BG TILESET\\png\\Tiles\\Tile (5).png"
tile3_path = "SPRITES\\BG TILESET\\png\\Tiles\\Bone (2).png"
tile4_path = "SPRITES\\BG TILESET\\png\\Tiles\\Bone (3).png"

crates = "SPRITES\\BG TILESET\\png\\Objects\\Crate.png"

bat_path1 = "SPRITES\\BG TILESET\\BAT\\bat_1.png"
bat_path2 = "SPRITES\\BG TILESET\\BAT\\bat_2.png"

# SOUNDS
mixer.init()
slide = mixer.Sound("SOUNDS\\player_slide.wav")
hit = mixer.Sound("SOUNDS\\player_hit.wav")
jump = mixer.Sound("SOUNDS\\player_jump.wav")
bg_music = mixer.Sound("SOUNDS\\bgmusic.wav")

pygame.quit()
