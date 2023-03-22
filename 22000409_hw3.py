'''
22000409 양승렬
description: 휴보가 계단을 올라가서 신문을 놓고 다시 돌아오는 프로그램입니다.
'''

from cs1robots import*
load_world("worlds/newspaper.wld")
hubo=Robot(beepers=1)
hubo.set_trace("blue")
hubo.set_pause(0.2)
# Turn right.
def turn_right():  
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()
# Go up one stair.
def upstair_block(): 
    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()
    hubo.move()
# Come down one stair.
def downstair_block():
    hubo.move()
    hubo.move()
    hubo.turn_left()
    hubo.move()
    turn_right()
# Move foward to go up the stair.
hubo.move()
# Go up four stairs through for loops. 
for i in range(4):
    upstair_block()
# Drop the newspaper.     
hubo.drop_beeper()
# Turn around to come back.
hubo.turn_left()
hubo.turn_left()
# Come down four stairs through for loops.
for i in range(4):
    downstair_block()
# Move forward to comeback and Turn around.
hubo.move()
hubo.turn_left()
hubo.turn_left()
