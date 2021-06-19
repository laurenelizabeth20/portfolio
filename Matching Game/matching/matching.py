
import arcade
from pathlib import Path
import random as rand
 
# Set how many rows and columns we will have
ROW_COUNT = 3
COLUMN_COUNT = 4

#Load all sounds and pictures
CLICK_SOUND = arcade.load_sound("matching/click_sound.mp3")
FLOWER = arcade.load_texture("matching/flower.jpg")
CAT = arcade.load_texture("matching/cat.jpg")
DOG = arcade.load_texture("matching/dog.jpg")
TURTLE = arcade.load_texture("matching/turtle.jpg")
BUNNY = arcade.load_texture("matching/bunny.jpg")
TREE = arcade.load_texture("matching/tree.jpg")
 
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 100
HEIGHT = 100
 
# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 15
 
# Do the math to figure out our screen dimensions
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN
SCREEN_TITLE = "Array Backed Grid Example"
 
 
class MyGame(arcade.Window):
    """
    Main application class.
    """
 
    def __init__(self, width, height, title):
        """
        Set up the application.
        """
 
        super().__init__(width, height, title)

        # Create a 2 dimensional array. A two dimensional
        # array is simply a list of lists.
        self.grid = []
        for row in range(ROW_COUNT):
            # Add an empty array that will hold each cell
            # in this row
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                
                #setattr(self.grid[row][column], "image", rand.choice(images))
                self.grid[row].append(0)  # Append a cell

        arcade.set_background_color(arcade.color.BLACK)

        #randomly assign pictures to squares, making sure there are two of each picture on the board
        squares = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
        self.sqr1 = rand.choice(squares)
        squares.remove(self.sqr1)
        self.sqr2 = rand.choice(squares)
        squares.remove(self.sqr2)
        self.sqr3 = rand.choice(squares)
        squares.remove(self.sqr3)
        self.sqr4 = rand.choice(squares)
        squares.remove(self.sqr4)
        self.sqr5 = rand.choice(squares)
        squares.remove(self.sqr5)
        self.sqr6 = rand.choice(squares)
        squares.remove(self.sqr6)
        self.sqr7 = rand.choice(squares)
        squares.remove(self.sqr7)
        self.sqr8 = rand.choice(squares)
        squares.remove(self.sqr8)
        self.sqr9 = rand.choice(squares)
        squares.remove(self.sqr9)
        self.sqr10 = rand.choice(squares)
        squares.remove(self.sqr10)
        self.sqr11 = rand.choice(squares)
        squares.remove(self.sqr11)
        self.sqr12 = rand.choice(squares)
        squares.remove(self.sqr12)


    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        self.images = [CAT, FLOWER, DOG, TURTLE, BUNNY, TREE]

        # Draw the grid
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                # Compute x and y
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                if self.grid[row][column] == 1:
                    if row == 0 and column == 0:
                        image = self.images[self.sqr1]
                    elif row == 0 and column == 1:
                        image = self.images[self.sqr2]
                    elif row == 0 and column == 2:
                        image = self.images[self.sqr3]
                    elif row == 0 and column == 3:
                        image = self.images[self.sqr4]
                    elif row == 1 and column == 0:
                        image = self.images[self.sqr5]
                    elif row == 1 and column == 1:
                        image = self.images[self.sqr6]
                    elif row == 1 and column == 2:
                        image = self.images[self.sqr7]
                    elif row == 1 and column == 3:
                        image = self.images[self.sqr8]
                    elif row == 2 and column == 0:
                        image = self.images[self.sqr9]
                    elif row == 2 and column == 1:
                        image = self.images[self.sqr10]
                    elif row == 2 and column == 2:
                        image = self.images[self.sqr11]
                    elif row == 2 and column == 3:
                        image = self.images[self.sqr12]
                    arcade.draw_lrwh_rectangle_textured(x-50, y-50, WIDTH, HEIGHT, image)
                else:
                    white = arcade.color.WHITE
                    arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, white)


    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """
 
        # Change the x/y screen coordinates to grid coordinates
        column = int(x // (WIDTH + MARGIN))
        row = int(y // (HEIGHT + MARGIN))
        arcade.play_sound(CLICK_SOUND)
 
        print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")
 
        # Make sure we are on-grid. It is possible to click in the upper right
        # corner in the margin and go to a grid location that doesn't exist
        if row < ROW_COUNT and column < COLUMN_COUNT:
 
            # Flip the location between 1 and 0.
           if self.grid[row][column] == 0:
               self.grid[row][column] = 1
           else:
               self.grid[row][column] = 0


def main():

    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()