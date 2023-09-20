# from settings2 import *
# import pygame
# import random
# import time
# from cards import collected_cards

# pygame.init()
# pygame.joystick.init()

# # Initialize Pygame
# SCREEN_WIDTH = WIDTH
# SCREEN_HEIGHT = HEIGHT
# WHITE = (255, 255, 255)
# RED = (255, 0, 0)
# ORANGE = (255, 165, 0)
# YELLOW = (255, 255, 0)
# GREEN = (0, 128, 0)
# BLUE = (0, 0, 255)
# VIOLET = (238, 130, 238)
# BLACK = (255, 255, 255)
# class Player(object):
#     def __init__(self, x, y):
#         self.playerX = x
#         self.playerY = y
#         self.player_size = 25
#         self.border_size = 5  # Add border size
#         self.color = RED  # Set the initial color to red
#         self.border_color = WHITE  # Set the initial border color to white

#     def move(self, x_speed, y_speed, game_map):
#         speed = 2

#         # Calculate the new player position based on speed
#         new_playerX = self.playerX + x_speed * speed
#         new_playerY = self.playerY + y_speed * speed

#         # Check if the new position is within the game window boundaries
#         if (
#             0 <= new_playerX <= SCREEN_WIDTH - self.player_size
#             and 0 <= new_playerY <= SCREEN_HEIGHT - self.player_size
#         ):
#             # Check for collisions with walls
#             tile_x = int(new_playerX // game_map.tile_size)
#             tile_y = int(new_playerY // game_map.tile_size)
#             if game_map.layout[tile_y][tile_x] == 0:
#                 # Update the player's position if within boundaries and no wall collision
#                 self.playerX = new_playerX
#                 self.playerY = new_playerY

#     def draw(self, screen):
#         # Draw the border around the player's position
#         pygame.draw.rect(
#             screen,
#             self.border_color,
#             pygame.Rect(
#                 self.playerX - self.border_size,
#                 self.playerY - self.border_size,
#                 self.player_size + 2 * self.border_size,
#                 self.player_size + 2 * self.border_size,
#             ),
#         )

#         # Draw the player's position (inside the border)
#         pygame.draw.rect(
#             screen,
#             self.color,
#             pygame.Rect(self.playerX, self.playerY, self.player_size, self.player_size),
#         )

# # Modify the Map class to include wall drawing and collision handling

# class Map:
#     def __init__(self):
#         # Define the map layout using a two-dimensional array
#         self.layout = [
#             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#             [1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#         ]
#         self.tile_size = 40

#     def draw(self, screen):
#         for row in range(len(self.layout)):
#             for col in range(len(self.layout[row])):
#                 tile_x = col * self.tile_size
#                 tile_y = row * self.tile_size
#                 if self.layout[row][col] == 1:
#                     pygame.draw.rect(screen, BLACK, pygame.Rect(tile_x, tile_y, self.tile_size, self.tile_size))
#                 elif self.layout[row][col] == 2:
#                     pygame.draw.rect(screen, BLUE, pygame.Rect(tile_x, tile_y, self.tile_size, self.tile_size))

# # Rainbow War Mini-Game
# def rainbow_war_mini_game(playerX, playerY, screen, joysticks):
#     deadzone_threshold = 0.2
#     player = Player(playerX, playerY)

#     # Initialize joystick axis values to zero before entering the game loop
#     x_speed = 0.0
#     y_speed = 0.0

#     running = True
#     enemies = []  # Initialize the enemies list
#     dots = []  # Initialize the dots list
#     dot_counters = {
#         RED: 0,
#         ORANGE: 0,
#         YELLOW: 0,
#         GREEN: 0,
#         BLUE: 0,
#         VIOLET: 0
#     }
#     dot_spawn_interval = 2  # Set the dot spawn interval (2 seconds)
#     enemy_speed = 1
#     enemy_spawn_interval = 5
#     time_since_last_enemy_spawn = 0.0
#     time_since_last_dot_spawn = 0.0
#     game_map = Map()
#     while running:
#         screen.fill(WHITE)

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_ESCAPE:
#                     running = False

