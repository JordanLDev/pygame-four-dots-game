#IMPORTS THE pg PYTHON LIBRARY - OPEN SOURCE
import pygame as pg
import os

"""
THIS IS WHERE THE WINDOW SIZE IS DEFINED BY X AND Y VALUES.
THESE VALUES ARE THEN STORED IN VARIABLES AND ARE PASSED TO THE WIN VARIABLE
FRAMES PER SECOND (FPS) IS SET TO UPDATE 60 TIMES PER SECOND.
"""

WIDTH = 820
HEIGHT = 600
WIN = pg.display.set_mode((WIDTH,HEIGHT))

pg.display.set_caption('First Game')
FPS = 30

btn_width = 240
btn_height = 120


btn_fill = [0,1,2,3,4,5,6,7]

btn_border = 22
btn_border_amount = 4

btn_border_color = (100,70,70)
btn_rgb_default = (170,70,70)
btn_rgb_hover = (220,70,70)
btn_color = btn_rgb_default

btn_pos_x = WIDTH / 2 - (btn_width / 2)
btn_pos_y = HEIGHT / 2 - (btn_height / 2)

pg.font.init()
btn_font_size = 24
btn_font_style = pg.font.Font(pg.font.get_default_font(),btn_font_size)
btn_font_txt = 'EXIT GAME'
btn_font_color = (255,255,255)
btn_font_pos_x = 10#btn_width / 5#len(str(btn_font_txt))
btn_font_pos_y = 10

cxyc_rgb_default = (120,100,100)
cxyc_rgb_hover = (180,100,100)
cxyc_rgb_pressed = (60,100,100)
ctrl_xy_color = cxyc_rgb_default

"""
DRAW WINDOW FUNCTION ENCAPSULATES EVERYTHING THAT IS DRAWN TO THE WINDOW
THIS IS THEN CALLED FROM MAIN AND UPDATES BY THE SET FRAMES PER SECOND
"""

def draw_btn(btn_rect,btn_border_rect,btn_color,btn_font_style,btn_font_txt,btn_font_pos_x,btn_font_pos_y,
main_control_area,fine_control_area,drop_down_area,display_render_area,main_c_scale_y,ctrl_xy_color):
    WIN.fill((50,42,42))
    pg.draw.rect(WIN,(230,230,230),display_render_area)
    pg.draw.rect(WIN,(200,200,200),main_control_area)
    pg.draw.rect(WIN,ctrl_xy_color,main_c_scale_y)
    pg.draw.rect(WIN,(150,150,150),fine_control_area)
    pg.draw.rect(WIN,btn_color,btn_rect,btn_fill[0],btn_border)
    pg.draw.rect(WIN,(10,10,10),btn_border_rect,btn_fill[btn_border_amount],btn_border)
    btn_rendered_txt = pg.font.Font.render(btn_font_style,btn_font_txt,True,btn_font_color)
    WIN.blit(btn_rendered_txt,(btn_font_pos_x,btn_font_pos_y))
    
    pg.draw.rect(WIN,(180,180,180),drop_down_area)
    pg.display.update()


