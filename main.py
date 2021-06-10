import turtle
import time
import random
import copy

def make_grid(height):
    # make a 2d array with all filled with 0
    n = int(height/10)
    grid = [[0] * n for row in range(n)]

    return grid

def start_populate(height):
    # populate the grid with a random selection or "seed"
    grid = make_grid(height)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] = random.choices((0,1), weights=(90, 10))[0]

    return grid

def populate_cell(grid, edge, cells):

    # place initial cells
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # create the cell            
            cell = turtle.Turtle()
            cell.speed(0)
            cell.shape("square")
            cell.penup()
            cell.goto(edge - i * 10, edge - j * 10)
            cell.direction = "stop" 
            # make it the appropriate colour
            if grid[i][j] == 1:
                cell.color("black")
            else:
                cell.color("white")

            cells.append(cell)

    return cells


def is_one(grid, i, j, sum):

    # check if the neighbouring is on or not. Too clumsy to fit in the neighbour_check() function
    
    if grid[i+1][j] == 1:
        sum += 1
    if grid[i][j-1] == 1:
        sum += 1
    if grid[i-1][j-1] == 1:
        sum += 1
    if grid[i-1][j+1] == 1:
        sum += 1
    if grid[i+1][j+1] == 1:
        sum += 1
    if grid[i+1][j-1] == 1:
        sum += 1

    return sum
def neighbour_check(grid, i, j):

    # check the neighbours

    sum = 0

    if i+1 == len(grid):
        i = -1
    if j+1 >= len(grid[i]):
        j = -1

    sum = is_one(grid, i, j, sum)
    return sum

def rules(grid, sum, grid_copy):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            sum = neighbour_check(grid, i, j)

            #If there are less than two live cells surrounding the live cell, it dies
            if sum < 2 and grid[i][j] == 1:
                grid_copy[i][j] = 0
            # if there is three live cells around a dead cell, it becomes live
            elif sum == 3 and grid[i][j] == 0:
                grid_copy[i][j] = 1
            # if there are two or three live around a live cell, it lives on
            elif (sum == 2 or sum == 3) and grid[i][j] == 1:
                grid_copy[i][j] = 1
            # if there is greater than 3 surrounding the live cell, it dies
            elif sum > 3 and grid[i][j] == 1:
                grid_copy[i][j] = 0

    return grid_copy

def main():

    #initialize some variables
    height = 600
    delay = 0.1
    edge = height/2
    sum = 0
    cells = []

    # make the screen
    window = turtle.Screen()
    window.title("Conway's Game of Life, But turtles You know")
    window.bgcolor("white")
    window.setup(height, height)
    window.tracer(0)

    grid = start_populate(height)
    # game loop
    while True:
        window.update()

        cells = populate_cell(grid, edge, cells)
        grid_copy = copy.deepcopy(grid)
        sum = neighbour_check(grid, 1, 0)
        
        grid = rules(grid, sum, grid_copy)
        
        # deleting the turtles. Dosent seem to help with memory usage problem
        for cell in cells:
            del cell
        time.sleep(delay)

main()
