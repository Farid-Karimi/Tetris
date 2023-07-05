import random
import pygame
from Blocks import *
from Grid import Grid


class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.currentBlock = self.getRandomBlock()
        self.nextBlock = self.getRandomBlock()
        self.gameOver = False
        self.score = 0
        self.rotate_sound = pygame.mixer.Sound("Sounds/bip.ogg")
        self.clear_sound = pygame.mixer.Sound("Sounds/line clear.ogg")
        pygame.mixer.music.load("Sounds/Child's Nightmare.ogg")
        pygame.mixer.music.play(-1)

    def updateScore(self, linesCleared, moveDownPoints):
        if linesCleared == 1:
            self.score += 100
        elif linesCleared == 2:
            self.score += 300
        elif linesCleared == 3:
            self.score += 500
        self.score += moveDownPoints

    def getRandomBlock(self):
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block

    def moveLeft(self):
        self.currentBlock.move(0, -1)
        if self.blockInside() == False or self.blockFits() == False:
            self.currentBlock.move(0, 1)

    def moveRight(self):
        self.currentBlock.move(0, 1)
        if self.blockInside() == False or self.blockFits() == False:
            self.currentBlock.move(0, -1)

    def moveDown(self):
        self.currentBlock.move(1, 0)
        if self.blockInside() == False or self.blockFits() == False:
            self.currentBlock.move(-1, 0)
            self.lockBlock()

    def lockBlock(self):
        tiles = self.currentBlock.getCellPositions()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.currentBlock.id
        self.currentBlock = self.nextBlock
        self.nextBlock = self.getRandomBlock()
        rowsCleared = self.grid.clearFullRows()
        if rowsCleared > 0:
            self.clear_sound.play()
            self.updateScore(rowsCleared, 0)
        if not self.blockFits():
            self.gameOver = True

    def reset(self):
        self.grid.reset()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.currentBlock = self.getRandomBlock()
        self.nextBlock = self.getRandomBlock()
        self.score = 0

    def blockFits(self):
        tiles = self.currentBlock.getCellPositions()
        for tile in tiles:
            if not self.grid.isEmpty(tile.row, tile.column):
                return False
        return True

    def rotate(self):
        self.currentBlock.rotate()
        if self.blockInside() == False or self.blockFits() == False:
            self.currentBlock.undoRotation()
        else:
            self.rotate_sound.play()

    def blockInside(self):
        tiles = self.currentBlock.getCellPositions()
        for tile in tiles:
            if not self.grid.isInside(tile.row, tile.column):
                return False
        return True

    def draw(self, screen):
        self.grid.draw(screen)
        self.currentBlock.draw(screen, 11, 11)

        if self.nextBlock.id == 3:
            self.nextBlock.draw(screen, 255, 290)
        elif self.nextBlock.id == 4:
            self.nextBlock.draw(screen, 255, 280)
        else:
            self.nextBlock.draw(screen, 270, 270)
