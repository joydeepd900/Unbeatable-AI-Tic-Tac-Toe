# Unbeatable-AI-Tic-Tac-Toe

## Overview
This project is a Python-based implementation of the Minimax Algorithm to solve the zero-sum game of Tic-Tac-Toe. The AI agent evaluates all possible future board states to play optimally, ensuring it never loses.

## Features
* **Unbeatable AI:** Uses recursive Minimax algorithm.
* **Game Logging:** Automatically saves match results to 'game_history.txt'.
* **Modular Design:** Separated logic, UI, and AI components.

## Tools Used
* **Programming Language:** Python .
* **Standard Libraries:** 'random','datetime' (for logging).

## Steps to Install & Run
1.  Ensure Python is installed.
2.  Clone the Repository: Download the Folder- AI_Tic-Tac-Toe
3.  Run the command: 'python main.py'

## Testings
**Test A: Functional Gameplay**
1.  Run the game.
2.  Enter a number (0-8) to place your 'X'.
3.  Verify that the 'O' (AI) responds immediately.

**Test B: AI Intelligence (The "Unbeatable" Test)**
1.  Play 3 full games.
2.  Try to trap the AI using "fork" strategies.
3.  **Success Criteria:** The AI must either Win or Force a Draw. It must NEVER lose.

**Test C: Robustness (Error Handling)**
1.  Enter a letter (e.g., "Z") instead of a number.
2.  Enter a number larger than 8 (e.g., "50").
3.  Try to place a mark on a spot already taken.
4.  **Success Criteria:** The program should print an error message ("Invalid input") and ask you to try again. It should NOT crash.

**Test D: Logging System**
1.  Complete a game (Win or Draw).
2.  Open the 'game_history.txt' file in the project folder.
3.  **Success Criteria:** A new line with the current timestamp and result should be present.
