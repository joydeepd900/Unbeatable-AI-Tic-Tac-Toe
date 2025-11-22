## Problem Statement
To design and implement an intelligent agent capable of playing Tic-Tac-Toe against a human opponent without ever losing. This system utilizes the Minimax algorithm to demonstrate the concept of Adversarial Search in a zero-sum game environment, solving the problem of automated decision-making under competitive constraints.

## Scope of the Project
The project focuses on the backend logic of Game Theory. It includes a console-based interface for user interaction, a rule engine for game state validation, and an AI engine for move calculation. The scope is limited to a standard 3x3 grid.

## Target Users
* **AI Students & Learners:** Individuals looking to understand the practical implementation of Adversarial Search and the Minimax algorithm.
* **Evaluators & Instructors:** Academic staff assessing the correct application of "Fundamentals in AI & ML" .
* **Game Theory Enthusiasts:** Developers interested in the logic behind unsolvable games and perfect-play algorithms.

## High-Level Features
1.  **Unbeatable AI Engine:** Implements the recursive Minimax algorithm to evaluate the Game Tree and select the mathematically optimal move every turn.
2.  **Interactive Game Loop:** A robust console interface that accepts user input, updates the board state, and displays results in real-time.
3.  **Smart Input Validation:** Prevents the application from crashing by handling invalid inputs (e.g., non-integers, out-of-bound numbers, or occupied spaces).
4.  **Automated Session Logging:** A reporting module that writes the outcome of every match (Win/Loss/Draw) to a 'game_history.txt' file for tracking performance.
