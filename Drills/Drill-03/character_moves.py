from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

# fill here

x = 0
y = 90
delta = 0
r = 210
num = 10

while (num > 0) :
    while (x < 780) :
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x + 10
        delay(0.01)

    while ( y < 570) :
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y = y + 10
        delay(0.01)

    while ( x > 20) :
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x - 10
        delay(0.01)

    while (y > 90) :
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y = y - 10
        delay(0.01)

    while (x < 400) :
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x = x + 10
        delay(0.01)
    
    while (x < 700 and y < 300) :
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x + 4
        delta = math.sqrt((400 - x)**2 + (300 - y)**2) 
        y = y + (delta - r)
        if (x > 700) :
            x = 700
        delay(0.01)
        
    while (x > 400 and y < 600) :
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y = y + 4
        delta = math.sqrt((400 - x)**2 + (300 - y)**2)
        if ( r > delta) :
            x = x - (r - delta)
        else :
            x = x - (delta - r)
        delay(0.01)
    
    while (x > 0 and y > 300) :
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x - 4
        delta = math.sqrt((400 - x)**2 + (300 - y)**2) 
        if ( r > delta) :
            y = y - (r - delta)
        else :
            y = y - (delta - r)
        delay(0.01)
        
    while (x < 400 and y > 90) :
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x + 4
        delta = math.sqrt((400 - x)**2 + (300 - y)**2)
        if ( r > delta) :
            y = y - (r - delta)
        else :
            y = y - (delta - r)
        delay(0.01)

    num = num - 1
    
close_canvas()    
