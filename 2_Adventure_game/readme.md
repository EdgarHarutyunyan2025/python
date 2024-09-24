# Pygame Space Shooter Game

This Python script implements a simple space shooter game using the Pygame library. Players control a fighter spaceship to avoid incoming alien ships and shoot rockets to destroy them. The game features basic keyboard controls and incorporates sounds and images for a more immersive experience.

## Features

- **Player Controls**: Use arrow keys (`LEFT` and `RIGHT`) to move the fighter spaceship horizontally across the screen. Press `SPACE` to fire rockets towards the aliens.
  
- **Alien Interaction**: Aliens descend from the top of the screen, and the player must shoot rockets to destroy them before they reach the fighter spaceship.
  
- **Scoring**: Each successful hit on an alien awards points. The game dynamically increases the difficulty as more aliens are destroyed.

## Setup and Requirements

1. **Python and Pygame Installation**:
   - Ensure you have Python 3.x installed on your system.
   - Install Pygame using the following command:
     ```
     pip install pygame
     ```

2. **Game Assets**:
   - Download or prepare images (`fighter.png`, `rocket.png`, `alien.png`) and sounds (`11_Stage.mp3`, `vyistrel.mp3`, `vzryiv.mp3`, `24_Game Over.mp3`) and place them in the appropriate directory (`2_Adventure_game/images/` and `2_Adventure_game/mp3/`).

## How to Play

1. **Run the Game**:
   - Execute the script `2_Adventure_game.py` to start the game:
     ```
     python 2_Adventure_game.py
     ```

2. **Gameplay Instructions**:
   - Use `LEFT` and `RIGHT` arrow keys to move the fighter spaceship.
   - Press `SPACE` to shoot rockets at the aliens.
   - Avoid collisions between the fighter spaceship and descending aliens.
   - Score points by destroying aliens with rockets.

3. **End of Game**:
   - The game ends if an alien collides with the fighter spaceship.
   - Upon game over, the total score is displayed along with a game over message and sound.

## Notes

- Adjust game parameters (`STAP`, `ROCKET_STAP`, `ALIEN_STAP`) in the script to fine-tune game difficulty and performance.
- Ensure a functional microphone setup for optimal gameplay experience.

## Author

- Edgar Hautyunyan

