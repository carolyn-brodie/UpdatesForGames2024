
import arcade
import random
import sys
import os

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    os.chdir(sys._MEIPASS)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

## These numbers represent "states" that the game can be in.
GAME_INTRO = 1
GAME_RUNNING = 2
GAME_OVER = 3
TIMEBETWEENDROPS = 100


class Bunny(arcade.Sprite):
    def update(self):

        ## bounce off sides
        if self.left <= 0 or self.right >= SCREEN_WIDTH:
            self.change_x *= -1

        elif random.randrange(200) == 0:
            self.change_x *= -1

        self.center_x += self.change_x
        super(Bunny, self).update()

class InstructionView(arcade.View):
    def on_show_view(self):
        arcade.set_background_color(arcade.color.LIGHT_BLUE)

    def on_draw(self):
        self.clear()
        arcade.draw_text("This is an introduction ", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("screen ", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 75,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Click to advance", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 150,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = MyApplication()
        game_view.setup()
        self.window.show_view(game_view)

class MyApplication(arcade.View):
    """ Main application class """

    def __init__(self):
        super().__init__()
        # Background image will be stored in this variable
        self.background = None

        self.frame_count = 0
        self.all_sprites_list = []
        self.Bunny = None
        self.lolli_list = []

        self.player = None
        self.score = 0
        self.score_text = None
        self.current_state = None
        self.dropTime = TIMEBETWEENDROPS
        self.difficulty = 70  ##Intial speed determiner

        # Do show the mouse cursor
        self.window.set_mouse_visible(True)

        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):

        self.background = arcade.load_texture("./Resources/Images/wall.jpg")
        self.all_sprites_list = arcade.SpriteList()
        self.lolli_list = arcade.SpriteList()
        # Score
        self.score = 0


        self.player = arcade.Sprite("./Resources/Images/plantPurple.png", 1)
        self.all_sprites_list.append(self.player)

        self.bunny = Bunny("./Resources/Images/rabbit.png", 1)
        self.bunny.scale = .3
        self.bunny.center_x = 200
        self.bunny.center_y = SCREEN_HEIGHT - self.bunny.height
        self.bunny.angle = 0
        self.bunny.change_x = 1
        self.all_sprites_list.append(self.bunny)

    def on_draw(self):
        """Render the screen. """

        arcade.start_render()
        # Draw the background texture
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.draw_game()


    def draw_game(self):

        self.bunny.draw()
        self.lolli_list.draw()
        self.player.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 550, arcade.color.BLACK, 14)

    def draw_game_over(self):
        """
        Draw "Game over" across the screen.
        """
        end_view = GameOverView()
        self.window.show_view(end_view)



    def update(self, delta_time):
        """All the logic to move, and the game logic goes here. """

        # Use this if you want something to stay on the screen for a limited time
        self.frame_count += 1

        # Determine when to drop next lollipop
        if self.dropTime == 0:
            lolli = arcade.Sprite("./Resources/Images/lollipopRed.png")
            lolli.scale = .5
            lolli.center_x = self.bunny.center_x
            lolli.angle = -90
            lolli.top = self.bunny.bottom
            lolli.change_y = -2

            self.lolli_list.append(lolli)
            self.all_sprites_list.append(lolli)
            self.dropTime = TIMEBETWEENDROPS * (random.randrange(self.difficulty, 100) / 100)

        else:
            self.dropTime = self.dropTime - 1

        # Generate a list of all sprites that collided with the player.
        hit_list = arcade.check_for_collision_with_list(self.player,
                                                        self.lolli_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for lolli in hit_list:
            lolli.kill()
            self.score += 10

        if self.score % 100 == 0 and self.score > 0 and self.difficulty > 0:
            self.difficulty -= 10

        # Get rid of the lolli when it flies off-screen
        for lolli in self.lolli_list:
            if lolli.top < 0:
                lolli.kill()
                self.draw_game_over()
                self.frame_count = 0

        self.lolli_list.update()
        self.bunny.update()

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """ Called whenever the mouse moves. """
        self.player.center_x = x
        self.player.center_y = 50

    def on_key_release(self, key, modifiers):
        if key == arcade.key.SPACE:
            if self.current_state == GAME_INTRO:
                self.current_state= GAME_RUNNING
        elif key == arcade.key.ESCAPE:
            if self.current_state == GAME_OVER:
                self.close()

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
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Lolli Lunacy")
    instruction_view = InstructionView()
    window.show_view(instruction_view)
    arcade.run()


main()