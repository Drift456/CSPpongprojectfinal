from time import sleep
from sense_hat import SenseHat

sense = SenseHat()
y = 4
ball_position=[6, 3]
ball_speed=[-1, -1]

def move_up(event):
    global y
    if y > 1 and event.action=='pressed':
        y -= 1
    print(event)

def move_down(event):
    global y
    if y < 6 and event.action=='pressed':
        y += 1
    print(event)

def draw_bat():
    sense.set_pixel(0, y, 0, 255, 255)
    sense.set_pixel(0, y+1, 0, 255, 255)
    sense.set_pixel(0, y-1, 0, 255, 255)
        
def ball_play():
    sense.set_pixel(ball_position[0], ball_position[1], 0, 0, 0)

    ball_position[0] += ball_speed[0]
    ball_position[1] += ball_speed[1]

    if ball_position[1] == 0 or ball_position[1] == 7:
        ball_speed[1] = -ball_speed[1]
    if ball_position[0] == 7:
        ball_speed[0] = -ball_speed[0]
    if ball_position[0] == 1 and y-1 <= ball_position[1] <= y+1:
        ball_speed[0] = -ball_speed[0]
    if ball_position[0] == 0:
        return False

    sense.set_pixel(ball_position[0], ball_position[1], 0, 0, 255)
    return True



sense.stick.direction_up = move_up
sense.stick.direction_down = move_down

while ball_play():
    draw_bat()
    sleep(0.25)
    sense.clear(0, 0, 0)
    
sense.show_message(" 00f u lose ", text_colour=(69, 69, 69))
