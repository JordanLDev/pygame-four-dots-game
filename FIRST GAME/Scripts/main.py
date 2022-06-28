#IMPORTS THE pg PYTHON LIBRARY - OPEN SOURCE
import pygame as pg
import os

"""
THIS IS WHERE THE WINDOW SIZE IS DEFINED BY X AND Y VALUES.
THESE VALUES ARE THEN STORED IN VARIABLES AND ARE PASSED TO THE WIN VARIABLE
FRAMES PER SECOND (FPS) IS SET TO UPDATE 60 TIMES PER SECOND.
"""

WIDTH = 820
HEIGHT = 560
WIN = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('First Game')
FPS = 30

"""
=========================================================
        THIS IS THE IMPORT SECTION FOR ASSETS
=========================================================
OS.PATH.JOIN WILL HANDLE ALL TYPES OF OS PATH SEPERATORS.
---------------------------------------------------------
DO NOT USE /
=========================================================
"""
GREEN_COUNTER_IMPORT = pg.image.load(os.path.join('Assets', 'Green_Counter_V2.png'))
"""
RESIZING THE GREEN COUNTER BY USING TRANSFORM.SCALE AND OPTIONALLY ROTATING IT.
"""
counter_height = 64
counter_width = counter_height 

GREEN_COUNTER = pg.transform.scale(GREEN_COUNTER_IMPORT,(counter_width,counter_height))

RED_COUNTER_IMPORT = pg.image.load(os.path.join('Assets', 'Red_Counter_V2.png'))
RED_COUNTER = pg.transform.scale(RED_COUNTER_IMPORT,(counter_width,counter_height))

current_counter = [GREEN_COUNTER,RED_COUNTER]

icon_width = 64
icon_height = icon_width / 2

P1_TRUE_ICON_IMPORT = pg.image.load(os.path.join('Assets', 'P1_True_Icon.png'))
P1_TRUE_ICON = pg.transform.scale(P1_TRUE_ICON_IMPORT,(icon_width,icon_height))

P2_TRUE_ICON_IMPORT = pg.image.load(os.path.join('Assets', 'P2_True_Icon.png'))
P2_TRUE_ICON = pg.transform.scale(P2_TRUE_ICON_IMPORT,(icon_width,icon_height))

P1_P2_BG_ICON_IMPORT = pg.image.load(os.path.join('Assets', 'P1_P2_BG_Icon.png'))
P1_P2_BG_ICON = pg.transform.scale(P1_P2_BG_ICON_IMPORT,(icon_width * 2,icon_height))

grid_scale = counter_width
grid_border = 10
grid_offset = grid_border

col_amount = 9
row_amount = 6
total_counters = col_amount * row_amount

grid_size_width = (grid_scale+grid_border) * col_amount

grid_size_width_no_border = grid_size_width-grid_border

grid_size_height = (grid_scale+grid_border) * row_amount

grid_max_counter_width = grid_size_width_no_border - grid_scale
print(grid_size_width)

print(total_counters)

icon_bg_pos_x = grid_size_width+grid_border
icon_bg_pos_y = grid_scale+grid_border


GRID_ICON_IMPORT = pg.image.load(os.path.join('Assets', 'Grid_Icon.png'))
GRID_ICON = pg.transform.scale(GRID_ICON_IMPORT,(grid_size_width_no_border,grid_size_height-grid_border))

GRID_B_ICON_IMPORT = pg.image.load(os.path.join('Assets', 'Grid_B_Icon.png'))
GRID_BORDER_ICON = pg.transform.scale(GRID_B_ICON_IMPORT,(grid_size_width,grid_size_height))

GRID_BORDER_FILL_V = pg.transform.scale(GRID_B_ICON_IMPORT,(grid_border,grid_size_height-grid_border))
GRID_BORDER_FILL_H = pg.transform.rotate(pg.transform.scale(GRID_B_ICON_IMPORT,(grid_border,grid_scale+grid_border)),90)
GRID_BORDER_FILL_V_END = pg.transform.scale(GRID_B_ICON_IMPORT,(grid_border,grid_size_height+grid_border))

