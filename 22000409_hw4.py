'''
22000409 양승렬
description: 휴보가 비퍼를 줍는 프로그램입니다. 
'''

from cs1robots import*
load_world("worlds/harvest1.wld")
hubo=Robot()
hubo.set_trace("blue")
hubo.set_pause(0.2)
# Turn right.
def turn_right():  
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()
# A course of picking up beeper while moving. 
def course():
    for i in range(5):
        hubo.pick_beeper()
        hubo.move()
    hubo.pick_beeper()
    hubo.turn_left()
    hubo.move()
    hubo.turn_left()
# Reverse course of picking up beeper while moving.  
def reverse_course():
    for i in range(5):
        hubo.pick_beeper()
        hubo.move()
    hubo.pick_beeper()
    turn_right()
    hubo.move()
    turn_right()
# Move forward to pick up the beeper.    
hubo.move()
# Pick up the beeper while moving. 
for i in range(3):
    course()
    reverse_course()


