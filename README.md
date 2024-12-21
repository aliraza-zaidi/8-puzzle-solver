# 8-Puzzle Solver Using A* Algorithm with Pygame Visualization

## Overview

This project implements a solver for the 8-puzzle problem using the A* search algorithm. The puzzle consists of a 3x3 grid with 8 numbered tiles and one blank space. The goal is to rearrange the tiles from an initial configuration to a target configuration by sliding tiles into the blank space. The A* algorithm is used to efficiently find the optimal sequence of moves.

Additionally, the solver's progress is visualized using Pygame, showing each step of the algorithm as it finds the solution.

## Features

- **A * Algorithm**: The solver uses the A* algorithm to find the shortest path from the initial state to the goal state. It employs a heuristic based on the Manhattan distance to evaluate the cost of moves.
- **Pygame Visualization**: The entire process is visualized using Pygame, where the tiles' movements and the state transitions are shown graphically.

## Installation

Install the required libraries using pip:

```bash
pip install pygame

## Run Script

Run the script using:

```bash
python3 play.py
