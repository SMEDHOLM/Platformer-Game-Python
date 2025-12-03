LAUNCH:
download repository and run python main.py in terminal in root
LAUNCH:
download repository and run python main.py in terminal in root
1. Overview
 This project is a platformer game without using pygame library. Like most platformer games, it is in 2D format. These games
 have various win conditions, such as defeating a boss, killing all enemies, or, in this case, reaching
 a specific point. As the name suggests, platformer gameplay consists of jumping on different
 platforms.
 This implementation has two difficulty levels—medium and advanced. The work was completed at
 the advanced level.
 When the main script is launched, the main menu appears with three buttons: Exit (closes the
 game), Scoreboard (displays the scoreboard), and Start (takes the user to the level selection menu,
 where they can choose between three different levels).
 The game graphics are images downloaded from the internet. Additionally, the game uses various
 sounds: background music and a jump sound.
 2. User Guide
 The program starts from the main script.
 To close the game, press “EXIT.”
 To view the scoreboard, press “SCOREBOARD.”
 To start the game, press “START.”
 Choose a level, such as “LEVEL1.”
 To return to the main menu, press “BACK.”
 Movement:
 A – move left
 D – move right
 W – jump
 The character cannot jump unless standing on solid ground.
 To stop movement, press the opposite direction key.
 To move faster, hold the movement key.
 Win condition: reaching the door. A timer shows microseconds. After reaching the door, a menu
 appears displaying the score and notifying if a new record is achieved.
If the player touches lava or collides with a monster, they die, and a menu appears.
 If the player is above a monster, the monster dies and the player jumps.
 3. External Libraries
 The only external library used is PyQt5. Images, drawing, and music playback use its methods.
 4. Program Structure
 Each script (except main) contains a class.
 Tester – checks if the level has both player and door.
 Main – runs tests, creates Game, calls displayMainMenu.
 Game – handles menus, key updates, starts levels.
 Button – draws interactive buttons.
 Level – loads level file and creates objects based on characters.
 Lava, Door – place images.
 Enemy – movement and collision logic.
 Player – movement, collisions, win/loss detection, scoreboard handling.
 Restart, Back, Exit – button classes.
 5. Algorithms
 Important functions:
 move – applies dx, dy to coordinates.
 CollisionX / CollisionY – converts pixel coordinates to grid and detects block collisions.
 OnGround – checks if player stands on a block.
 add_item_to_scene – generates objects based on level file characters.
 6. Data Structures
 Lists were used because they are simple and allow modification.
 7. Files
 Game uses PNG, GIF, MP3, and TXT.
Levels are 32×17 text files.
 Scoreboard is a TXT with entries for best times.
 8. Testing
 Testing performed by gameplay. Walls prevent falling out of the level. Occasional crashes occur.
 9. Known Issues
 Player sometimes enters walls or moves incorrectly.
 Player doesn’t always jump on monsters.
 Extra button classes should be refactored.
 Graphics from internet, no animations.
 Buttons do not change color on text hover.
 No background image.
 10. Strengths and Weaknesses
 Strengths:
 1. Difficulty hides small level size.
 2. Good background music.
 3. Levels can be edited without coding.
 Weaknesses:
 1. Occasional crashes.
 2. Character movement bugs.
 3. Jump inconsistency on monsters.
 11. Deviations
 Collision methods required much more time.
 12. Workflow
 Level → player movement → enemies/lava → door → audio/graphics → menus → timer → extra
 levels → scoreboard.
13. Evaluation
 Proud of the work despite flaws caused by library limitations.
![Screenshot_3-12-2025_235052_](https://github.com/user-attachments/assets/c69a3eb5-9d67-4034-bdb1-5b2fea56b584)
![Screenshot_3-12-2025_23511_](https://github.com/user-attachments/assets/02ef9ee7-1f64-4f64-b322-cc648b48788b)
![Screenshot_3-12-2025_235113_](https://github.com/user-attachments/assets/6dae27d1-7d10-424e-bbeb-69890ac8da3a)
![Screenshot_3-12-2025_235128_](https://github.com/user-attachments/assets/c490b071-811b-4dac-b474-f8c385f254ed)
