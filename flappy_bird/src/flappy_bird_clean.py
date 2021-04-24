import pygame, random

class FlappyBird:
    def __init__(self):
        pygame.init()
        
        # Game Variables
        self.clock = pygame.time.Clock()
        self.screen_width = 576
        self.screen_height = 1024
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.bird_movement = 0
        self.gravity = 0.25
        self.game_active = True

        self.bg_surface = pygame.image.load("assets/background-day.png").convert()
        self.bg_surface = pygame.transform.scale2x(self.bg_surface)

        self.floor_surface = pygame.image.load("assets/base.png").convert()
        self.floor_surface = pygame.transform.scale2x(self.floor_surface)
        self.floor_x_pos = 0

        self.green_pipe_surface = pygame.image.load("assets/pipe-green.png").convert()
        self.green_pipe_surface = pygame.transform.scale2x(self.green_pipe_surface)
        self.pipe_list = []

        self.red_pipe_surface = pygame.image.load("assets/pipe-red.png").convert()
        self.red_pipe_surface = pygame.transform.scale2x(self.red_pipe_surface)

        self.bird_surface = pygame.image.load("assets/redbird-midflap.png").convert()
        self.bird_surface= pygame.transform.scale2x(self.bird_surface)
        self.bird_rect = self.bird_surface.get_rect(center = (100, 512))

        self.SPAWNGREENPIPE = pygame.USEREVENT
        pygame.time.set_timer(self.SPAWNGREENPIPE, 1200)
        self.pipe_height = [400, 600, 800]

        pygame.display.set_caption("Flappy Bird")

        self.game_loop()
    
    def game_loop(self):
        while True:
            self.check_events()
            self.draw_background()
            
            self.pipe_list = self.move_pipe(self.pipe_list)
            self.draw_pipes(self.pipe_list)

            self.draw_floor()

            self.draw_bird()
            self.fall()

            self.check_collision(self.pipe_list)

            pygame.display.update()
            self.clock.tick(120)
        

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == self.SPAWNGREENPIPE:
                self.pipe_list.extend(self.create_pipe())
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.bird_fly()
    
    def draw_background(self):
        self.screen.blit(self.bg_surface, (0,0))

    def draw_floor(self):
        self.screen.blit(self.floor_surface, (self.floor_x_pos,900))
        self.screen.blit(self.floor_surface, (self.floor_x_pos+576, 900))
        self.floor_x_pos -= 1
        if self.floor_x_pos <= -576:
            self.floor_x_pos = 0
    
    def create_pipe(self):
        random_pipe_pos = random.choice(self.pipe_height)
        bottom_pipe = self.green_pipe_surface.get_rect(midtop = (700, random_pipe_pos))
        top_pipe = self.green_pipe_surface.get_rect(midbottom = (700, random_pipe_pos - 300))
        return bottom_pipe, top_pipe
    
    def move_pipe(self, pipes: list):
        for pipe in pipes: 
            pipe.centerx -= 5
        visible_pipes = [pipe for pipe in pipes if pipe.right > -50]
        return visible_pipes

    def draw_pipes(self, pipes: list):
        for pipe in pipes:
            if pipe.bottom >= 1024:
                self.screen.blit(self.green_pipe_surface, pipe)
            else:
                flip_pipe = pygame.transform.flip(self.green_pipe_surface, False, True)
                self.screen.blit(flip_pipe, pipe)
    
    def draw_bird(self):
        self.screen.blit(self.bird_surface, self.bird_rect)
    
    def fall(self):
        self.bird_movement += self.gravity
        self.bird_rect.centery += self.bird_movement

    def bird_fly(self):
        self.bird_movement = 0
        self.bird_movement -= 10

    def check_collision(self, pipes: list):
        for pipe in pipes:
            if self.bird_rect.colliderect(pipe):
                self.game_active = False
            if self.bird.top >= -100:
                return False

""" class for handling pipe color UNDER PROGRESS
class Pipe:
    def __init__(self, type: str, height: int):
        self.__type = type

    @property
    def type(self):
        return self.__type
"""    


if __name__ == "__main__":
    FlappyBird()
