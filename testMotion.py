import pygame

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

class Player(object):
    def __init__(self):
        self.player = pygame.rect.Rect((300, 400, 50, 50))
        self.color = "white"

    def move(self, x_speed, y_speed):
        self.player.move_ip((x_speed, y_speed))

    def change_color(self, color):
        self.color = color

    def draw(self, game_screen):
        pygame.draw.rect(game_screen, self.color, self.player)

pygame.init()
player = Player()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.JOYBUTTONDOWN:
            if pygame.joystick.Joystick(0).get_button(0):
                player.change_color("blue")
            elif pygame.joystick.Joystick(0).get_button(1):
                player.change_color("red")
            elif pygame.joystick.Joystick(0).get_button(2):
                player.change_color("yellow")
            elif pygame.joystick.Joystick(0).get_button(3):
                player.change_color("green")

    # Get the x and y axis values
    x_speed = round(pygame.joystick.Joystick(0).get_axis(0), 2)  # Left stick x-axis
    y_speed = round(pygame.joystick.Joystick(0).get_axis(1), 2)  # Left stick y-axis
    player.move(x_speed * 5, y_speed * 5)

    screen.fill((0, 0, 0))
    player.draw(screen)
    pygame.display.update()

    clock.tick(60)  # Set the frame rate to 60 frames per second
