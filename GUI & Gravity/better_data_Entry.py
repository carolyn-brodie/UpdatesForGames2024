import arcade
from arcade import load_texture
from arcade.gui import UIManager
from arcade.gui.widgets import UITextArea, UIInputText, UITexturePane
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

LOREM_IPSUM = (
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent eget pellentesque velit. "
    "Nam eu rhoncus nulla. Fusce ornare libero eget ex vulputate, vitae mattis orci eleifend. "
    "Donec quis volutpat arcu. Proin lacinia velit id imperdiet ultrices. Fusce porta magna leo, "
    "non maximus justo facilisis vel. Duis pretium sem ut eros scelerisque, a dignissim ante "
    "pellentesque. Cras rutrum aliquam fermentum. Donec id mollis mi.\n"
    "\n"
    "Nullam vitae nunc aliquet, lobortis purus eget, porttitor purus. Curabitur feugiat purus sit "
    "amet finibus accumsan. Proin varius, enim in pretium pulvinar, augue erat pellentesque ipsum, "
    "sit amet varius leo risus quis tellus. Donec posuere ligula risus, et scelerisque nibh cursus "
    "ac. Mauris feugiat tortor turpis, vitae imperdiet mi euismod aliquam. Fusce vel ligula volutpat, "
    "finibus sapien in, lacinia lorem. Proin tincidunt gravida nisl in pellentesque. Aenean sed "
    "arcu ipsum. Vivamus quam arcu, elementum nec auctor non, convallis non elit. Maecenas id "
    "scelerisque lectus. Vivamus eget sem tristique, dictum lorem eget, maximus leo. Mauris lorem "
    "tellus, molestie eu orci ut, porta aliquam est. Nullam lobortis tempor magna, egestas lacinia lectus.\n"
)

class InstructionView(arcade.View):
    def on_show_view(self):
        arcade.set_background_color(arcade.color.LIGHT_BLUE)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Test of Instruction ", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Screen ", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 75,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Click to advance", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 150,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = MyWindow()
        game_view.setup()
        self.window.show_view(game_view)


class MyWindow(arcade.View):
    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)
        self.text = ""

    def setup(self):
        self.manager = UIManager()
        self.manager.enable()
        ## Create Text Area
        bg_tex = load_texture(":resources:gui_basic_assets/window/grey_panel.png")
        text_area = UITextArea(x=100,
                               y=200,
                               width=200,
                               height=300,
                               text=LOREM_IPSUM,
                               text_color=(0, 0, 0, 255))



        self.manager.add(
            UITexturePane(
                text_area.with_space_around(right=20),
                tex=bg_tex,
                padding=(10, 10, 10, 10)
            )
        )

        ##Text input area
        self.input_area = UIInputText(x=340, y=200, width=200, height=50, text="")
        self.manager.add(
            UITexturePane(
                #UIInputText(x=340, y=200, width=200, height=50, text=""),
                self.input_area,
                tex=bg_tex,
                padding=(10, 10, 10, 10)
            ))

        ##Text on screen
        self.manager.add(
            UIInputText(x=340, y=110, width=200, height=50, text=self.text),
        )

        ##Buttons
        # Create a BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()

        # Create the buttons
        reload_button = arcade.gui.UIFlatButton(text="Read Text", width=200)
        self.v_box.add(reload_button.with_space_around(bottom=20))

        reload_button.on_click = self.on_click_reload

        end_button = arcade.gui.UIFlatButton(text="Ending Button", width=200)
        self.v_box.add(end_button.with_space_around(bottom=20))

        end_button.on_click = self.on_click_end

        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="bottom",
                child=self.v_box)
        )

    def on_click_reload(self, event):
        print("My Start:", event)
        self.text = self.input_area.text
        self.clear()
        self.setup()


    def on_click_end(self, event):
        print("My Start:", event)
        end_view = EndingView()
        self.window.show_view(end_view)

    def on_draw(self):
        self.clear()
        self.manager.draw()


class EndingView(arcade.View):
    def on_show_view(self):
        arcade.set_background_color(arcade.color.LIGHT_BLUE)

    def on_draw(self):
        self.clear()
        arcade.draw_text("End of Game ", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.BLACK, font_size=50, anchor_x="center")

        arcade.draw_text("Click to advance", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 150,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
       arcade.exit()


# window = MyWindow()
# arcade.run()
window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "GUI")
instruction_view = InstructionView()
window.show_view(instruction_view)
arcade.run()