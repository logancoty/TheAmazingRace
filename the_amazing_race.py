import os
import re

def read_maze(file_path):
    """
    Reads the maze from the given file path and returns it as a 2D list.
    Each line in the file is a row in the maze.
    """
    with open(file_path, 'r') as file:
        maze = []
        for line in file:
            maze.append([int(x) for x in line.split()])
    return maze

def find_start_coordinates(maze):
    """
    Finds the entrance (the lone 1 of the first row) of the maze.
    """
    for j in range(len(maze[0])):
        if maze[0][j] == 1:
            return (0, j)

def find_end_coordinates(maze):
    """
    Finds the exit (the lone 1 of the last row) of the maze.
    """
    for j in range(len(maze[-1])):
        if maze[-1][j] == 1:
            return (len(maze) - 1, j)

def find_path(maze, x, y, endX, endY, path):
    """
    Recursively finds a path from the current position (x, y) to the exit (endX, endY).
    Marks the visited cells and backtracks if necessary.
    """
    # Check boundaries and if the current cell is a path
    if x < 0 or y < 0 or x >= len(maze) or y >= len(maze[0]) or maze[x][y] != 1:
        return False

    # Add the current cell to the path
    path.append((x, y))
    
    # Mark as visited
    maze[x][y] = -1  

    # Check if we have reached the exit
    if (x, y) == (endX, endY):
        return True

    # Recursively search neighboring cells
    if (find_path(maze, x + 1, y, endX, endY, path) or  # Down
        find_path(maze, x - 1, y, endX, endY, path) or  # Up
        find_path(maze, x, y + 1, endX, endY, path) or  # Right
        find_path(maze, x, y - 1, endX, endY, path)):   # Left
        return True

    # If no path is found, remove cell from path and backtrack
    path.pop()
    return False



def main():
    # Get the current working directory of the script
    cwd = os.getcwd()

    # Create list of all files in the current working directory
    files_in_directory = os.listdir(cwd)

    # Filter files that match the pattern "mazeX.txt"
    maze_files = [f for f in files_in_directory if re.match(r'maze\d+\.txt', f)]

    # Sort maze files in ascending order by number in the filename
    maze_files.sort(key=lambda f: int(re.search(r'\d+', f).group()))
    
    # Loop through each maze file
    for index, maze_file in enumerate(maze_files):
        maze_path = os.path.join(cwd, maze_file)

        maze = read_maze(maze_file)

        # Find the start and end coordinates
        startX, startY = find_start_coordinates(maze)
        endX, endY = find_end_coordinates(maze)

        # List to store the path
        path = []

        # Find and print the path
        if find_path(maze, startX, startY, endX, endY, path):
            print("Path found for Maze " + str(index + 1) + ":")
            for step in path:
                print(step, end=" ")
        else:
            print("No path found!")
        
        # Print empty lines for readability in output
        print()
        print()



if __name__ == "__main__":
    main()

