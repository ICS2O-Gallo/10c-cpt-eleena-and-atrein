import random
import arcade
import math



WIDTH = 640
HEIGHT = 480


player_x = WIDTH/2
player_y = HEIGHT/2

rain_x_pos = [100, 200, 300, 400, 350]
rain_y_pos = [480, 480, 480, 480, 480]
rain_radius = [25]
ship_w = [125]
ship_l = [100]

ship_img = arcade.load_texture('images/space_ship.jpg')




up_pressed = False
down_pressed = False
left_pressed = False
right_pressed = False


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release

    arcade.run()


def update(delta_time):
    global player_y
    if up_pressed == True :
        player_y += 10
    if down_pressed == True:
        player_y -= 10
    global player_x
    if left_pressed == True :
        player_x -= 10
    if right_pressed == True:
        player_x += 10
    for index in range(len(rain_y_pos)):
        rain_y_pos[index] -= 6

        if rain_y_pos[index] < 0:
            rain_y_pos[index] = random.randrange(HEIGHT, HEIGHT+50)
            rain_x_pos[index] = random.randrange(0, WIDTH)

    a = rain_radius[0] - ship_w[0]
    b = rain_radius[0] - ship_l[0]
    dist = math.sqrt(a**2 + b**2)

    if dist < rain_radius[0] + ship_w[0]:
        current_screen = "End"



def on_draw():
    global player_x, player_y
    arcade.start_render()
    # Draw in here..
    arcade.draw_texture_rectangle(player_x, player_y, ship_w[0],ship_l[0] , ship_img)
    for x, y in zip(rain_x_pos, rain_y_pos):
        arcade.draw_circle_filled(x, y, rain_radius[0], arcade.color.YELLOW)


def on_key_press(key, modifiers):
    global up_pressed
    if key == arcade.key.W:
        up_pressed = True
    global down_pressed
    if key == arcade.key.S:
        down_pressed = True
    global left_pressed
    if key == arcade.key.A:
        left_pressed = True
    global right_pressed
    if key == arcade.key.D:
        right_pressed = True


def on_key_release(key, modifiers):
    global up_pressed
    if key == arcade.key.W:
        up_pressed = False
    global down_pressed
    if key == arcade.key.S:
        down_pressed = False
    global right_pressed
    if key == arcade.key.D:
        right_pressed = False
    global left_pressed
    if key == arcade.key.A:
        left_pressed = False

def on_mouse_press(x, y, button, modifiers):
    pass



if __name__ == '__main__':
    setup()
