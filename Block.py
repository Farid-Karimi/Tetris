import pygame

from Color import Colors
from Position import Position


class Block:
	def __init__(self, id):
		self.id = id
		self.cells = {}
		self.cellSize = 30
		self.rotationState = 0
		self.rowOffset = 0
		self.columnOffset = 0
		self.colors = Colors.getCellColors()

	def move(self, rows, columns):
		self.rowOffset += rows
		self.columnOffset += columns

	def getCellPositions(self):
		tiles = self.cells[self.rotationState]
		moved_tiles = []
		for position in tiles:
			position = Position(position.row + self.rowOffset, position.column + self.columnOffset)
			moved_tiles.append(position)
		return moved_tiles

	def rotate(self):
		self.rotationState += 1
		if self.rotationState == len(self.cells):
			self.rotationState = 0

	def undoRotation(self):
		self.rotationState -= 1
		if self.rotationState == -1:
			self.rotationState = len(self.cells) - 1

	def draw(self, screen, offset_x, offset_y):
		tiles = self.getCellPositions()
		for tile in tiles:
			tile_rect = pygame.Rect(offset_x + tile.column * self.cellSize,offset_y + tile.row * self.cellSize, self.cellSize - 1, self.cellSize - 1)
			pygame.draw.rect(screen, self.colors[self.id], tile_rect)