def button(btn_width,btn_height,btn_color,btn_pos_x,btn_pos_y,
btn_font_style,btn_font_txt,btn_font_pos_x,btn_font_pos_y,ctrl_xy_color):
    
    

    fine_control_area_w = WIDTH / 4
    main_control_width = (WIDTH - fine_control_area_w)

    moveable_border_width = HEIGHT * 0.025

    """ FILE / PANELS / ETC SECTION """
    drop_down_area = pg.Rect(0,0,WIDTH,moveable_border_width)

    """ MAIN BUTTON CONTROLS SECTION """
    main_control_area = pg.Rect(0,HEIGHT - (HEIGHT/3),main_control_width,(HEIGHT / 3 ))

    """ EXTRA AND MISC CONTROLS SECTION """
    fine_control_area = pg.Rect(main_control_area.right,(drop_down_area.centery*2),WIDTH,HEIGHT)

    display_render_area = pg.Rect(drop_down_area.y,drop_down_area.y,main_control_width,main_control_area.top)

    main_c_s_width = 100
    main_c_scale_y = pg.Rect(main_control_width /2 - (main_c_s_width /2),main_control_area.y,main_c_s_width,moveable_border_width)



    """ main button in display render area """

    btn_rect = pg.Rect(display_render_area.centerx - (btn_width / 2),display_render_area.centery - (btn_height / 2),btn_width,btn_height)
    btn_border_rect = btn_rect
    btn_clickable = False
    btn_font_pos_x = btn_rect.center[0] - (btn_font_size * (len(str(btn_font_txt)) * 0.33))#len(str(btn_font_txt))
    print(btn_font_pos_x)
    btn_font_pos_y = btn_rect.centery - (btn_font_size / 2)
    print(btn_font_pos_y)
    
    run = True
    clock = pg.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEMOTION:
                current_m_pos = pg.mouse.get_pos()
                if current_m_pos[0] >= btn_rect.x and current_m_pos[0] < btn_rect.x + btn_width and current_m_pos[1] > btn_rect.y and current_m_pos[1] < btn_rect.y + btn_height:
                    pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
                    btn_clickable = True
                    btn_color = btn_rgb_hover
                elif current_m_pos[0] >= main_c_scale_y.x and current_m_pos[0] < main_c_scale_y.x + main_c_s_width and current_m_pos[1] > main_c_scale_y.y and current_m_pos[1] < main_c_scale_y.y + moveable_border_width:
                    pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
                    btn_clickable = True
                    ctrl_xy_color = cxyc_rgb_hover
                else:
                    pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)
                    btn_clickable = False
                    btn_color = btn_rgb_default
                    ctrl_xy_color = cxyc_rgb_default
            if event.type == pg.MOUSEBUTTONDOWN:
                if btn_clickable == True:
                    if current_m_pos[0] >= btn_rect.x and current_m_pos[0] < btn_rect.x + btn_width and current_m_pos[1] > btn_rect.y and current_m_pos[1] < btn_rect.y + btn_height:
                        btn_color = (80,70,70)
                    elif current_m_pos[0] >= main_c_scale_y.x and current_m_pos[0] < main_c_scale_y.x + main_c_s_width and current_m_pos[1] > main_c_scale_y.y and current_m_pos[1] < main_c_scale_y.y + main_c_s_width:
                        pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
                        ctrl_xy_color = cxyc_rgb_pressed
                        current_m_pos = pg.mouse.get_pos()
                        main_c_scale_y = current_m_pos[0]
                        main_control_area.y = current_m_pos[0]
                    else:
                        btn_clickable = False
            if event.type == pg.MOUSEBUTTONUP:
                if btn_clickable == True:
                    if current_m_pos[0] >= btn_rect.x and current_m_pos[0] < btn_rect.x + btn_width and current_m_pos[1] > btn_rect.y and current_m_pos[1] < btn_rect.y + btn_height:
                        btn_color = btn_rgb_hover
                    if current_m_pos[0] >= main_c_scale_y.x and current_m_pos[0] < main_c_scale_y.x + main_c_s_width and current_m_pos[1] > main_c_scale_y.y and current_m_pos[1] < main_c_scale_y.y + main_c_s_width:
                        ctrl_xy_color = cxyc_rgb_hover
        
        draw_btn(btn_rect,btn_border_rect,btn_color,btn_font_style,
        btn_font_txt,btn_font_pos_x,btn_font_pos_y,main_control_area,
        fine_control_area,drop_down_area,display_render_area,main_c_scale_y,ctrl_xy_color)
    pg.quit()


#THIS IF STATEMENT CHECKS FOR THE FILE NAME OF MAIN.PY 
#ITS TRUE THEN IT WILL CALL MAIN() ELSE IT WILL BE FALSE. 
#ENSURING MAIN() DOESN'T RUN FOREVER
if __name__ == "__main__":
    while True:
        button(btn_width,btn_height,btn_color,btn_pos_x,btn_pos_y,btn_font_style,btn_font_txt,btn_font_pos_x,btn_font_pos_y,ctrl_xy_color)
    
#