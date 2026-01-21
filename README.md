# Turtle Flag Guessing Game 🏳️🐢

A simple Python mini-game built with **turtle** where a random flag is drawn on the screen and the player must guess the country name.  
Each correct guess gives **1 point** and removes that flag from the pool. You start with **3 lives** — three wrong guesses and the game ends.

## Features
- Draws flags using Python `turtle`
- Random flag selection with `random`
- Score system (**points**) and life system (**lives**)
- Flags are removed after a correct guess so you don’t get repeats

## How to Play
1. Run the script.
2. A flag appears in the turtle window.
3. Type your guess in the terminal exactly as the country function name:
   - `Germany`
   - `Spain`
   - `Sweden`
4. If you’re correct: +1 point and the flag is removed.
5. If you’re wrong: you lose 1 life.
6. Game ends when you run out of lives or guess all flags.

## Requirements
- Python 3.x  
- No extra libraries needed (uses built-in `turtle` and `random`)

## Run
```bash
python flag_game.py
