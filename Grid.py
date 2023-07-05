import pygame

from Color import Colors


class Grid:
    def __init__(self):
        self.numberOfRows = 20
        self.numberOfColumns = 10
        self.cellSize = 30
        self.grid = [[0 for j in range(self.numberOfColumns)] for i in range(self.numberOfRows)]
        self.colors = Colors.getCellColors()

    def printGrid(self):
        for row in range(self.numberOfRows):
            for column in range(self.numberOfColumns):
                print(self.grid[row][column], end=" ")
            print()

    def draw(self, screen):
        for row in range(self.numberOfRows):
            for column in range(self.numberOfColumns):
                cellValue = self.grid[row][column]
                cellRect = pygame.Rect(column * self.cellSize + 11, row * self.cellSize + 11, self.cellSize - 1,
                                       self.cellSize - 1)
                pygame.draw.rect(screen, self.colors[cellValue], cellRect)

    def isInside(self, row, column):
        if row >= 0 and row < self.numberOfRows and column >= 0 and column < self.numberOfColumns:
            return True
        return False

    def isEmpty(self, row, column):
        if self.grid[row][column] == 0:
            return True
        return False

    def isRowFull(self, row):
        for column in range(self.numberOfColumns):
            if self.grid[row][column] == 0:
                return False
        return True

    def clearRow(self, row):
        for column in range(self.numberOfColumns):
            self.grid[row][column] = 0

    def moveRowDown(self, row, numberOfRows):
        for column in range(self.numberOfColumns):
            self.grid[row + numberOfRows][column] = self.grid[row][column]
            self.grid[row][column] = 0

    def clearFullRows(self):
        completed = 0
        for row in range(self.numberOfRows - 1, 0, -1):
            if self.isRowFull(row):
                self.clearRow(row)
                completed += 1
            elif completed > 0:
                self.moveRowDown(row, completed)
        return completed

    def reset(self):
        for row in range(self.numberOfRows):
            for column in range(self.numberOfColumns):
                self.grid[row][column] = 0
