import pygame
from settings2 import *
from tile import Tile
from debug import debug
from dotsMinigame import *
from cardWarMinigame import *
# class Enemy(pygame.sprite.Sprite):
#     def __init__(self, pos, groups, obstacle_sprites, player, level):
#         super().__init__()
#         self.image = pygame.image.load('../graphics/test/enemy.png').convert_alpha()  # Updated image path
#         self.rect = self.image.get_rect(topleft=pos)
#         self.hitbox = self.rect.inflate(0, -26)
#         self.speed = 3
#         self.obstacle_sprites = obstacle_sprites
#         self.player = player
#         self.level = level
#     def collision(self, direction):
#         for sprite in self.obstacle_sprites:
#             if sprite.rect.colliderect(self.rect):
#                 if direction == 'horizontal':
#                     if self.rect.centerx < sprite.rect.centerx:
#                         self.rect.right = sprite.rect.left
#                     else:
#                         self.rect.left = sprite.rect.right
#                 elif direction == 'vertical':
#                     if self.rect.centery < sprite.rect.centery:
#                         self.rect.bottom = sprite.rect.top
#                     else:
#                         self.rect.top = sprite.rect.bottom
#         # Debugging
#         print("Enemy position after collision check:", self.rect.topleft)

    # def update(self):
    #     self.move()
        
    #     # Check for collisions with the player
    #     if pygame.sprite.collide_rect(self, self.player):
    #         print("Game Over")

    #     # Debugging
    #     print("Enemy position after update:", self.rect.topleft)
    # def move(self):
    #     direction = pygame.math.Vector2(self.player.rect.center) - pygame.math.Vector2(self.rect.center)
    #     if direction.magnitude() != 0:
    #         direction = direction.normalize()
    #     self.rect.x += direction.x * self.speed
    #     self.collision('horizontal')
    #     self.rect.y += direction.y * self.speed
    #     self.collision('vertical')

    # def collision(self, direction):
    #     if direction == 'horizontal':
    #         for sprite in self.obstacle_sprites:
    #             if sprite.rect.colliderect(self.rect):
    #                 if direction == 'horizontal':
    #                     if self.rect.centerx < sprite.rect.centerx:
    #                         self.rect.right = sprite.rect.left
    #                     else:
    #                         self.rect.left = sprite.rect.right

    #     if direction == 'vertical':
    #         for sprite in self.obstacle_sprites:
    #             if sprite.rect.colliderect(self.rect):
    #                 if direction == 'vertical':
    #                     if self.rect.centery < sprite.rect.centery:
    #                         self.rect.bottom = sprite.rect.top
    #                     else:
    #                         self.rect.top = sprite.rect.bottom

    # def update(self):
    #     self.move()
        
    #     # Check for collisions with the player
    #     if pygame.sprite.collide_rect(self, self.player):
    #         print("Game Over")
class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = YsortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        self.player = None  # Initialize player attribute to None
        self.enemy = None   # Initialize enemy attribute to None
        self.create_map()
        self.mini_game_triggered = False
        self.mini_game_triggered2 = False

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'X':
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites])
                if col == 'P':
                    self.player = Player((x, y), self.visible_sprites, self.obstacle_sprites)
                    self.visible_sprites.set_player(self.player)  # Set the player attribute in YsortCameraGroup
                if col == 'M':
                    self.mini_tile_pos = (x, y)
                if col == 'Q':
                    self.mini_tile_pos2 = (x, y)

        # Create the enemy after the player so that it is sorted correctly by YsortCameraGroup
        # if self.player is not None:
        #     self.enemy = Enemy((100, 100), [self.visible_sprites, self.obstacle_sprites], self.obstacle_sprites, self.player, self)
        #     self.enemy_group = pygame.sprite.Group(self.enemy)

    def run(self):
        self.visible_sprites.update()  # Update the player and obstacles
        if self.enemy is not None:
            self.enemy_group.update()   # Update the enemy if it exists
        self.visible_sprites.custom_draw(self.player)  # Draw the player and obstacles
        if self.enemy is not None:
            self.enemy_group.draw(self.display_surface)  # Draw the enemy if it exists
        pygame.display.flip()
        joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

        if not self.mini_game_triggered and self.player.rect.colliderect(pygame.Rect(self.mini_tile_pos, (TILESIZE, TILESIZE))):
            self.mini_game_triggered = True
            print("Entering Rainbow War Mini-Game!")
            player_x, player_y = self.player.rect.topleft
            rainbow_war_mini_game(player_x, player_y, self.display_surface, joysticks)
            print("You survived the Rainbow War Mini-Game!")
            self.mini_game_triggered2 = False
        
        
        if not self.mini_game_triggered2 and self.player.rect.colliderect(pygame.Rect(self.mini_tile_pos2, (TILESIZE, TILESIZE))):
            self.mini_game_triggered2 = True
            print("Entering Card War Mini-Game!")
            player_cards = [get_random_player_card() for _ in range(4)]
            computer_cards = [get_random_color_card() for _ in range(4)]
            card_war_game(player_cards, computer_cards)
            print("You survived the Card War Mini-Game!")
            self.mini_game_triggered = False

class YsortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()
        self.player = None  # Initialize player attribute to None

    def set_player(self, player):
        self.player = player

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

    def custom_draw(self, player):
        self.offset.x = player.rect.x - self.half_width
        self.offset.y = player.rect.y - self.half_height

        sprites_sorted = sorted(self.sprites(), key=lambda sprite: sprite.rect.centery)

        for sprite in sprites_sorted:
            offset_pos = sprite.rect.topleft - self.offset
            # Draw the sprite image at the correct position based on its self.rect attribute
            self.display_surface.blit(sprite.image, offset_pos)
class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites, player=None, level=None):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -26)
        # movement
        self.direction = pygame.math.Vector2()
        self.speed = 5
        self.obstacle_sprites = obstacle_sprites
        pygame.joystick.init()
        joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
        if joysticks:
            self.joystick = joysticks[0]
            self.joystick.init()

    def input(self):
        # Keyboard input
        keys = pygame.key.get_pressed()
        self.direction = pygame.math.Vector2()
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0

        # Joystick input
        if hasattr(self, 'joystick'):
            joystick_x = round(self.joystick.get_axis(0), 2)  # Left stick x-axis
            joystick_y = round(self.joystick.get_axis(1), 2)  # Left stick y-axis
            if abs(joystick_x) > 0.1 or abs(joystick_y) > 0.1:
                self.direction.x = joystick_x
                self.direction.y = joystick_y

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.rect.x += self.direction.x * speed
        self.collision('horizontal')
        self.rect.y += self.direction.y * speed
        self.collision('vertical')

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0:
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:
                        self.rect.left = sprite.rect.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0:
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom

    def update(self):
        self.input()
        self.move(self.speed)

# Rest of your code...
