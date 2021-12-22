import pygame
from pygame.locals import *
from Piece_classes import PawnClass, KnightClass, BishopClass, RookClass, QueenClass, KingClass

# set colour tuples as variables
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
RED = (255, 0, 0)
LIGHT_BROWN = (159, 129, 112)

def create_chess_board_squares():
    chess_board_squares = []
    for i in range(8):
        for j in range(8):
            if i%2==0:
                if j%2 == 0:
                    color = WHITE
                else:
                    color = LIGHT_BROWN
            else:
                if j%2 == 0:
                    color = LIGHT_BROWN
                else:
                    color = WHITE
            x_loc = 100+(100*j)
            y_loc = 100+(100*i)
            chess_board_squares.append((Rect(x_loc, y_loc, 100, 100), color))
    return chess_board_squares

# run the function and obtain list of chess board squares as Rects
chess_board_squares = create_chess_board_squares()

# set screen size
screen = pygame.display.set_mode((1000, 1000))

# row letters (used for pawns)
row_letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
# knight bishop rook letters
kbr_letters = ('q', 'k')
def create_piece_instances():
    black_piece_dict = {}
    black_piece_images_dict = {}
    black_piece_rects_dict = {}
    # Pawns
    for i in range(len(row_letters)):
        black_piece_dict['Pawn_' + row_letters[i]] = PawnClass(150+100*i, 750, 'BLACK')
        img_temp_ = pygame.image.load(f'/Users/jackkelly/OneDrive/Python_Projects/Chess/Pieces/Black_Pawn.png')
        black_piece_images_dict['img_Pawn_' + row_letters[i]] = pygame.transform.scale(img_temp_, (100, 100))
        black_piece_images_dict['img_Pawn_' + row_letters[i]].convert()
        black_piece_rects_dict['rect_Pawn_' + row_letters[i]] = black_piece_images_dict['img_Pawn_' + row_letters[i]].get_rect()
        black_piece_rects_dict['rect_Pawn_' + row_letters[i]].center = 150+100*i, 750
    # Knights
    for i in range(len(kbr_letters)):
        black_piece_dict['Knight_' + kbr_letters[i]] = KnightClass(250+ 500*i, 850, 'Black')
        img_temp_ = pygame.image.load(f'/Users/jackkelly/OneDrive/Python_Projects/Chess/Pieces/Black_Knight.png')
        black_piece_images_dict['img_Knight_' + kbr_letters[i]] = pygame.transform.scale(img_temp_, (100, 100))
        black_piece_images_dict['img_Knight_' + kbr_letters[i]].convert()
        black_piece_rects_dict['rect_Knight_' + kbr_letters[i]] = black_piece_images_dict['img_Knight_' + kbr_letters[i]].get_rect()
        black_piece_rects_dict['rect_Knight_' + kbr_letters[i]].center = 250+ 500*i, 850
    # Bishops
    for i in range(len(kbr_letters)):
        black_piece_dict['Bishop_' + kbr_letters[i]] = BishopClass(350+ 300*i, 850, 'Black')
        img_temp_ = pygame.image.load(f'/Users/jackkelly/OneDrive/Python_Projects/Chess/Pieces/Black_Bishop.png')
        black_piece_images_dict['img_Bishop_' + kbr_letters[i]] = pygame.transform.scale(img_temp_, (100, 100))
        black_piece_images_dict['img_Bishop_' + kbr_letters[i]].convert()
        black_piece_rects_dict['rect_Bishop_' + kbr_letters[i]] = black_piece_images_dict['img_Bishop_' + kbr_letters[i]].get_rect()
        black_piece_rects_dict['rect_Bishop_' + kbr_letters[i]].center = 350+ 300*i, 850
    # Rook
    for i in range(len(kbr_letters)):
        black_piece_dict['Bishop_' + kbr_letters[i]] = RookClass(150 + 700*i, 850, 'Black')
        img_temp_ = pygame.image.load(f'/Users/jackkelly/OneDrive/Python_Projects/Chess/Pieces/Black_Rook.png')
        black_piece_images_dict['img_Rook_' + kbr_letters[i]] = pygame.transform.scale(img_temp_, (100, 100))
        black_piece_images_dict['img_Rook_' + kbr_letters[i]].convert()
        black_piece_rects_dict['rect_Rook_' + kbr_letters[i]] = black_piece_images_dict['img_Rook_' + kbr_letters[i]].get_rect()
        black_piece_rects_dict['rect_Rook_' + kbr_letters[i]].center = 150 + 700*i, 850
    # Queen
    black_piece_dict['Queen'] = QueenClass(550, 850, 'Black')
    img_temp_ = pygame.image.load(f'/Users/jackkelly/OneDrive/Python_Projects/Chess/Pieces/Black_Queen.png')
    black_piece_images_dict['img_Queen'] = pygame.transform.scale(img_temp_, (100, 100))
    black_piece_images_dict['img_Queen'].convert()
    black_piece_rects_dict['rect_Queen'] = black_piece_images_dict['img_Queen'].get_rect()
    black_piece_rects_dict['rect_Queen'].center = 550, 850
    #King
    black_piece_dict['King'] = KingClass(450, 850, 'Black')
    img_temp_ = pygame.image.load(f'/Users/jackkelly/OneDrive/Python_Projects/Chess/Pieces/Black_King.png')
    black_piece_images_dict['img_King'] = pygame.transform.scale(img_temp_, (100, 100))
    black_piece_images_dict['img_King'].convert()
    black_piece_rects_dict['rect_King'] = black_piece_images_dict['img_King'].get_rect()
    black_piece_rects_dict['rect_King'].center = 450, 850

    return black_piece_dict, black_piece_images_dict, black_piece_rects_dict

