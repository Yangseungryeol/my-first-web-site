'''
22000409 양승렬
description: 휴보가 허들을 넘고 비퍼를 주운 후 다시 돌아오는 프로그램입니다. 
'''

from cs1robots import*
load_world("worlds/hurdles1.wld")
hubo=Robot()
hubo.set_trace("blue")
hubo.set_pause(0.2)

# Turn right.
def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()

# Jump one hurdle.
def jump_hurdle():
    hubo.move()
    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()
    turn_right()
    hubo.move()
    hubo.turn_left()
# Come back one hurdle.
def come_back():
    hubo.move()
    turn_right()
    hubo.move()
    hubo.turn_left()
    hubo.move()
    hubo.turn_left()
    hubo.move()
    turn_right()
# four Jump block through for loops.
for i in range(4):
    jump_hurdle()
# move forward to pick the beeper.
hubo.move()
hubo.pick_beeper()
# Turn around to come back.
hubo.turn_left()
hubo.turn_left()
# four come back through for loops.
for i in range(4):
    come_back()
# Return to first time.
hubo.move()
turn_right()
turn_right()
