import arcade

# Set screen size
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Touch grass simulator")

arcade.set_background_color(arcade.color.BLUE)

arcade.start_render()

# write code

arcade.finish_render()

arcade.run()