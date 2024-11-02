import arcade


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

 #Set Background color
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Display Shapes to Screen")
arcade.set_background_color(arcade.color.WHITE)

# Start the render process. This must be done before any drawing commands.
arcade.start_render()

# 0,0 will be the top left corner.  45 and 45 represent the width and height of the rectangle
#arcade.draw_rectangle_filled(0, 0, 45, 45, arcade.color.BLUSH)

# # Draw a filled ellipse, and another one rotated

# for x in range(20,800,100):
#     for y in range(20, 600, 100):
#
#         arcade.draw_rectangle_filled(x, y, 45, 45, arcade.color.BLUE)


arcade.finish_render()
arcade.run()