#         x_speed = round(joysticks[0].get_axis(0), 2)  # Left stick x-axis
#         y_speed = round(joysticks[0].get_axis(1), 2)  # Left stick y-axis
        
#         x_speed = 0.0 if abs(x_speed) < deadzone_threshold else x_speed
#         y_speed = 0.0 if abs(y_speed) < deadzone_threshold else y_speed

#         player.move(x_speed, y_speed, game_map)  # Pass the game_map object


#         player_rect = pygame.Rect(player.playerX, player.playerY, player.player_size, player.player_size)

#         for enemyX, enemyY in enemies:
#             enemy_rect = pygame.Rect(enemyX, enemyY, player.player_size, player.player_size)
#             if player_rect.colliderect(enemy_rect):
#                 running = False
#                 print("You lost the Rainbow War mini-game.")

#         if time.time() - time_since_last_dot_spawn > dot_spawn_interval:
#             # Create a new dot and add it to the dots list
#             dot_colors = [RED, ORANGE, YELLOW, GREEN, BLUE, VIOLET]
#             num_dots = 10
#             dot_size = 10
#             dot_x = random.randint(0, SCREEN_WIDTH - 10)
#             dot_y = random.randint(0, SCREEN_HEIGHT - 10)
#             dot_color = random.choice(dot_colors)
#             dot_rect = pygame.Rect(dot_x, dot_y, 10, 10)
#             dots.append({"rect": dot_rect, "color": dot_color, "collected": False})
#             time_since_last_dot_spawn = time.time()

#         # Draw dots on the screen and check for collisions with the player
#         for dot in dots:
#             if not dot["collected"]:
#                 pygame.draw.ellipse(screen, dot["color"], dot["rect"])
#                 if player_rect.colliderect(dot["rect"]):
#                     dot["collected"] = True
#                     dot_counters[dot["color"]] += 1
#                     if dot_counters[dot["color"]] >= 3:
#                         dot_counters[dot["color"]] = 0
#                         if dot["color"] == RED:
#                             collected_cards.append("Red Card")
#                         elif dot["color"] == ORANGE:
#                             collected_cards.append("Orange Card")
#                         elif dot["color"] == YELLOW:
#                             collected_cards.append("Yellow Card")
#                         elif dot["color"] == GREEN:
#                             collected_cards.append("Green Card")
#                         elif dot["color"] == BLUE:
#                             collected_cards.append("Blue Card")
#                         elif dot["color"] == VIOLET:
#                             collected_cards.append("Violet Card")

#         # Draw and move enemies
#         if time.time() - time_since_last_enemy_spawn > enemy_spawn_interval:
#             enemyX = random.randint(0, SCREEN_WIDTH - player.player_size)
#             enemyY = random.randint(0, SCREEN_HEIGHT - player.player_size)
#             enemies.append((enemyX, enemyY))
#             time_since_last_enemy_spawn = time.time()

#         if time.time() - time_since_last_enemy_spawn > enemy_spawn_interval:
#             enemyX = random.randint(0, SCREEN_WIDTH - player.player_size)
#             enemyY = random.randint(0, SCREEN_HEIGHT - player.player_size)
#             enemies.append((enemyX, enemyY))
#             time_since_last_enemy_spawn = time.time()

#         for i, (enemyX, enemyY) in enumerate(enemies):
#             # Move the enemy towards the player
#             dx = player.playerX - enemyX
#             dy = player.playerY - enemyY
#             distance = max(abs(dx), abs(dy))
#             if distance > 0:
#                 # Calculate the normalized direction vector towards the player
#                 dx_normalized = dx / distance
#                 dy_normalized = dy / distance

#                 # Update the enemy position based on the normalized direction vector and enemy_speed
#                 enemyX += dx_normalized * enemy_speed
#                 enemyY += dy_normalized * enemy_speed

#                 # Update the position in the enemies list
#                 enemies[i] = (enemyX, enemyY)

#             enemy_rect = pygame.Rect(enemyX, enemyY, player.player_size, player.player_size)
#             pygame.draw.rect(screen, BLUE, enemy_rect)
#         game_map.draw(screen)
#         # Draw the player
#         pygame.draw.rect(screen, RED, player_rect)

