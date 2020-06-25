import sys, pygame
from GridBall import GridBall
from GridFlat import GridFlat

# dead color
black = 0, 0, 0


# living colors sorted by age, oldest at the top
maroon = 128,0,0
dark_red = 139,0,0
brown = 165,42,42 
firebrick = 178,34,34
crimson = 220,20,60
red = 255,0,0
tomato = 255,99,71
coral = 255,127,80
indian_red = 205,92,92
light_coral = 240,128,128
dark_salmon = 233,150,122
salmon = 250,128,114
light_salmon = 255,160,122
orange_red = 255,69,0
dark_orange = 255,140,0
orange = 255,165,0
gold = 255,215,0
yellow = 255,255,0
yellow_green = 154,205,50
dark_olive_green = 85,107,47
olive_drab = 107,142,35
lawn_green = 124,252,0
green_yellow = 173,255,47
dark_green = 0,100,0
 
# lookup table for colors
colors = {0:dark_green, 1:green_yellow, 2:lawn_green, 3:olive_drab, 4:dark_olive_green,
5:yellow_green,6:yellow,7:gold, 8:orange, 9:dark_orange, 10:orange_red, 11:light_salmon,
12:salmon, 13:dark_salmon, 14:light_coral, 15:indian_red, 16:coral, 17:tomato,
18:red, 19:crimson, 20:firebrick, 21:brown, 22:dark_red, 23:maroon}

class LifeGame:

    def __init__(self, rows = 60, columns = 120, cell_size = 10, max_fps = 10, shape = "ball"):

        pygame.init()
        self.cell_size = cell_size
        self.rows = rows
        self.columns = columns
        self.board_size = self.columns * self.cell_size, self.rows*self.cell_size
        self.screen = pygame.display.set_mode(self.board_size)
        self.paused = False
        self.game_over = False
        self.max_fps = max_fps
        self.shape = shape

        if self.shape == "ball":
            
            self.game_grid = GridBall(self.rows, self.columns)
        
        elif self.shape == "flat":

            self.game_grid = GridFlat(self.rows, self.columns)

        else:

            print("please chose either ball or flat for the shape parameter")

        self.game_grid.create_grid()

    def clear_screen(self):

        self.screen.fill(black)

    def draw_grid(self):

        self.clear_screen()

        for row in range(self.rows):

            for column in range(self.columns):

                if self.game_grid.grid[row][column].alive:

                    age = self.game_grid.grid[row][column].age//2

                    if age > 23:

                        age = 23
                
                    color = colors[age]

                else:

                    color = black

                pygame.draw.circle(self.screen, color, 
                (int(column * self.cell_size + (self.cell_size / 2)),
                int(row * self.cell_size + (self.cell_size / 2))), 
                int(self.cell_size / 2),
                0)

        pygame.display.flip()

    def handle_events(self):

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:

                if event.unicode == "s":

                    if self.paused:

                        self.paused = False

                    else:

                        self.paused = True

                elif event.unicode == "r":

                    self.game_grid.create_grid()
                    self.game_grid.grid_random_state()
                    self.draw_grid()

                elif self.paused and event.unicode == "c":

                    self.game_grid.create_grid()
                    self.draw_grid()

                elif event.unicode == "q":

                    self.game_over = True

            if event.type == pygame.MOUSEBUTTONDOWN and self.paused:

                location = event.pos
                column = location[0] // self.cell_size
                row = location[1] // self.cell_size

                cell = self.game_grid.grid[row][column]

                if cell.alive:

                    cell.alive = False
                    cell.age = 0

                else:

                    cell.alive = True
                    
                self.draw_grid()

            if event.type == pygame.QUIT:

                sys.exit()

    def update_generation(self):

        self.game_grid.grid_count_neighbors()
        self.game_grid.grid_survive()

    def run(self):

        self.game_grid.grid_random_state()

        clock = pygame.time.Clock()

        while True:

            if self.game_over:
                return

            self.handle_events()

            if not self.paused:
                self.update_generation()
                self.draw_grid()

            clock.tick(self.max_fps)


if __name__ == "__main__":
    game = LifeGame()
    game.run()