black_piece_dict, black_piece_images_dict, black_piece_rects_dict = create_piece_instances()

# initally assert none of the pieces as moving
def initialise_no_moving_pieces():
    moving_Pawn_a = False
    moving_Pawn_b = False
    moving_Pawn_c = False
    moving_Pawn_d = False
    moving_Pawn_e = False
    moving_Pawn_f = False
    moving_Pawn_g = False
    moving_Pawn_h = False
    moving_Bishop_q = False
    moving_Bishop_k = False
    moving_Knight_q = False
    moving_Knight_k = False
    moving_Rook_q = False
    moving_Rook_k = False
    moving_Queen = False
    moving_King = False
    return moving_Pawn_a, moving_Pawn_b, moving_Pawn_c, moving_Pawn_d, moving_Pawn_e, moving_Pawn_f, moving_Pawn_g,\
        moving_Pawn_h, moving_Bishop_q, moving_Bishop_k, moving_Knight_q, moving_Knight_k, moving_Rook_q, moving_Rook_k,\
        moving_Queen, moving_King

moving_Pawn_a, moving_Pawn_b, moving_Pawn_c, moving_Pawn_d, moving_Pawn_e, moving_Pawn_f, moving_Pawn_g,\
        moving_Pawn_h, moving_Bishop_q, moving_Bishop_k, moving_Knight_q, moving_Knight_k, moving_Rook_q, moving_Rook_k,\
        moving_Queen, moving_King = initialise_no_moving_pieces()

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == MOUSEBUTTONDOWN:
            # if the mouse is within the image (collidepoint), set the moving flag to True for that piece
            if black_piece_rects_dict['rect_Pawn_a'].collidepoint(event.pos):
                moving_Pawn_a = True
            elif black_piece_rects_dict['rect_Pawn_b'].collidepoint(event.pos):
                moving_Pawn_b = True
            elif black_piece_rects_dict['rect_Pawn_c'].collidepoint(event.pos):
                moving_Pawn_c = True
            elif black_piece_rects_dict['rect_Pawn_d'].collidepoint(event.pos):
                moving_Pawn_d = True
            elif black_piece_rects_dict['rect_Pawn_e'].collidepoint(event.pos):
                moving_Pawn_e = True
            elif black_piece_rects_dict['rect_Pawn_f'].collidepoint(event.pos):
                moving_Pawn_f = True
            elif black_piece_rects_dict['rect_Pawn_g'].collidepoint(event.pos):
                moving_Pawn_g = True
            elif black_piece_rects_dict['rect_Pawn_h'].collidepoint(event.pos):
                moving_Pawn_h = True
            elif black_piece_rects_dict['rect_Knight_q'].collidepoint(event.pos):
                moving_Knight_q = True
            elif black_piece_rects_dict['rect_Knight_k'].collidepoint(event.pos):
                moving_Knight_k = True
            elif black_piece_rects_dict['rect_Bishop_q'].collidepoint(event.pos):
                moving_Bishop_q = True
            elif black_piece_rects_dict['rect_Bishop_k'].collidepoint(event.pos):
                moving_Bishop_k = True
            elif black_piece_rects_dict['rect_Rook_q'].collidepoint(event.pos):
                moving_Rook_q = True
            elif black_piece_rects_dict['rect_Rook_k'].collidepoint(event.pos):
                moving_Rook_k = True
            elif black_piece_rects_dict['rect_Queen'].collidepoint(event.pos):
                moving_Queen = True
            elif black_piece_rects_dict['rect_King'].collidepoint(event.pos):
                moving_King = True

        # if button is up we don't want any moving pieces
        elif event.type == MOUSEBUTTONUP:
            moving_Pawn_a = False
            moving_Pawn_b = False
            moving_Pawn_c = False
            moving_Pawn_d = False
            moving_Pawn_e = False
            moving_Pawn_f = False
            moving_Pawn_g = False
            moving_Pawn_h = False
            moving_Bishop_q = False
            moving_Bishop_k = False
            moving_Knight_q = False
            moving_Knight_k = False
            moving_Rook_q = False
            moving_Rook_k = False
            moving_Queen = False
            moving_King = False

        # if the mouse is being moved as the piece flag is True, move the Rect in-place (means no new object is created)
        elif event.type == MOUSEMOTION and moving_Pawn_a:
            black_piece_rects_dict['rect_Pawn_a'].move_ip(event.rel)

        elif event.type == MOUSEMOTION and moving_Pawn_b:
            black_piece_rects_dict['rect_Pawn_b'].move_ip(event.rel)

        elif event.type == MOUSEMOTION and moving_Pawn_c:
            black_piece_rects_dict['rect_Pawn_c'].move_ip(event.rel)

        elif event.type == MOUSEMOTION and moving_Pawn_d:
            black_piece_rects_dict['rect_Pawn_d'].move_ip(event.rel)

        elif event.type == MOUSEMOTION and moving_Pawn_e:
            black_piece_rects_dict['rect_Pawn_e'].move_ip(event.rel)

        elif event.type == MOUSEMOTION and moving_Pawn_f:
            black_piece_rects_dict['rect_Pawn_f'].move_ip(event.rel)

        elif event.type == MOUSEMOTION and moving_Pawn_g:
            black_piece_rects_dict['rect_Pawn_g'].move_ip(event.rel)

        elif event.type == MOUSEMOTION and moving_Pawn_h:
            black_piece_rects_dict['rect_Pawn_h'].move_ip(event.rel)

        elif event.type == MOUSEMOTION and moving_Knight_q:
            black_piece_rects_dict['rect_Knight_q'].move_ip(event.rel)

        elif event.type == MOUSEMOTION and moving_Knight_k:
            black_piece_rects_dict['rect_Knight_k'].move_ip(event.rel)

        elif event.type == MOUSEMOTION and moving_Bishop_q:
            black_piece_rects_dict['rect_Bishop_q'].move_ip(event.rel)
        
        elif event.type == MOUSEMOTION and moving_Bishop_k:
            black_piece_rects_dict['rect_Bishop_k'].move_ip(event.rel)

        elif event.type == MOUSEMOTION and moving_Rook_q:
            black_piece_rects_dict['rect_Rook_q'].move_ip(event.rel)

        elif event.type == MOUSEMOTION and moving_Rook_k:
            black_piece_rects_dict['rect_Rook_k'].move_ip(event.rel)

        elif event.type == MOUSEMOTION and moving_Queen:
            black_piece_rects_dict['rect_Queen'].move_ip(event.rel)

        elif event.type == MOUSEMOTION and moving_King:
            black_piece_rects_dict['rect_King'].move_ip(event.rel)

    # give screen a grey background
    screen.fill(GRAY)

    # draw each of the squares of the board
    for i in range(len(chess_board_squares)):
        square_coords, square_color = chess_board_squares[i]
        pygame.draw.rect(screen, square_color, square_coords)

    # attach the pieces to the red rectangles and draw
    
    for i in ('Pawn_a', 'Pawn_b', 'Pawn_c', 'Pawn_d', 'Pawn_e', 'Pawn_f', 'Pawn_g', 'Pawn_h', 'Knight_q', 'Knight_k',\
        'Bishop_q', 'Bishop_k', 'Rook_q', 'Rook_k', 'Queen', 'King'):
        screen.blit(black_piece_images_dict['img_' + i], black_piece_rects_dict['rect_' + i])
        pygame.draw.rect(screen, BLACK, black_piece_rects_dict['rect_' + i], 1)
    #update the display
    pygame.display.update()

pygame.quit()

