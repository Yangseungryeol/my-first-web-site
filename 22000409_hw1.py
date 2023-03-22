'''
22000409 양승렬
Description: 지그재그 방향으로 나아가 (10,0)으로 도달하는 프로그램입니다.
'''

from cs1robots import*
create_world()
hubo=Robot()
hubo.set_trace("blue")
hubo.set_pause(0.2)

# Turn right.
def turn_right():
    for i in range(3):
        hubo.turn_left()
# Straight from current point until turning.
def go_straight():
    for i in range(9):
        hubo.move()
# One cycle of doing zigzag.
def one_cycle():
    hubo.turn_left()
    go_straight()
    turn_right()
    hubo.move()
    turn_right()
    go_straight()
# four times to zigzag through for loops(main code)
for k in range(4): 
    one_cycle()
    hubo.turn_left()
    hubo.move()
#last cycle to finish the zigzag.
one_cycle()

    





