from codigo.pack.graphics import GraphWin, Text, color_rgb
from codigo.pack.pieces import King,Rook, Queen, Bishop
from codigo.pack.board import ChessBoard

letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
numbers = [8, 7, 6, 5, 4, 3, 2, 1]
chessBoard = []
pieceArray = []


def main():
    win = GraphWin("Chess", 900, 900)
    chessBoard = ChessBoard()
    for row in chessBoard.tiles:
        for tile in row:
            tile.figure.draw(win)
            center = tile.figure.getCenter()
            text = Text(center, tile.name)
            text.draw(win)
    whiteKing = King(True, "WhiteKing.png", chessBoard.tiles[4][7])
    print(whiteKing.tile.numY)
    whiteKing.image.draw(win)
    pieceArray.append(whiteKing)
    whiteRook1 = Rook(True, "WhiteRook.png", chessBoard.tiles[0][7])
    whiteRook1.image.draw(win)
    pieceArray.append(whiteRook1)
    whiteRook2 = Rook(True, "WhiteRook.png", chessBoard.tiles[7][7])
    whiteRook2.image.draw(win)
    pieceArray.append(whiteRook2)
    whiteBishop1 = Bishop(True, "WhiteBishop.png", chessBoard.tiles[2][7])
    whiteBishop1.image.draw(win)
    pieceArray.append(whiteBishop1)
    whiteBishop2 = Bishop(True, "WhiteBishop.png", chessBoard.tiles[5][7])
    whiteBishop2.image.draw(win)
    pieceArray.append(whiteBishop2)
    whiteQueen = Queen(True, "WhiteQueen.png", chessBoard.tiles[3][7])
    whiteQueen.image.draw(win)
    pieceArray.append(whiteQueen)
    blackQueen = Queen(False, "BlackQueen.png", chessBoard.tiles[3][0])
    blackQueen.image.draw(win)
    pieceArray.append(blackQueen)

    def mov():
        click = win.getMouse()
        for piece in pieceArray:
            if chessBoard.clicked(click) == piece.tile:
                possible = piece.possibleMov(chessBoard.tiles)
                for tile in possible:
                    tile.figure.setFill(color_rgb(0, 179, 71))
                    tile.figure.setOutline(color_rgb(0, 0, 0))
                click = win.getMouse()
                piece.mov(chessBoard.clicked(click), pieceArray)
                for tile in possible:
                    tile.figure.setFill(tile.color)
                    tile.figure.setOutline(tile.color)

        return

    while True:
        mov()
    win.close()

    return

if __name__ == "__main__":
    main()