#         pygame.display.update()

#     pygame.time.delay(2000)  # Wait for 2 seconds before exiting the mini-game

# if __name__ == "__main__":
#     print("Rainbow War Mini-Game!")
#     joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
#     screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#     playerX = SCREEN_WIDTH // 2 - 25
#     playerY = SCREEN_HEIGHT // 2 - 25
#     rainbow_war_mini_game(playerX, playerY)
#     print("You survived the Rainbow War mini-game.")
#     pygame.quit()

from settings2 import *
import pygame
import random
import time
from cards import collected_cards
import math

pygame.init()
pygame.joystick.init()

# Initialize Pygame
SCREEN_WIDTH = WIDTH
SCREEN_HEIGHT = HEIGHT
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 128, 0)
BLUE = (0, 0, 255)
VIOLET = (238, 130, 238)
def get_random_angle():
    return random.uniform(0, 2 * math.pi)

def get_random_position_away_from_player(playerX, playerY, min_distance):
    angle = get_random_angle()
    distance_from_player = random.uniform(min_distance, min_distance * 2)  # Random distance between min_distance and 2 * min_distance
    enemyX = playerX + distance_from_player * math.cos(angle)
    enemyY = playerY + distance_from_player * math.sin(angle)
    return enemyX, enemyY
class Player(object):
    def __init__(self, x, y):
        self.playerX = x
        self.playerY = y
        self.player_size = 25
        self.border_size = 5  # Add border size
        self.color = RED  # Set the initial color to red
        self.border_color = WHITE  # Set the initial border color to white

    def move(self, x_speed, y_speed):
        speed = 2

        # Calculate the new player position based on speed
        new_playerX = self.playerX + x_speed * speed
        new_playerY = self.playerY + y_speed * speed

        # Check if the new position is within the game window boundaries
        if (
            0 <= new_playerX <= SCREEN_WIDTH - self.player_size
            and 0 <= new_playerY <= SCREEN_HEIGHT - self.player_size
        ):
            # Update the player's position if within boundaries
            self.playerX = new_playerX
            self.playerY = new_playerY
    def draw(self, screen):
        # Draw the border around the player's position
        pygame.draw.rect(
            screen,
            self.border_color,
            pygame.Rect(
                self.playerX - self.border_size,
                self.playerY - self.border_size,
                self.player_size + 2 * self.border_size,
                self.player_size + 2 * self.border_size,
            ),
        )

        # Draw the player's position (inside the border)
        pygame.draw.rect(
            screen,
            self.color,
            pygame.Rect(self.playerX, self.playerY, self.player_size, self.player_size),
        )

