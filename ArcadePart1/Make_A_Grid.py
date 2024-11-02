import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Draw a Grid of Blocks")
arcade.set_background_color(arcade.color.GRAY_BLUE)
arcade.start_render()


arcade.draw_rectangle_filled(22, 33, 44, 66, arcade.color.BLUSH)




#  Finish and run
arcade.finish_render()
arcade.run()