GRID_OVERLAY_S_ICON_IMPORT = pg.image.load(os.path.join('Assets', 'Grid_Overlay_Icon_Small_1.png'))
GRID_O_S_ICON = pg.transform.scale(GRID_OVERLAY_S_ICON_IMPORT,(grid_scale,grid_scale))

CURRENT_COL_ICON_IMPORT = pg.image.load(os.path.join('Assets', 'Current_Col_Icon.png'))
CURRENT_COL_ICON = pg.transform.scale(CURRENT_COL_ICON_IMPORT,(grid_scale-10,HEIGHT))

col_1 = 0
col_2 = grid_size_width / col_amount 
col_3 = col_2 * 2
col_4 = col_2 * 3
col_5 = col_2 * 4
col_6 = col_2 * 5
col_7 = col_2 * 6
col_8 = col_2 * 7
col_9 = grid_size_width_no_border-grid_scale

row_1 = (grid_size_height / row_amount) + grid_border 
row_2 = (grid_size_height / row_amount * 2) + grid_border 
row_3 = (grid_size_height / row_amount * 3) + grid_border 
row_4 = (grid_size_height / row_amount * 4) + grid_border 
row_5 = (grid_size_height / row_amount * 5) + grid_border 
row_6 = (grid_size_height / row_amount * 6) + grid_border 

rows = [row_1,row_2,row_3,row_4,row_5,row_6]
cols = [col_1,col_2,col_3,col_4,col_5,col_6,col_7,col_8,col_9]

"""
DRAW WINDOW FUNCTION ENCAPSULATES EVERYTHING THAT IS DRAWN TO THE WINDOW
THIS IS THEN CALLED FROM MAIN AND UPDATES BY THE SET FRAMES PER SECOND
"""

def draw_window(player_counter_rect,player_two_counter_rect,player_one_two_icon_rect,grid_rect,grid_overlay_s_rect,col_1_rect,PLAYER_ONE,PLAYER_TWO,placed_counter_p_one):

    WIN.fill((75,80,125))
    WIN.blit(GRID_ICON,(grid_rect.x,grid_rect.y))

    WIN.blit(P1_P2_BG_ICON, (player_one_two_icon_rect.x, player_one_two_icon_rect.y))

    if PLAYER_ONE == True:
        WIN.blit(P1_TRUE_ICON, (player_one_two_icon_rect.x, player_one_two_icon_rect.y))
        WIN.blit(current_counter[0], (player_counter_rect.x, player_counter_rect.y))
        x = grid_border+grid_border
        player_counters = [0]
        for x in player_counters:
            if placed_counter_p_one == True:
                player_counters.append(player_counter_rect.x)
                player_counters.append(player_counter_rect.y)
                print(player_counters)
                WIN.blit(current_counter[0].copy(), (player_counter_rect.x, player_counter_rect.y))
                x += 1

    elif PLAYER_TWO == True:
        WIN.blit(P2_TRUE_ICON, (player_one_two_icon_rect.x+icon_width, player_one_two_icon_rect.y))
        WIN.blit(current_counter[1], (player_two_counter_rect.x, player_two_counter_rect.y))
    
    i = grid_scale+grid_border
    for i in cols:
        if i <= grid_size_width:
            WIN.blit(GRID_O_S_ICON.copy(),(i,rows[0]))
            WIN.blit(GRID_O_S_ICON.copy(),(i,rows[1]))
            WIN.blit(GRID_O_S_ICON.copy(),(i,row_3))
            WIN.blit(GRID_O_S_ICON.copy(),(i,row_4))
            WIN.blit(GRID_O_S_ICON.copy(),(i,row_5))
            WIN.blit(GRID_O_S_ICON.copy(),(i,row_6))
            
            WIN.blit(GRID_BORDER_FILL_V.copy(),(i-grid_border,col_2+grid_border))
            WIN.blit(GRID_BORDER_FILL_V_END.copy(),(grid_size_width_no_border,grid_scale+grid_border))

            WIN.blit(GRID_BORDER_FILL_H.copy(),(i-grid_border,row_1-grid_border))
            WIN.blit(GRID_BORDER_FILL_H.copy(),(i-grid_border,row_2-grid_border))
            WIN.blit(GRID_BORDER_FILL_H.copy(),(i-grid_border,row_3-grid_border))
            WIN.blit(GRID_BORDER_FILL_H.copy(),(i-grid_border,row_4-grid_border))
            WIN.blit(GRID_BORDER_FILL_H.copy(),(i-grid_border,row_5-grid_border))
            WIN.blit(GRID_BORDER_FILL_H.copy(),(i-grid_border,row_6-grid_border))
            WIN.blit(GRID_BORDER_FILL_H.copy(),(i-grid_border,row_6+grid_scale))
            #print("i: "+ str(i))
        
    
    pg.display.update()


