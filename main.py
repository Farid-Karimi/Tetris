import sys
import pygame

from Color import Colors
from Game import Game

pygame.init()
titleFont = pygame.font.Font("fonts/ARCADECLASSIC.TTF", 40)
titleFontForHS = pygame.font.Font("fonts/ARCADECLASSIC.TTF", 30)
titleFontForPause = pygame.font.Font("fonts/ARCADECLASSIC.TTF", 60)
scoreSurface = titleFont.render("Score", True, Colors.white)
nextSurface = titleFont.render("Next", True, Colors.white)
gameOverSurface = titleFontForPause.render("GAME OVER", True, Colors.white)
pauseSurface = titleFontForPause.render("PAUSED", True, Colors.white)
highScoreSurface = titleFontForHS.render("High Score", True, Colors.white)

scoreRect = pygame.Rect(320, 55, 170, 60)
nextRect = pygame.Rect(320, 215, 170, 180)
highScoreRect = pygame.Rect(320, 500, 170, 60)

screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Python Tetris")
img = pygame.image.load('fonts/icon.png')
pygame.display.set_icon(img)

clock = pygame.time.Clock()

game = Game()

gameUpdate = pygame.USEREVENT
pygame.time.set_timer(gameUpdate, 250)

paused = False

dim_surface = pygame.Surface(screen.get_size())
dim_surface.set_alpha(100)
dim_surface.fill(Colors.black)

# Load highscore from a text file
def load_highscore():
    try:
        with open("highscore.txt", "r") as file:
            highscore = int(file.read())
    except FileNotFoundError:
        highscore = 0
    return highscore

# Save highscore to a text file
def save_highscore(highscore):
    with open("highscore.txt", "w") as file:
        file.write(str(highscore))

highscore = load_highscore()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Save highscore before exiting the game
            save_highscore(highscore)
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused
            if game.gameOver:
                game.gameOver = False
                game.reset()
            if not paused:
                if event.key == pygame.K_LEFT and game.gameOver == False:
                    game.moveLeft()
                if event.key == pygame.K_RIGHT and game.gameOver == False:
                    game.moveRight()
                if event.key == pygame.K_DOWN and game.gameOver == False:
                    game.moveDown()
                    game.updateScore(0, 1)
                if event.key == pygame.K_UP and game.gameOver == False:
                    game.rotate()
        if event.type == gameUpdate and game.gameOver == False and not paused:
            game.moveDown()

    scoreValueSurface = titleFont.render(str(game.score), True, Colors.white)
    highscoreNum = titleFont.render(str(highscore), True, Colors.white)

    screen.fill(Colors.backGround)

    pygame.draw.rect(screen, Colors.boxes, scoreRect, 0, 15)
    screen.blit(scoreValueSurface, scoreValueSurface.get_rect(centerx=scoreRect.centerx, centery=scoreRect.centery))
    pygame.draw.rect(screen, Colors.boxes, nextRect, 0, 15)
    pygame.draw.rect(screen, Colors.boxes, highScoreRect, 0, 15)
    game.draw(screen)

    if game.gameOver:
        screen.blit(dim_surface, (0, 0))
        screen.blit(gameOverSurface, ((screen.get_width() - gameOverSurface.get_width()) // 2 ,
                                      (screen.get_height() - gameOverSurface.get_height()) // 2))
        # Update highscore if the current score is higher
        if game.score > highscore:
            highscore = game.score
    if paused:
        screen.blit(dim_surface, (0, 0))
        screen.blit(pauseSurface, ((screen.get_width() - pauseSurface.get_width()) // 2,
                                   (screen.get_height() - pauseSurface.get_height()) // 2))

    screen.blit(scoreSurface, (352, 15, 50, 50))
    screen.blit(nextSurface, (367, 175, 50, 50))
    screen.blit(highScoreSurface, (325, 460, 50, 50))
    screen.blit(highscoreNum, highscoreNum.get_rect(centerx=highScoreRect.centerx, centery=highScoreRect.centery))

    pygame.display.update()
    clock.tick(60)
