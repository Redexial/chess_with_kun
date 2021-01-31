# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 13:39:21 2020

@author: juanc
"""

#CHESS BOARD AND TILES
#from pieces import Piece
from .graphics import Rectangle
from .graphics import color_rgb
from .graphics import Point

dimension = 60
letters=["A","B","C","D","E","F","G","H"]
numbers=[8,7,6,5,4,3,2,1]

def nomenclature(letters,numbers):
    nomenList=[]
    for letter in range(len(letters)):
        for number in range(len(numbers)):
            variable=letters[letter]+str(numbers[number])
            nomenList.append(variable)
    return nomenList



class Tile:
    def __init__(self, _white:bool,_gridPos:tuple, _name:str, _numX:int, _numY:int, hasPiece:bool):
        self.name=_name
        self.gridPos = _gridPos
        self.numY = _numX
        self.numX = _numY
        self.hasPiece=hasPiece
        self.white=_white
        #True White/ False Black
        if(_white):
            self.color = color_rgb(240,217,181)
        else:
            self.color = color_rgb(181,136,99)
        self.figure = Rectangle(Point(_gridPos[0]*dimension,_gridPos[1]*dimension),Point((_gridPos[0]+1)*dimension,(_gridPos[1]+1)*dimension))
        self.figure.setFill(self.color)
        self.figure.setOutline(self.color)
        
    def clicked(self, point:Point):
        if(point.x < self.figure.getCenter().x+30 and point.x > self.figure.getCenter().x-30 and point.y < self.figure.getCenter().y+30 and point.y > self.figure.getCenter().y-30):
            
            return self
        else:
            return None
        
    def __eq__(self,other)->bool:
        try:
            return self.numX == other.numX and self.numY == other.numY
        except AttributeError:
            return False

class ChessBoard:
    def __init__(self):
        self.color = False
        self.nameTile=nomenclature(letters,numbers)
        self.k=0
        self.j=0
        self.tiles = []
        self.figure = Rectangle(Point(210,210),Point(690,690))
        for row in range(8):
            i=0
            lista = []
            for column in range(8):
                self.color = not self.color
                lista.append(Tile(self.color, (row+3.5, column+3.5), self.nameTile[self.k],i,self.j,False))
#                self.tiles[i].figure.draw(win)
#                center=chessBoard.figure.getCenter()
#                text=Text(center,nameTile[i])
#                text.draw(win)
                i+=1
                self.k+=1
            self.j+=1
            i=0
            self.tiles.append(lista)
            self.color = not self.color
    def clicked(self, point:Point)->Tile:
        if(point.x < self.figure.getCenter().x+240 and point.x > self.figure.getCenter().x-240 and point.y < self.figure.getCenter().y+240 and point.y > self.figure.getCenter().y-240):
            
            for row in self.tiles:
                for tile in row:
                    if (tile.clicked(point)!=None):
                        return tile
        
    
        
        
    
        
    
    
        
    
    