from pico2d import *

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

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
    x, y = 510, 92
    frame = 0
    while (x < 692 and y < 518):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += 4
        y += 13
        delay(0.01)
        get_events()

def MoveEighthStep() :
    x, y = 692, 518
    frame = 0
    while (x > 682 and y > 336):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x -= 1
        y -= 13
        delay(0.01)
        get_events()

def MoveNinthStep() :
    x, y = 682, 336
    frame = 0
    while (x < 712 and y < 349):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += 3
        y += 1
        delay(0.01)
        get_events()

def MoveTenthStep() :
    x, y = 712, 349
    frame = 0
    while (x > 203 and y < 535):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x -= 13
        y += 5
        delay(0.01)
        get_events()


while True :
    #MoveFirstStep()
    #MoveSecondStep()
    #MoveThirdStep()
    #MoveFourthStep()
    #MoveFifthStep()
    #MoveSixthStep()
    #MoveSeventhStep()
    #MoveEighthStep()
    #MoveNinthStep()
    MoveTenthStep()

close_canvas()