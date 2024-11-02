import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def drawPerson(xPosition, yPosition):

    #Snowballs

    arcade.draw_circle_filled(xPosition, yPosition, 60, arcade.color.WHITE)
    yMiddle = yPosition +80
    arcade.draw_circle_filled(xPosition, yMiddle, 50, arcade.color.WHITE)
    yTop = yPosition  + 140
    arcade.draw_circle_filled(xPosition, yTop, 40, arcade.color.WHITE)

    # Eyes
    arcade.draw_circle_filled(xPosition-15, yTop+10, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(xPosition+15, yTop+10, 5, arcade.color.BLACK)



def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Many Snowmen")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.start_render()

    # Draw the ground
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)

    # Draw a snow person
    drawPerson(300,200)
    drawPerson(500, 200)

    #  Finish and run
    arcade.finish_render()
    arcade.run()


if __name__ == "__main__":
    main()