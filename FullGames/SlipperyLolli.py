import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 5


class Lolli (arcade.Sprite):
    def update(self):

        ## bounce off sides
        if self.left <= 0 or self.right >= SCREEN_WIDTH:
            self.change_x *= -1

        elif self.bottom <=0 or self.top >= SCREEN_HEIGHT:
            self.change_y *= -1

        self.center_x += self.change_x
        super(Lolli, self).update()

class InstructionView(arcade.View):
    def on_show_view(self):
        arcade.set_background_color(arcade.color.LIGHT_BLUE)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Hit the lolli with the cake ", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("to make it jump ", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 75,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Click to advance", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 150,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = Game()
        game_view.setup()
        self.window.show_view(game_view)



class Game(arcade.View):    ## Change arcade.Window to arcade.View
    """ Main application class """

    def __init__(self):
        super().__init__()
        # Background image will be stored in this variable
        self.background = None
        self.lolli = None
        self.cake = None
        self.frame_count = 0
        self.all_sprites_list = []
        self.lolli_list = []
        self.cake_list = []
        self.score = 0
        self.score_text = None



        # Do show the mouse cursor
        self.window.set_mouse_visible(True)

        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):

        self.background = arcade.load_texture("./images/wall.jpg")
        self.all_sprites_list = arcade.SpriteList()
        self.lolli_list = arcade.SpriteList()
        self.cake_list = arcade.SpriteList()



        self.lolli = Lolli("./images/lollipopRed.png", 1)

        self.lolli.center_x = SCREEN_WIDTH // 2
        self.lolli.center_y = SCREEN_HEIGHT // 2
        self.lolli.angle = 0
        self.lolli.change_x = 1
        self.lolli.change_y  = 1
        self.all_sprites_list.append(self.lolli)
        self.lolli_list.append(self.lolli)

        self.cake = arcade.Sprite("./images/cake.png", .75)
        self.cake_list.append(self.cake)
        self.all_sprites_list.append(self.cake)

        self.score = 0





    def on_draw(self):
        """Render the screen. """

        arcade.start_render()
        # Draw the background texture
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        self.draw_game()







    def draw_game(self):
        self.lolli.draw()
        self.cake.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 550, arcade.color.BLACK, 14)





    def update(self, delta_time):
        """All the logic to move, and the game logic goes here. """

        self.frame_count += 1
        self.cake_list.update()
        self.lolli_list.update()

        # Generate a list of all sprites that collided with the player.
        hit_list = arcade.check_for_collision_with_list(self.cake, self.lolli_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for lolli in hit_list:
            self.lolli.center_x = random.randrange(SCREEN_WIDTH)
            self.lolli.center_y = random.randrange(SCREEN_HEIGHT)
            self.score += 1
            if self.score >= 10:
                self.draw_game_over()



    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """ Called whenever the mouse moves. """
        self.cake.center_x = x
        self.cake.center_y = y



    def on_key_release(self, key, modifiers):
        """
        Called when the user releases a key.
        """

        if key == arcade.key.ESCAPE:
            self.close()

    def draw_game_over(self):
        end_view = GameOverView()
        self.window.show_view(end_view)


class GameOverView(arcade.View):
    def on_show_view(self):
        arcade.set_background_color(arcade.color.LIGHT_BLUE)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Game Over ", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.BLACK, font_size=50, anchor_x="center")


    def on_mouse_press(self, _x, _y, _button, _modifiers):
        self.window.close()





def main():
    """ Main method """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Slippery Lolli")
    instruction_view = InstructionView()
    window.show_view(instruction_view)
    arcade.run()



main()