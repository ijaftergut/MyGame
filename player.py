import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -26)
        # movement
        self.direction = pygame.math.Vector2()
        self.speed = 3
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
        joystick_x = round(self.joystick.get_axis(0), 2)  # Left stick x-axis
        joystick_y = round(self.joystick.get_axis(1), 2)  # Left stick y-axis
        if abs(joystick_x) > 0.1 or abs(joystick_y) > 0.1:
            self.direction.x = joystick_x
            self.direction.y = joystick_y
        else:
            self.direction.x = 0
            self.direction.y = 0
        
        
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
