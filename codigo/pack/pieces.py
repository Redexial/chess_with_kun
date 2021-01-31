from .graphics import Image
from .graphics import Point
from .graphics import color_rgb
from .board import ChessBoard
from .board import Tile
import time

garbage = Tile(False, (0,0), "garbage", 0, 0, False)

class Piece:
    def __init__(self,white:bool,sprite:Image,tile:Tile):
        self.color=white
        self.tile=tile
        self.tile.hasPiece = True
        a=self.tile.figure.getCenter()
        self.image=Image(a,sprite)
        
    def movement(self,newTile:Tile)->Point:
        a_x=self.tile.figure.getCenter().x
        a_y=self.tile.figure.getCenter().y
        self.tile.hasPiece=False
        self.tile=newTile
        b_x=self.tile.figure.getCenter().x
        b_y=self.tile.figure.getCenter().y
        dx=b_x-a_x
        dy=b_y-a_y
        self.horizontal=dx/60
        self.vertical=-dy/60
        self.image.move(dx,dy)
        self.tile.hasPiece=True
        
    def __del__(self):
        print("del called")
        self.image.undraw()
        self.tile=garbage
        del self
    def capture(self,pieceCap):
        pieceCap.__del__()
        
    def mov(self, newTile:Tile, pieces:list):
        if(self.movCondition(newTile)):
            if newTile.hasPiece:
                for piece in pieces:
                    if(piece.tile == newTile):
                        if self.color!=piece.color:
                            self.capture(piece)
                            self.movement(newTile)
                            break
            else: 
                self.movement(newTile)
                
    def possibleMov(self,chessboard:list)->list:
        possibleMove=[]
        removeMoves=[]
        yStop = False
        xStop = False
        for row in chessboard:
            for tile in row:
                if self.movCondition(tile):
                    if (yStop and tile.numX == self.tile.numX)or(xStop and tile.numY == self.tile.numY):
                        continue
                    possibleMove.append(tile)
                if tile.hasPiece:
                    xDif = self.tile.numX-tile.numX
                    yDif = self.tile.numY-tile.numY
                    if xDif == 0:
                        if yDif > 0:
                            for nTile in possibleMove:
                                if nTile.numY < tile.numY and nTile.numX == tile.numX:
                                    removeMoves.append(nTile)
                        elif yDif < 0:
                            yStop = True
                    if yDif == 0:
                        if xDif > 0:
                            for nTile in possibleMove:
                                if nTile.numX < tile.numX and nTile.numY == tile.numY:
                                    removeMoves.append(nTile)
                        elif xDif < 0:
                            xStop = True

        def movFilter(a:Tile):
            if a in removeMoves:
                return False
            return True

        return list(filter(movFilter, possibleMove))
    
    def movCondition(self , newTile:Tile):
        return True
            
 
class King(Piece):
    def movCondition(self, newTile:Tile):
        return (self.tile.numX-newTile.numX==1 or self.tile.numX-newTile.numX==-1 or self.tile.numX-newTile.numX==0) and (self.tile.numY-newTile.numY==1 or self.tile.numY-newTile.numY==-1 or self.tile.numY-newTile.numY==0)

class Rook(Piece):
    def movCondition(self, newTile:Tile):
        return (self.tile.numX==newTile.numX) or (self.tile.numY==newTile.numY)
            
class Bishop(Piece):
    def movCondition(self, newTile:Tile):
        return (self.tile.numX-newTile.numX==self.tile.numY-newTile.numY) or (self.tile.numX-newTile.numX==-(self.tile.numY-newTile.numY))

class Queen(Piece):
    def movCondition(self, newTile:Tile):
        return ((self.tile.numX==newTile.numX) or (self.tile.numY==newTile.numY)) or ((self.tile.numX-newTile.numX==self.tile.numY-newTile.numY) or (self.tile.numX-newTile.numX==-(self.tile.numY-newTile.numY)))
            
class Knight(Piece):
    def knightMove(self,newTile:Tile):
        pass
        
            


