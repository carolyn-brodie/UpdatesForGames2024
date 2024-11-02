import random
import arcade


SCREEN_WIDTH = 360
SCREEN_HEIGHT = 640
pipeGapList = []


class Bird (arcade.Sprite):

    def __init__(self, image, scale):
        super().__init__(image, scale)
        self.center_x = 100
        self.center_y = 500
        self.angle = 0
        self.velo = 0
        self.is_jumping = False



    def update(self, symbol = None):
        # Gravity and Jump
        self.velo += -0.5
        self.center_y += self.velo
        if self.velo < -7:
            self.velo = -7
        if symbol == arcade.key.SPACE and self.center_y > 0:
            self.is_jumping = True
            self.velo = 0
            self.velo += 8.5


class Pipe(arcade.Sprite):

    def __init__(self, image, scale):
        super().__init__(image, scale)
        self.center_x = SCREEN_WIDTH+100


        if image == "top_pipe.png":
            randNumPipe = random.randint(SCREEN_HEIGHT // 2 - 150, SCREEN_HEIGHT // 2 + 150)
            pipeGapList.append(randNumPipe)
            self.bottom = randNumPipe + 75

        else:
            self.top = pipeGapList[-1] - 75
            pipeGapList.pop(0)



    def update(self):
        self.center_x -= 1
        if self.center_x < -50:
            self.remove_from_sprite_lists()
        super(Pipe, self).update()




class StartingScreen(arcade.View):

    def __init__(self):
        super().__init__()
        self.background = arcade.load_texture('BackGround.png')


    def on_draw(self):
        self.clear()
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        arcade.draw_text("Press Spacebar ", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 150,
                         arcade.color.WHITE, font_size=30, anchor_x="center")
        arcade.draw_text("to jump ", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 200,
                         arcade.color.WHITE, font_size=30, anchor_x="center")
        arcade.draw_text("Press Space to advance", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 250,
                         arcade.color.WHITE, font_size=15, anchor_x="center")

    def on_key_release(self, symbol, modifier):
            if symbol == arcade.key.SPACE:
                game_view = Game()
                game_view.setup()
                self.window.show_view(game_view)

class Game(arcade.View):
    """ Main application class """

    def __init__(self):
        super().__init__()
        # Background image will be stored in this variable
        self.background = None
        self.bottom_pipe_image = None
        self.top_pipe_image = None
        self.bird = None
        self.pipeTop = None
        self.pipeBot = None
        self.pipeWidth = 0
        self.pipeHeight = 0
        self.randPipeList = []
        self.count = 0
        # self.y_top = 0
        # self.x_top = 0
        # self.y_bottom = 0
        # self.x_bottom = 0
        self.pipe_timer = 150
        # self.pipes = []
        self.frame_count = 0
        self.birdSpriteList = arcade.SpriteList()
        self.pipeSpriteList = arcade.SpriteList()
        self.all_sprites_list = arcade.SpriteList()

    def on_key_press(self, symbol: int, modifiers: int):
        """Called whenever a key is pressed. """
        if symbol == arcade.key.SPACE:
            self.bird.update(symbol)


    def setup(self):

        self.background = arcade.load_texture("BackGround.png")
        self.all_sprites_list = arcade.SpriteList()
        self.bird = Bird("bird2.0.png", 0.1)
        self.pipeTop = Pipe("top_pipe.png", 1.1)
        self.pipeBot = Pipe("bottom_pipe.png", 1.1)
        self.all_sprites_list.append(self.bird)
        self.all_sprites_list.append(self.pipeTop)
        self.all_sprites_list.append(self.pipeBot)



    def on_draw(self):
        """Render the screen. """
        arcade.start_render()
        self.draw_game()



    def draw_game(self):

        # Draw the background texture
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)


        self.all_sprites_list.draw()


    def update(self, delta_time):
        """All the logic to move, and the game logic goes here. """

        self.frame_count += 1

        self.all_sprites_list.update()


        print(self.all_sprites_list[-3].center_x)
        # print(self.pipeTop.center_x)
        # print(self.pipeTop.center_x - SCREEN_WIDTH//1.5)

        if self.all_sprites_list[-3] == self.bird.center_x and self.all_sprites_list[-3] != self.bird:
            self.count += 1
            print(self.count)

        if self.pipeTop.center_x == SCREEN_WIDTH//1.5:
            self.pipeTop = Pipe("top_pipe.png", 1.1)
            self.pipeBot = Pipe("bottom_pipe.png", 1.1)
            self.all_sprites_list.append(self.pipeTop)
            self.all_sprites_list.append(self.pipeBot)

        if self.bird.center_y < 0 or self.bird.collides_with_list(self.all_sprites_list):
            gameOverView = gameOver()
            self.window.show_view(gameOverView)


class gameOver(arcade.View):
    def __init__(self):
        super().__init__()

    def on_draw(self):

        arcade.draw_text("Game Over", 80, 150, arcade.color.WHITE, 20)

    def on_key_release(self, symbol: int, modifiers: int):
        game_view = StartingScreen()
        self.window.show_view(game_view)

def main():
    """ Main method """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Flappy Bird")
    startingView = StartingScreen()
    window.show_view(startingView)
    arcade.run()


main()

