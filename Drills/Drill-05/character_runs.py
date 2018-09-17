from pico2d import *

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

OriginX, OriginY = 203, 535

def MoveFirstStep() :
    x, y = 203, 535
    frame = 0
    while (x > 132 and y > 243) :
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x -= 3
        y -= 11
        delay(0.01)
        get_events()

def MoveSecondStep() :
    x, y = 132, 243
    frame = 0
    while (x < 535 and y < 470) :
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += 11
        y += 6
        delay(0.01)
        get_events()

def MoveThirdStep() :
    x, y = 535, 470
    frame = 0
    while (x > 477 and y > 203) :
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x -= 3
        y -= 12
        delay(0.01)
        get_events()

def MoveFourthStep() :
    x, y = 477, 203
    frame = 0
    while (x < 715 and y > 136) :
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += 11
        y -= 3
        delay(0.01)
        get_events()

def MoveFifthStep() :
    x, y = 715, 136
    frame = 0
    while (x > 316 and y < 225) :
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x -= 11
        y += 3
        delay(0.01)
        get_events()

def MoveSixthStep() :
    x, y = 316, 225
    frame = 0
    while (x < 510 and y > 92) :
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += 5
        y -= 3
        delay(0.01)
        get_events()

def MoveSeventhStep() :
    pass

def MoveEighthStep() :
    pass

def MoveNinthStep() :
    pass

def MoveTenthStep() :
    pass

while True :
    #MoveFirstStep()
    #MoveSecondStep()
    #MoveThirdStep()
    #MoveFourthStep()
    #MoveFifthStep()
    MoveSixthStep()
    MoveSeventhStep()
    MoveEighthStep()
    MoveNinthStep()
    MoveTenthStep()

close_canvas()