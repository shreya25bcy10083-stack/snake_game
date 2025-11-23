🐍 Snake Game (Player Mode) — Python + Pygame

This is a simple Snake game built using Python and Pygame.
The game is player-controlled only (NO AI) and includes:
-10 food items per round
-30-second countdown timer
-Win / Lose status messages
-Smooth grid movement
-Restart anytime with R

🎮 How to Play:
Key	Action
ENTER-	Start the game
Arrow Keys-	Move the snake
R-	Restart the game
ESC / Window Close-	Quit the game

🕹 Game Rules
-Eat all 10 food items to win.
-Survive within 30 seconds.
-If you hit a wall or your own body → Game Over.
-If the timer reaches 0 → Time Up (You Lose).

📁 Project Structure
snake_ai/
│
├── main.py
├── snake.py
├── ai.py          ← (not used in player mode)
├── food.py
└── README.md

📦 Requirements

-Install Pygame:
  pip install pygame (type this in your terminal)
-Requires Python 3.8 or newer.

▶️ How to Run the Game
Open your terminal in the project folder and run:
  python main.py
A game window will open.

🧩 File Descriptions
main.py-
 Handles:
  -Game loop
  -User input
  -Timer
  -Drawing snake and food
  -Win/Lose logic

snake.py-
 Defines the Snake class:
  -Movement
  -Direction changes
  -Growth
  -Collision detection

food.py-
 -Handles food generation:
 -Random spawn
 -Respawn when eaten

ai.py-
 -Contains AI pathfinding code
  (not used in this version but kept for future upgrades)

📝 Author
Created by Shreya :)
registration no.- 25bcy10083
