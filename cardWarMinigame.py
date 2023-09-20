import pygame
import random
import sys
from cards import collected_cards
from settings2 import *


# Initialize Pygame

class Minigame1(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super(). __init__(groups)
        self.image = pygame.image.load('../graphics/test/rock.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -10)
    
# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Initialize Pygame screen
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Card War Game")

def draw_text(surface, text, font, color, x, y):
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (x, y))

def get_random_color_card():
    return random.choice(["Red Card", "Yellow Card", "Orange Card", "Blue Card", "Green Card", "Violet Card"])
def get_random_player_card():
    return random.choice(collected_cards)


def card_war_game(player_cards, computer_cards):
    pygame.init()
    pygame.font.init()
    card_values = {
    "Red Card": 1,
    "Orange Card": 2,
    "Yellow Card": 3,
    "Green Card": 4,
    "Blue Card": 5,
    "Violet Card": 6
    }

    card_priorities = {
        "Red Card": 1,
        "Orange Card": 2,
        "Yellow Card": 1,
        "Green Card": 2,
        "Blue Card": 1,
        "Violet Card": 2
    }
    # Set up the game interface
    window_size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Card War Game")
    font = pygame.font.Font(None, 30)

    player_score = 0
    computer_score = 0

    pygame.joystick.init()
    joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
    if joysticks:
        joystick = joysticks[0]
        joystick.init()

    while len(player_cards) > 0 and len(computer_cards) > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        player_choice_1 = get_random_player_card()
        player_choice_2 = get_random_player_card()
        # Display the choices and prompt the player to choose one
        screen.fill((255, 255, 255))
        draw_text(screen, "Choose a card to play:", font, (0, 0, 0), 50, 100)
        draw_text(screen, f"1: {player_choice_1}", font, (0, 0, 0), 50, 150)
        draw_text(screen, f"2: {player_choice_2}", font, (0, 0, 0), 50, 180)
        pygame.display.flip()

        # Wait for player's choice (either 1 or 2)
        player_choice = None
        while player_choice not in [1, 2]:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.JOYBUTTONDOWN:
                    if joystick.get_button(0):  # Button 1 on the joystick
                        player_choice = 1
                    elif joystick.get_button(1):  # Button 2 on the joystick
                        player_choice = 2
        # Use the chosen card to play the round
        if player_choice == 1:
            player_card = player_choice_1
        else:
            player_card = player_choice_2

        computer_card = computer_cards.pop(0)
        player_value = card_values.get(player_card, 0)
        computer_value = card_values.get(computer_card, 0)
        player_priority = card_priorities.get(player_card, 0)
        computer_priority = card_priorities.get(computer_card, 0)

        if player_priority > computer_priority:
            player_score += 1
            result_text = "You win this round!"
        elif player_priority < computer_priority:
            computer_score += 1
            result_text = "Computer wins this round!"
        else:
            # If priorities are equal, compare card values
            if player_value > computer_value:
                player_score += 1
                result_text = "You win this subround!"
            elif player_value < computer_value:
                computer_score += 1
                result_text = "Computer wins this subround!"
            else:
                result_text = "It's a tie!"

        # Draw the cards and result on the screen
        screen.fill((255, 255, 255))
        draw_text(screen, f"Your card: {player_card}", font, (0, 0, 0), 50, 100)
        draw_text(screen, f"Computer's card: {computer_card}", font, (0, 0, 0), 50, 150)
        draw_text(screen, result_text, font, (0, 0, 0), 50, 200)
        draw_text(screen, f"Your score: {player_score}", font, (0, 0, 0), 50, 250)
        draw_text(screen, f"Computer score: {computer_score}", font, (0, 0, 0), 50, 280)

        pygame.display.flip()

        pygame.time.delay(2000)  # Wait for 1 second before showing the next round

    pygame.time.delay(1000)  # Wait for 2 seconds before displaying the final result

    if player_score > computer_score:
        final_text = "Congratulations, you won the card game!"
    elif player_score < computer_score:
        final_text = "Computer won the card game."
    else:
        final_text = "The game ended in a tie."

    # Draw the final result on the screen
    screen.fill((255, 255, 255))
    draw_text(screen, final_text, font, (0, 0, 0), 50, 150)
    pygame.display.flip()

def start_mini_game():
    # Save the original window size and caption
    original_size = screen.get_size()
    original_caption = pygame.display.get_caption()

    # Set the mini-game window size and caption
    pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Mini-Game: Card War")

    # Start the mini-game with new window size
    player_cards = [get_random_color_card() for _ in range(4)]
    computer_cards = [get_random_color_card() for _ in range(4)]
    card_war_game(player_cards, computer_cards)

    # Restore the original window size and caption
    pygame.display.set_mode(original_size)
    pygame.display.set_caption(original_caption)

# Example usage of the card war game
if __name__ == "__main__":
    player_cards = [get_random_color_card() for _ in range(4)]
    computer_cards = [get_random_color_card() for _ in range(4)]
    card_war_game(player_cards, computer_cards)
    pygame.quit()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # If the mini-game is completed, show the final result and wait for 2 seconds
        start_mini_game()
        pygame.time.delay(2000)