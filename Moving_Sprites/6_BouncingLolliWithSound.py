import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Lolli (arcade.Sprite):

    def __init__(self, image, scale, bounce_sound):
        super().__init__(image,scale)
        self.bounce_sound = arcade.load_sound(bounce_sound)

    def update(self):
        ## bounce off sides
        if self.left <= 0 or self.right >= SCREEN_WIDTH:
            arcade.play_sound(self.bounce_sound)
            self.change_x *= -1

        elif self.bottom <=0 or self.top >= SCREEN_HEIGHT:
            arcade.play_sound(self.bounce_sound)
            self.change_y *= -1

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
        self.all_sprites_list = []
        self.sound = None



        # Do show the mouse cursor
        self.set_mouse_visible(True)

        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):

        self.background = arcade.load_texture("images/wall.jpg")
        self.all_sprites_list = arcade.SpriteList()
        self.sound = "./images/jump4.wav"

        self.lolli = Lolli("images/lollipopRed.png", .75, ":resources:sounds/hit5.wav")

        self.lolli.center_x = SCREEN_WIDTH // 2
        self.lolli.center_y = SCREEN_HEIGHT // 2
        self.lolli.angle = 0
        self.lolli.change_x = 1
        self.lolli.change_y  = 1
        self.all_sprites_list.append(self.lolli)

        self.sound = "./images/jump4.wav"



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


if __name__ == "__main__":
    main()