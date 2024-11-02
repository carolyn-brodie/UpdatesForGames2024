import arcade


SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

 #Set Background color
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Add a Background Image")
arcade.set_background_color(arcade.color.WHITE)

#Load a background image
background = arcade.load_texture("images/wall.jpg")

# Start the render process. This must be done before any drawing commands.
arcade.start_render()

arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                              SCREEN_WIDTH, SCREEN_HEIGHT, background)
arcade.finish_render()
arcade.run()