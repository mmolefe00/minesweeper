# start
# ===== FUNCTIONS ======
def game_reader(grid):
    # make output variable a 2d list to format into
    num_rows = 5
    num_cols = 5
    output = [[0 for _ in range(num_cols)] for _ in range(num_rows)]

    for count, row in enumerate(grid, start=0):         # count is x coordinate in grid
        for idx, value in enumerate(row, start=0):      # idx is y coordinate in grid
            out = 0
            if row[idx] != '#':

                # included count and idx restrictions to keep output value for current position within bounds:
                # north restriction: 0 < count <= 5 (no checking above grid (row -1)
                # south restriction: -1 <= count <= 3 (no checking below grid (row 5)
                # east restriction: idx <= 3 (no checking right of grid (column 5)
                # west restriction: 0 < idx <= 5 (no checking left of grid (column -1)


                # north neighbour:
                if 0 < count <= 5 and grid[count-1][idx] == '#':
                    # increase output value of current position by 1
                    out += 1

                # north-east neighbour:
                if 0 < count <= 5 and idx <= 3 and grid[count-1][idx+1] == '#':
                    # output value increments by 1 with each new condition met (+1 for every adj mine)
                    out += 1

                # east neighbour:
                if idx <= 3 and row[idx+1] == '#':
                    out += 1

                # south-east neighbour
                if -1 <= count <= 3 and -1 < idx <= 3 and grid[count+1][idx+1] == '#':
                    out += 1

                # south neighbour
                if -1 <= count <= 3 and grid[count+1][idx] == '#':
                    out += 1        # increase output number by 1

                # south-west neighbour
                if -1 <= count <= 3 and 0 < idx <= 5 and grid[count+1][idx-1] == '#':
                    out += 1        # increase output number by 1

                # west neighbour:
                if 0 < idx <= 5 and row[idx-1] == '#':
                    out += 1

                # north-west neighbour:
                if 0 < count <= 5 and 0 < idx <= 5 and grid[count-1][idx-1] == '#':
                    out += 1

                # replace numerical values into 'output' 2D list
                output[count][idx] = grid[count][idx].replace(f'{value}', f"{out}")
            else:
                # replace '#' values into 'output' 2D list
                output[count][idx] = grid[count][idx].replace(f'{value}', "#")

    return output


def output_format(grid):

    for row in grid:
        for column in row:
            print(f'{column}', end='    ')         # separates each column by a space
        print()                                 # new line for each row


# greeting and prompt
greeting = "Welcome to Minesweeper Reader!\n"
prompt = "This code takes a mine map of '#' & '-' and returns the numerical value of mines[#] surrounding each empty block [-].\n"
print(greeting + prompt)
mine_grid = [['-', '-', '-', '#', '#'],
             ['-', '#', '-', '-', '-'],
             ['-', '-', '#', '-', '-'],
             ['-', '#', '#', '-', '-'],
             ['-', '-', '-', '-', '-']]

# format input into grid
print('Initial Mine Map:')
output_format(mine_grid)

# format output into grid
print(f'\nOutput Mine Map:')
num_grid = game_reader(mine_grid)
output_format(num_grid)

# end
