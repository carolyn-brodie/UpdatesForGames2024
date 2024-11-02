import arcade


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

 #Set Background color
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Demonstrate a Window")
arcade.set_background_color(arcade.color.BLUE)

# Start the render process. This must be done before any drawing commands.
arcade.start_render()

##Finish the rendor process
arcade.finish_render()
#Must always be executed before starting
arcade.run()