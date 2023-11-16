# Super-Goblin-Slayer-Final
Pygame
Description of SUPER SPACE GOBLIN SLAYER
Setting Up the Game Window:
•	The game window is created using the Pygame library with a width and height of 750 pixels.
•	Various images for rockets, lasers, and the background are loaded and resized.
Classes:
Laser Class:
•	Represents a laser beam with a starting position (x, y), an image, and collision detection.
•	It can move upward (move method), check if it's off-screen, and detect collisions.
Ship Class:
•	A general class for both the player's ship and enemy ships.
•	Manages the ship's position, health, image, lasers, and shooting mechanism.
•	Has methods to draw the ship, move lasers, handle cooldown for shooting, and check collisions.
•	The player's ship has additional features like a health bar and customized shooting behavior.
Player Class (inherits from Ship):
•	Represents the player's ship, inheriting attributes and methods from the Ship class.
•	Customized for the player with a unique image, laser, and health bar.
•	Overrides the shoot and move lasers methods to suit the player's ship behavior.
Enemy Class (inherits from Ship):
•	Represents an enemy ship with specific images and behaviors.
•	Inherits from the Ship class but has its own movement patterns and shooting behaviors.
Functions:
1.	collide Function:
•	Takes two objects and checks if their masks (used for precise collision detection) overlap.
•	Used to detect collisions between lasers, ships, and player.
•	
2.	redraw_window Function:
•	Clears the game window and redraws all game elements.
•	Displays information like the player's lives and the current level.
•	If the player loses, it shows a "You Lost!" message.



Main Game Loop:
•	Initializes game variables, including the player, enemies, lives, and level.
•	Inside the game loop, it checks for player input (keyboard keys) and updates the game accordingly.
•	Manages enemy waves, their movements, and their interactions with the player.
•	Handles collisions, player health, and the game state (whether the player won or lost).
Closing the Game:
•	The game continues to run until the player quits or loses all lives.
•	After the game ends, a "You Lost!" message is displayed for a brief period.

WHY I CHOOSE UNIT TEST?
1.	Early Bug Detection: Unit tests allow you to catch and fix bugs early in the development process. By testing individual components of your code in isolation, you can identify and address issues before they propagate to other parts of the system.
2.	Improved Code Quality: Writing unit tests often leads to better code design and modularity. When you design code with testing in mind, you tend to create smaller, more focused functions and classes, making your codebase more maintainable and understandable.
3.	Code Confidence: Unit tests provide a safety net for refactoring and code changes. When you make modifications to your code, running the associated unit tests helps ensure that existing functionality is not broken. This confidence is crucial when working on large and complex projects.
4.	Documentation: Unit tests serve as a form of documentation. They provide examples of how to use the code, and by reading the tests, developers can gain insights into the expected behavior of different components.
5.	Regression Testing: Unit tests act as a form of regression testing, ensuring that new changes don't introduce unexpected side effects or break existing functionality. This becomes especially important as a project evolves and more features are added.


