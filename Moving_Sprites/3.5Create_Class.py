import arcade

SCREEN_WIDTH = 450
SCREEN_HEIGHT = 450

class Lolli (arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        super().update()


class Game(arcade.Window):
    """ Main application class """

    def __init__(self, width, height):
        super().__init__(width, height)
        # Background image will be stored in this variable
        self.background = None
        self.lolli = None
        self.frame_count = 0
        self.all_sprites_list = []


        # Do show the mouse cursor
        self.set_mouse_visible(True)

        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):

        self.background = arcade.load_texture("images/wall.jpg")
        ##Display a sprite
        self.lolli = arcade.Sprite("images/lollipopRed.png")
        self.lolli.scale = .75
        self.lolli.center_x = SCREEN_WIDTH / 2
        self.lolli.top = SCREEN_HEIGHT / 2


    def on_draw(self):

        """Render the screen. """
        arcade.start_render()

        # Draw the background texture
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        self.lolli.draw()

    def update(self, delta_time):
        """All the logic to move, and the game logic goes here. """
        self.lolli.update()


def main():
    """ Main method """
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()


main()