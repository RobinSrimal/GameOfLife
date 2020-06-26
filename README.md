# GameOfLife

![screenshot](https://github.com/RobinSrimal/GameOfLife/blob/master/images/screenshot.png)


1. To run the Game of Life you need pygame installed. Best way would be to create a pipenv with the 
requirements.txt

2. You can chose if you want the Grid of the game to be flat or a ball by setting shape to 
either "flat" or "ball" when instantiating LifeGame. Also you can customize the number of rows and columns
and the cell_size. 

3. The game initializes with a random state. Pause and unpause the game by pressing "s" on the keyboard.

4. When the game is paused you can 

    4.1. Kill specific cells or bring them back to life by clicking on them.

    4.2. Clear the whole screen by pressing "c".

    4.3. Create a new random distribution by pressing "r".

5. Quit the game by pressing "q".

6. Cells change their color with their age. Currently code is commented out in both grids that gives each cell 
an increasing  chance to die the older they get. 