def main():
   
    """
    PLAYER ONE AND TWO VARS AND ASSET IMPORTS
    """
    PLAYER_ONE = True
    PLAYER_TWO = False
    #PREVIOUS COUNTER POS 10, 6
    player_counter_rect = pg.Rect(0,6,counter_width,counter_height)
    player_two_counter_rect = pg.Rect(0,6,counter_width,counter_height)
    placed_counter_p_one = False
    placed_counter_p_two = False
    placed_counter_x = 0
    player_counter_moving = False
    player_two_counter_moving = False
    counter_move_speed = 0
    counter_two_move_speed = 0

    player_one_two_icon_rect = pg.Rect(icon_bg_pos_x, icon_bg_pos_y, icon_width * 2, icon_height)
    
    grid_rect = pg.Rect(0,84,grid_size_width_no_border,grid_size_height)
    grid_overlay_s_rect = pg.Rect(10,84,grid_scale,grid_scale)
    
    col_1_rect = pg.Rect(0,0,grid_scale,grid_scale)
    
    run = True
    clock = pg.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEMOTION:
                current_m_pos = pg.mouse.get_pos()
                if current_m_pos[1] < row_2-grid_border and current_m_pos[0] < grid_size_width_no_border:
                    pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
                    if player_counter_moving or player_two_counter_moving == False:
                        if current_m_pos[0] < col_2 and current_m_pos[0]  > col_1:
                            if PLAYER_ONE == True:
                                player_counter_rect.x = col_1
                            elif PLAYER_TWO == True:
                                player_two_counter_rect.x = col_1
                            print("mouse motioned col 1")
                        elif current_m_pos[0] < col_3 and current_m_pos[0]  > col_2:
                            if PLAYER_ONE == True:
                                player_counter_rect.x = col_2
                            elif PLAYER_TWO == True:
                                player_two_counter_rect.x = col_2
                            print("mouse motioned col 2")
                        elif current_m_pos[0] < col_4 and current_m_pos[0]  > col_3:
                            if PLAYER_ONE == True:
                                player_counter_rect.x = col_3
                            elif PLAYER_TWO == True:
                                player_two_counter_rect.x = col_3
                            print("mouse motioned col 3")
                        elif current_m_pos[0] < col_5 and current_m_pos[0]  > col_4:
                            if PLAYER_ONE == True:
                                player_counter_rect.x = col_4
                            elif PLAYER_TWO == True:
                                player_two_counter_rect.x = col_4
                            print("mouse motioned col 4")
                        elif current_m_pos[0] < col_6 and current_m_pos[0]  > col_5:
                            if PLAYER_ONE == True:
                                player_counter_rect.x = col_5
                            elif PLAYER_TWO == True:
                                player_two_counter_rect.x = col_5
                            print("mouse motioned col 5")
                        elif current_m_pos[0] < col_7 and current_m_pos[0]  > col_6:
                            if PLAYER_ONE == True:
                                player_counter_rect.x = col_6
                            elif PLAYER_TWO == True:
                                player_two_counter_rect.x = col_6
                            print("mouse motioned col 6")
                        elif current_m_pos[0] < col_8 and current_m_pos[0]  > col_7:
                            if PLAYER_ONE == True:
                                player_counter_rect.x = col_7
                            elif PLAYER_TWO == True:
                                player_two_counter_rect.x = col_7
                            print("mouse motioned col 7")
                        elif current_m_pos[0] < col_9 and current_m_pos[0]  > col_8:
                            if PLAYER_ONE == True:
                                player_counter_rect.x = col_8
                            elif PLAYER_TWO == True:
                                player_two_counter_rect.x = col_8
                            print("mouse motioned col 8")
                        elif current_m_pos[0] < grid_size_width_no_border and current_m_pos[0]  > col_9:
                            if PLAYER_ONE == True:
                                player_counter_rect.x = col_9
                            elif PLAYER_TWO == True:
                                player_two_counter_rect.x = col_9
                            print("mouse motioned col 9")
                    else:
                        pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)
            if event.type == pg.MOUSEBUTTONDOWN:
                if current_m_pos[1] < row_2-grid_border and current_m_pos[0] < grid_size_width_no_border:
                    pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
                    if PLAYER_ONE == True:
                        if player_counter_rect.y < grid_size_height:
                            counter_move_speed = 1
                            player_counter_moving = True
                            print("Mouse down")
                    elif PLAYER_TWO == True:
                        if player_two_counter_rect.y < grid_size_height:
                            counter_two_move_speed = 1
                            player_two_counter_moving = True
                            print("Mouse down")
            if event.type == pg.MOUSEBUTTONUP:
                #pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)
                    #print("Mouse click")
                if player_counter_moving == True or player_two_counter_moving == True:

                        for i in rows:
                            if PLAYER_ONE == True:
                                i = 0
                                if player_counter_rect.y < grid_size_height:
                                    counter_move_speed += 1
                                    player_counter_rect.move_ip(0,counter_move_speed)            
                                    i += 1
                                elif player_counter_rect.y > grid_size_height:
                                    counter_move_speed = 0
                                    player_counter_rect.y = row_6
                                    player_counter_moving = False
                                    placed_counter_p_one = True  
                            if PLAYER_TWO == True:
                                i = 0
                                if player_two_counter_rect.y < grid_size_height:
                                    counter_two_move_speed += 1
                                    player_two_counter_rect.move_ip(0,counter_two_move_speed)            
                                    i += 1
                                elif player_two_counter_rect.y > grid_size_height:
                                    counter_two_move_speed = 0
                                    player_two_counter_rect.y = row_6
                                    player_counter_moving = False
                                    placed_counter_p_two = True
                            if player_counter_rect.y > row_1 and PLAYER_ONE == True:
                                if placed_counter_p_one == True:
                                    counter_move_speed = 0
                                    PLAYER_ONE = False
                                    player_two_counter_rect.x = col_9
                                    player_two_counter_rect.y = 6
                                    PLAYER_TWO = True
                                    placed_counter_p_two = False
                            if player_two_counter_rect.y > row_1 and PLAYER_TWO == True:
                                if placed_counter_p_two == True:
                                    counter_two_move_speed = 0
                                    PLAYER_ONE = True
                                    player_counter_rect.x = col_1
                                    player_counter_rect.y = 6  
                                    PLAYER_TWO = False
                                    placed_counter_p_one = False  
                
        print(placed_counter_p_one)
        print("Player one: " + str(PLAYER_ONE))
        print("Player two: " + str(PLAYER_TWO))
        draw_window(player_counter_rect,player_two_counter_rect,player_one_two_icon_rect,grid_rect,grid_overlay_s_rect,col_1_rect,PLAYER_ONE,PLAYER_TWO,placed_counter_p_one)
    pg.quit()


#THIS IF STATEMENT CHECKS FOR THE FILE NAME OF MAIN.PY 
#ITS TRUE THEN IT WILL CALL MAIN() ELSE IT WILL BE FALSE. 
#ENSURING MAIN() DOESN'T RUN FOREVER
if __name__ == "__main__":
    while True:
        main()
    
#