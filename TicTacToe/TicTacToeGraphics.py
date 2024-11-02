import arcade
from TTTLogic import Tic_Tac_Toe_logic
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 650
POSITION_RANGES = [[[1, 199], [201, 399], [401, 599]], [[1, 199], [201, 399], [401, 599]]]

class IntroView(arcade.View):
    def on_show_view(self):
        arcade.set_background_color(arcade.color.LIGHT_BLUE)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Click on square ", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("to move ", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 75,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Click to advance", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 150,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = Game()
        game_view.setup()
        self.window.show_view(game_view)



class Game(arcade.View):
    """ Main application class """

    def __init__(self):
        super().__init__()
        # Background image will be stored in this variable
        self.background = None

        self.all_sprites_list = []


        self.player = None
        self.score = 0
        self.score_text = None
        self.play = None
        self.logic = None


        # Do show the mouse cursor
        self.window.set_mouse_visible(False)

        # Set the background color
        arcade.set_background_color(arcade.color.WHITE)

    def setup(self):

        self.all_sprites_list = arcade.SpriteList()
        self.move_list = arcade.SpriteList()
        self.player = arcade.Sprite("downLeft.png", 1)
        self.all_sprites_list.append(self.player)
        self.logic = Tic_Tac_Toe_logic(SCREEN_WIDTH, SCREEN_HEIGHT-50)
        # Score
        self.score = 0



    def on_draw(self):
        """Render the screen. """

        arcade.start_render()
        ## Draw Score area
        arcade.draw_rectangle_filled(SCREEN_WIDTH//2,SCREEN_HEIGHT-25,SCREEN_WIDTH,50,arcade.color.GRAY)
        ## Draw Board
        # Draw vertical lines every 120 pixels
        for x in range(200, SCREEN_WIDTH, (SCREEN_HEIGHT  // 3)):
            arcade.draw_line(x, 0, x, SCREEN_HEIGHT-50, arcade.color.BLACK, 2)

        # Draw horizontal lines every 200 pixels
        for y in range(200, SCREEN_HEIGHT-50, ((SCREEN_HEIGHT-50) // 3)):
            arcade.draw_line(0, y, SCREEN_WIDTH, y, arcade.color.BLACK, 2)
        self.draw_game()
        #self.draw_game_over()

    def draw_game(self):
        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, SCREEN_HEIGHT-25, arcade.color.BLACK, 14)
        self.player.draw()
        self.move_list.draw()





    def update(self, delta_time):
        """All the logic to move, and the game logic goes here. """
        self.player.update()

    def on_mouse_press(self, x, y, button, key_modifiers):
        """ Called when the user presses a mouse button. """
        # print("Clicked", self.player.center_x, self.player.center_y)
        self.put_symbol(self.player.center_x, self.player.center_y,"x_shape.gif")
        position = self.logic.find_best_move()
        self.draw_symbol(position, "circle.gif")




    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """ Called whenever the mouse moves. """
        self.player.center_x = x
        self.player.center_y = y

    def on_key_release(self, key, modifiers):

        if key == arcade.key.ESCAPE:
            self.close()


#########################################################
# Finding where user clicked and drawing symbols

    ## Put human's move on board
    def put_symbol(self,center_x, center_y, image):
        position = self.find_position(center_x,center_y)
        self.draw_symbol(position, image)

    def draw_symbol(self, position, image):
        # find position
        if image == "x_shape.gif":
            side = "x"
        else:
            side = "o"
        ## go to logic side
        position  = self.logic.control_board(position, side)
        ##If legal move
        if position != (-1, -1):
            #if not taken, draw symbol
            coords = self.get_centers(position)
            symbol = arcade.Sprite(image, 2)

            symbol.center_x = coords[1]+15
            symbol.center_y = coords[0]
            self.move_list.append(symbol)
            self.all_sprites_list.append(symbol)
            winner = self.logic.test_for_winner()
            if self.logic.test_for_draw():
                # go to end view
                end_view = EndView("", self.logic)
                self.window.show_view(end_view)
            elif winner != " ":
                end_view = EndView(winner,self.logic)
                self.window.show_view(end_view)
        else:
            print("Illegal move")


    def find_position(self,x_position, y_position):
        column = -1
        row = -1
        x_ranges = POSITION_RANGES[0]
        y_ranges = POSITION_RANGES[1]
        for index in range(len(x_ranges)):
            column_range = x_ranges[index]
            if column_range[0] <= x_position <= column_range[1]:
                column = index

        for index in range(len(y_ranges)):
            row_range = y_ranges[index]
            if row_range[0] <= y_position <= row_range[1]:
                row = index
        return (row, column)

    def get_centers(self, position):
        x_ranges = POSITION_RANGES[0]
        y_ranges = POSITION_RANGES[1]
        x_pos_range = x_ranges[position[0]]
        y_pos_range = y_ranges[position[1]]

        xpos = (x_pos_range[0] + x_pos_range[1])//2
        ypos = (y_pos_range[0] + y_pos_range[1]) // 2
        return (xpos,ypos )

class EndView(arcade.View):
    def __init__(self,winner, logic):
        super().__init__()
        if winner == "x":
            self.text = "Winner is Player"
        elif winner == "o":
            self.text = "Winner is Computer"
        else:
            self.text = "Draw"
        logic.draw_board()

    def on_show_view(self):
        arcade.set_background_color(arcade.color.LIGHT_BLUE)

    def on_draw(self):
        self.clear()
        arcade.draw_text(self.text, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.BLACK, font_size=50, anchor_x="center")


    def on_mouse_press(self, _x, _y, _button, _modifiers):
         arcade.exit()

def main():
    """ Main method """
    # window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
    # window.setup()
    # arcade.run()
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Tic Tac Toe")
    intro_view = IntroView()
    window.show_view(intro_view)
    arcade.run()


main()