# Rainbow War Mini-Game
def rainbow_war_mini_game(playerX, playerY, screen, joysticks):
    deadzone_threshold = 0.2
    player = Player(playerX, playerY)
    enemy_spawn_radius = 150
    # Initialize joystick axis values to zero before entering the game loop
    x_speed = 0.0
    y_speed = 0.0

    running = True
    enemies = []  # Initialize the enemies list
    dots = []  # Initialize the dots list
    dot_counters = {
        RED: 0,
        ORANGE: 0,
        YELLOW: 0,
        GREEN: 0,
        BLUE: 0,
        VIOLET: 0
    }
    dot_spawn_interval = 2  # Set the dot spawn interval (2 seconds)
    enemy_speed = .5
    enemy_spawn_interval = 5
    time_since_last_enemy_spawn = 0.0
    time_since_last_dot_spawn = 0.0

    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        x_speed = round(joysticks[0].get_axis(0), 2)  # Left stick x-axis
        y_speed = round(joysticks[0].get_axis(1), 2)  # Left stick y-axis
        
        x_speed = 0.0 if abs(x_speed) < deadzone_threshold else x_speed
        y_speed = 0.0 if abs(y_speed) < deadzone_threshold else y_speed

        player.move(x_speed, y_speed)


        player_rect = pygame.Rect(player.playerX, player.playerY, player.player_size, player.player_size)

        for enemyX, enemyY in enemies:
            enemy_rect = pygame.Rect(enemyX, enemyY, player.player_size, player.player_size)
            if player_rect.colliderect(enemy_rect):
                running = False
                print("You lost the Rainbow War mini-game.")

        if time.time() - time_since_last_dot_spawn > dot_spawn_interval:
            # Create a new dot and add it to the dots list
            dot_colors = [RED, ORANGE, YELLOW, GREEN, BLUE, VIOLET]
            num_dots = 10
            dot_size = 10
            dot_x = random.randint(0, SCREEN_WIDTH - 10)
            dot_y = random.randint(0, SCREEN_HEIGHT - 10)
            dot_color = random.choice(dot_colors)
            dot_rect = pygame.Rect(dot_x, dot_y, 10, 10)
            dots.append({"rect": dot_rect, "color": dot_color, "collected": False})
            time_since_last_dot_spawn = time.time()

        # Draw dots on the screen and check for collisions with the player
        for dot in dots:
            if not dot["collected"]:
                pygame.draw.ellipse(screen, dot["color"], dot["rect"])
                if player_rect.colliderect(dot["rect"]):
                    dot["collected"] = True
                    dot_counters[dot["color"]] += 1
                    if dot_counters[dot["color"]] >= 3:
                        dot_counters[dot["color"]] = 0
                        if dot["color"] == RED:
                            collected_cards.append("Red Card")
                        elif dot["color"] == ORANGE:
                            collected_cards.append("Orange Card")
                        elif dot["color"] == YELLOW:
                            collected_cards.append("Yellow Card")
                        elif dot["color"] == GREEN:
                            collected_cards.append("Green Card")
                        elif dot["color"] == BLUE:
                            collected_cards.append("Blue Card")
                        elif dot["color"] == VIOLET:
                            collected_cards.append("Violet Card")

        # Draw and move enemies
        if time.time() - time_since_last_enemy_spawn > enemy_spawn_interval:
            enemyX, enemyY = get_random_position_away_from_player(player.playerX, player.playerY, enemy_spawn_radius)

            # Make sure the enemy's position is within the game window boundaries
            enemyX = max(min(enemyX, SCREEN_WIDTH - player.player_size), 0)
            enemyY = max(min(enemyY, SCREEN_HEIGHT - player.player_size), 0)

            enemies.append((enemyX, enemyY))
            time_since_last_enemy_spawn = time.time()
        if time.time() - time_since_last_enemy_spawn > enemy_spawn_interval:
            enemyX = random.randint(0, SCREEN_WIDTH - player.player_size)
            enemyY = random.randint(0, SCREEN_HEIGHT - player.player_size)
            enemies.append((enemyX, enemyY))
            time_since_last_enemy_spawn = time.time()

        for i, (enemyX, enemyY) in enumerate(enemies):
            # Move the enemy towards the player
            dx = player.playerX - enemyX
            dy = player.playerY - enemyY
            distance = max(abs(dx), abs(dy))
            if distance > 0:
                # Calculate the normalized direction vector towards the player
                dx_normalized = dx / distance
                dy_normalized = dy / distance

                # Update the enemy position based on the normalized direction vector and enemy_speed
                enemyX += dx_normalized * enemy_speed
                enemyY += dy_normalized * enemy_speed

                # Update the position in the enemies list
                enemies[i] = (enemyX, enemyY)

            enemy_rect = pygame.Rect(enemyX, enemyY, player.player_size, player.player_size)
            pygame.draw.rect(screen, BLUE, enemy_rect)

        # Draw the player
        pygame.draw.rect(screen, RED, player_rect)

        pygame.display.update()

    pygame.time.delay(2000)  # Wait for 2 seconds before exiting the mini-game

if __name__ == "__main__":
    print("Rainbow War Mini-Game!")
    joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    playerX = SCREEN_WIDTH // 2 - 25
    playerY = SCREEN_HEIGHT // 2 - 25
    rainbow_war_mini_game(playerX, playerY)
    print("You survived the Rainbow War mini-game.")
    pygame.quit()