#Creatin a checker board using numpy and open cv
import numpy as np
import cv2
board_size = 8
square_size = 80
board = np.zeros((board_size, board_size), dtype=np.uint8)
board[1::2, ::2] = 255
board[::2, 1::2] = 255
board = cv2.resize(board, (square_size * board_size, square_size * board_size), interpolation=cv2.INTER_NEAREST)
image = np.zeros((square_size * board_size, square_size * board_size, 3), dtype=np.uint8)
image[:, :, 0] = board
image[:, :, 1] = board
image[:, :, 2] = board
cv2.imshow("Checkerboard", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
