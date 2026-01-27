import pygame # type: ignore[import]
import sys
from constants import *
from logger import log_state
from logger import log_event
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    
    # SCREEN SETTINGS
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0
    p_wid = SCREEN_WIDTH / 2
    p_hei = SCREEN_HEIGHT / 2

    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Shot.containers = (shots, drawable, updatable)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    player = Player(p_wid, p_hei)
    asteroidfield = AsteroidField()

    # While this inf-loop runs, the game runs.
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        

        dt = clock.tick(60) / 1000
        updatable.update(dt)
        
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
        
        
        
        
        
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
