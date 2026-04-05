# Platformer Game (PyQt5)

A 2D platformer built using PyQt5 instead of Pygame. The game includes level selection, hazards, enemies, a win condition, and simple record tracking.

## Overview

This project is a classic platformer-style game implemented with PyQt5 graphics and audio. Players navigate a character through tile-based levels, avoid hazards, and reach the exit door to win. The game includes:

- Main menu with Start, Scoreboard, and Exit
- Level selection menu for multiple levels
- Enemies and lava hazards
- Timer-based scoring and scoreboard tracking
- Restart and Back menu controls

## Requirements

- Python 3.8+
- PyQt5

Install dependencies with:

```bash
python -m pip install pyqt5
```

## Run the Game

From the root directory:

```bash
python main.py
```

## Controls

- `A` — move left
- `D` — move right
- `W` — jump
- Mouse click — select menu buttons

## Gameplay

- Reach the door to win the level.
- The timer tracks how long it takes to finish.
- Touching lava or colliding with an enemy from the side results in death.
- Jumping on top of an enemy defeats it and makes the player bounce.
- After winning or dying, use Restart or Back to continue.

## Project Structure

- `main.py` — launches the application and starts the test runner
- `game.py` — handles menus, input polling, and level startup
- `level.py` — loads level text files and creates scene objects
- `player.py` — player movement, collision detection, and scoring
- `enemy.py` — enemy movement and collision behavior
- `lava.py`, `door.py` — static hazard and exit objects
- `button.py`, `back.py`, `restart.py`, `exit.py` — interactive menu buttons
- `tester.py` — validates that each level contains required objects
- `SCOREBOARD` — plain text scoreboard file
- `LEVELS/` — level layout files
- `images/`, `music/` — game assets

## Notes

- Levels are loaded from simple text files in `LEVELS/`.
- The scoreboard is saved to the `SCOREBOARD` text file.
- Audio is played using PyQt5 multimedia.
- The game uses static images rather than frame-based animation.

## Known Issues

- Some collision edge cases may cause unintended movement.
- Jump behavior can be inconsistent on enemies.
- The current button implementation is basic and could be refactored.

## Screenshots

Screenshots are available in the `SCREENSHOTS/` folder.
