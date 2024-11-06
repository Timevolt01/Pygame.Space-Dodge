import pygame
import time
import random

pygame.font.init()


WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BG = pygame.transform.scale(pygame.image.load("./bg.jpg"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 65

PLAYER_VELOCITY = 4

STAR_WIDTH = 10
STAR_HEIGHT = 20

STAR_VELOCITY = 3

FONT = pygame.font.SysFont("comicsans", 25)
FONT1 = pygame.font.SysFont("comicsans", 50)

pygame.display.set_caption("Space Dodge")


def draw(player, elapsed_time, stars):
    WIN.blit(BG, (0, 0))

    text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(text, (10, 10))

    pygame.draw.rect(WIN, "blue", player)

    for star in stars:
        pygame.draw.rect(WIN, "yellow", star)

    pygame.display.update()


def main():
    run = True
    
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT,
                         PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    star_add_increment = 2000
    star_count = 0

    stars = []
    hit = False

    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if star_count > star_add_increment:
            for i in range(random.randint(round(elapsed_time/2), round(elapsed_time))):  
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT,
                                    STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)

            star_add_increment = max(500, star_add_increment - 50)
            star_count = 0


            

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()

        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player.x - PLAYER_VELOCITY >= 0:
            player.x -= PLAYER_VELOCITY
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player.x + PLAYER_VELOCITY + player.width <= WIDTH:
            player.x += PLAYER_VELOCITY

        for star in stars[:]:
            star.y += random.randint(round(elapsed_time /2), round(elapsed_time/2)+2) # New idea set it to 50 and change star to fireball new idea
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break

        if hit:
            print(f"Your current score : {round(elapsed_time)}")
            score = FONT1.render(f"Score: {round(elapsed_time)}s", 1, "Green")
            
            WIN.blit(score, (WIDTH / 2 - score.get_width() / 2, (HEIGHT / 2 - score.get_height() / 2)-130))
            lost = FONT.render("You lost!", 1, "red")
            WIN.blit(lost, (WIDTH / 2 - lost.get_width() / 2, HEIGHT / 2 - lost.get_height() / 2))
            pygame.display.update()
            pygame.time.delay(4000)
            run = False
            break
        draw(player, elapsed_time, stars)

        if keys[pygame.K_ESCAPE] or (keys[pygame.K_LCTRL] and keys[pygame.K_w]):
            run = False
    pygame.quit()


if __name__ == "__main__":
    main()
