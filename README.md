# README

## Overview

This Python program reads maze definitions from text files, finds the entrance and exit, 
and determines the path from the entrance to the exit. The maze is represented as a 2D grid 
of integers `1` and `0`, where `1` indicates a path and `0` indicates a wall. The entrance 
is the lone `1` in the first row, and the exit is the lone `1` in the last row.

## Prerequisites

- Python 3.x
- Text files named `mazeX.txt` (e.g., `maze1.txt`, `maze2.txt`) containing the maze data in the following format (any `a x a` size grid is acceptable):
```
0 0 0 1 0
0 0 1 1 1
1 1 1 0 0
1 0 0 0 0
1 0 0 0 0
```

## Instructions

### Setup

1. Ensure you have Python installed on your system. You can download Python from https://www.python.org/.

2. Create a directory for your project and place the Python script and maze files (`maze1.txt`, `maze2.txt`, etc.) in the same directory.

#### Running the Code

1. Open a terminal or command prompt.

2. Navigate to the directory containing the Python script and maze files: `cd path/to/your/directory`

3. Run the script:
   `python the_amazing_race.py`

### Output

The program will output the path for each maze file in the following format:

`Path found for Maze 1:`

`(0, 1) (1, 1) (2, 1) (2, 2) (2, 3) (3, 3) (3, 4) (4, 4)`

If no path is found, it will output

`No path found!`
