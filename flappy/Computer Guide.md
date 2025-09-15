# Flappy guide: Computer edition

This guide is written for a Windows computer.

## Step 0: Setup

Some of these steps may already have been completed. If it looks like someone has already done one of these for you, just move on to the next one.

First, make sure you have Python installed on your computer. On Windows, you can install it through the Microsoft store.

Next, create a new folder - a folder in your desktop will do fine.

Open the folder, then right-click the background of the file explorer. One of the options should be "Open in Terminal"; select that one. A black terminal should pop up. Write in the following lines (you will likely have to  wait after typing the first one):

```powershell
python -m venv env
New-Item flappy.py
code .
```

This should open Visual Studio code. Hit "Accept" on any permissions dialogs that open up, then look at the left-side toolbar. Below the triangle with a bug, there should be some squares - that's the extension menu. Open it up, find a Python extension, and install it.

Once that's done installing, open the pages tab on the left navbar and select `flappy.py`. Hit <kbd>CTRL</kbd>+<kbd>F5</kbd> - a dropdown should open up from the top. Select the option with "env" in it. Now hit <kbd>CTRL</kbd>+<kbd>`</kbd> and type:

```powershell
python -m pip install pygame
```

## Step 1: Imports

These are the modules and external functions we'll be using for the project. Type them into `flappy.py`.

```
import pygame
from random import randint
from time import sleep
```

## Step 2: Draw the player

This will have several sub-steps. First, add a blank line, then add the following line to set up the screen:

```python
pygame.init()
WIDTH, HEIGHT = 1280, 720
screen=pygame.display.set_mode((WIDTH, HEIGHT))
TICKS = 32

WHITE = (0, 0, 0)
BLACK = (255, 255, 255)
screen.fill(WHITE)
pygame.display.flip()
```

Next, add another blank line, then these lines to define what the player looks like:

```python
PLAYER_X = WIDTH/10
player_y = HEIGHT/2
PLAYER_R = 5
```

Finally, add one last blank line, then add these lines to draw the player once every tick.

```python
game_over = False

sleep(1)

while not game_over:
    sleep(1/TICKS)
  
    screen.fill(WHITE)
    pygame.draw.circle(screen, BLACK, (PLAYER_X, player_y), PLAYER_R)

    pygame.display.flip()
```

You can use <kbd>CTRL</kbd>+<kbd>F5</kbd> to test the code. If something breaks, compare it to this checkpoint:

<details>
<summary>Step 2 code</summary>

```python
import pygame
from random import randint
from time import sleep

PLAYER_X = WIDTH/10
player_y = HEIGHT/2
PLAYER_R = 5

game_over = False

sleep(1)

while not game_over:
    sleep(1/TICKS)
  
    screen.fill(WHITE)
    pygame.draw.circle(screen, BLACK, (PLAYER_X, player_y), PLAYER_R)

    pygame.display.flip()
```
</details>

This will run endlessly. When you're ready to stop, go back to the VS Code, click the bottom window, and hit <kbd>CTRL</kbd>+<kbd>C</kbd>.

## Step 3: Make the player fall

Before we can make the player fall, we need to explain what "falling" looks like. Add these lines just below `PLAYER_R=5`:

```python
player_v = 0
MAX_V = HEIGHT/TICKS
GRAVITY = HEIGHT/4/TICKS
```
These will store how fast the player is moving, how fast they can move, and how fast they speed up.

Now that we know those things, we can actually make the following happen. Two lines below `sleep(1/TICKS)`, add the following:

```python
    player_v += GRAVITY
    player_v = min(player_v, MAX_V)
    player_y += player_v
    if player_y > HEIGHT:
        game_over = True
```

Make sure the indentation is right! There should be four spaces before `player_v`, just like before `sleep`.

This will make the player fall. As a bonus, it'll end the game once you fall below the screen, so you won't have to break manually anymore :)

Run the program again to see the physics play out. If something breaks, compare your code to this dropdown:

<details>
<summary>Step 3 code</summary>

```python
import pygame
from random import randint
from time import sleep

pygame.init()
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
TICKS = 32

WHITE = (0, 0, 0)
BLACK = (255, 255, 255)
screen.fill(WHITE)
pygame.display.flip()

PLAYER_X = WIDTH/10
player_y = HEIGHT/2
PLAYER_R = 5
player_v = 0
MAX_V = HEIGHT/TICKS
GRAVITY = HEIGHT/4/TICKS

game_over = False

sleep(1)

while not game_over:
    sleep(1/TICKS)

    player_v += GRAVITY
    player_v = min(player_v, MAX_V)
    player_y += player_v
    if player_y > HEIGHT:
        game_over = True

    screen.fill(WHITE)
    pygame.draw.circle(screen, BLACK, (PLAYER_X, player_y), PLAYER_R)

    pygame.display.flip()
```
</details>

## Step 4: Let the player jump

So far, this is a video, not a game. To make it interactive, let's let the player jump. First, add this line below `GRAVITY=HEIGHT/4/TICKS` to set how fast the player jumps:

```python
JUMP_V = -HEIGHT/TICKS
```

See how it's negative? That's because on the calculator, "negative" means "up" and "positive" means "down" - which is also why gravity is positive!

Then, add the following lines two lines below `sleep(1/TICKS)` to let the player push a button to jump.

```python
    clicked = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type in {pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN}:
            clicked = True
    if clicked:
        player_v = JUMP_V
    else:
```

Indent the next two lines. Together with what you just added, it should look like this:

```python
    clicked = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type in {pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN}:
            clicked = True

    if clicked:
        player_v = JUMP_V
    else:
        player_v += GRAVITY
        player_v = min(player_v, MAX_V)
```

Altogether, this means "make the player jump if they hit a button, or fall if they didn't." Run the code to check if it works!

<details>
<summary>Step 4 code</summary>

```python
import pygame
from random import randint
from time import sleep

pygame.init()
WIDTH,HEIGHT=1280, 720
screen = pygame.display.set_mode((WIDTH,HEIGHT))
TICKS = 32

WHITE = (0,0,0)
BLACK = (255, 255, 255)
screen.fill(WHITE)
pygame.display.flip()

PLAYER_X = WIDTH/10
player_y = HEIGHT/2
PLAYER_R = 5
player_v = 0
MAX_V = HEIGHT/TICKS
GRAVITY = HEIGHT/4/TICKS
JUMP_V = -HEIGHT/TICKS

game_over=False

sleep(1)

while not game_over:
    sleep(1/TICKS)

    clicked = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type in {pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN}:
            clicked = True

    if clicked:
        player_v = JUMP_V
    else:
        player_v += GRAVITY
        player_v = min(player_v,MAX_V)
    player_y += player_v
    if player_y > HEIGHT:
        game_over = True

    screen.fill(WHITE)
    pygame.draw.circle(screen, BLACK, (PLAYER_X, player_y), PLAYER_R)

    pygame.display.flip()
```
</details>

## Step 5: Moving wall

So far, the game is just a dot jumping endlessly. To make it more interesting, let's add a wall for the player to avoid. First, set what the wall should look like two lines below `JUMP_V=-HEIGHT/TICKS`:

```python
wall_x = WIDTH
wall_v = -WIDTH/TICKS
GAP_HEIGHT = HEIGHT//3
wall_gap = randint(0, HEIGHT-GAP_HEIGHT)
```

Next, make it move across the scene, moving all the way to the right if it reaches the end. Place these two lines below `game_over=True`, but delete four of the spaces before you do so:

```python
    wall_x += wall_v
    if wall_x < 0:
        wall_x = WIDTH
        wall_gap = randint(0,HEIGHT-GAP_HEIGHT)
```

Finally, add these lines below `pygame.draw.circle(screen,BLACK,(PLAYER_X,player_y),PLAYER_R)` to draw the top and bottom halves of the wall.

```python
    pygame.draw.line(screen, BLACK, (wall_x, 0), (wall_x, wall_gap))
    pygame.draw.line(screen, BLACK, (wall_x, wall_gap+GAP_HEIGHT), (wall_x, HEIGHT))
```

Run the code to see the wall move. Nothing will happen if you hit the wall quite yet - you'll have to imagine that you're losing in your mind.

<details>
<summary>Step 5 code</summary>

```python
import pygame
from random import randint
from time import sleep

pygame.init()
WIDTH,HEIGHT = 1280,720
screen = pygame.display.set_mode((WIDTH,HEIGHT))
TICKS = 32

WHITE = (0, 0, 0)
BLACK = (255, 255, 255)
screen.fill(WHITE)
pygame.display.flip()

PLAYER_X = WIDTH/10
player_y = HEIGHT/2
PLAYER_R = 5
player_v = 0
MAX_V = HEIGHT/TICKS
GRAVITY = HEIGHT/4/TICKS
JUMP_V = -HEIGHT/TICKS

wall_x = WIDTH
wall_v = -WIDTH/TICKS
GAP_HEIGHT = HEIGHT//3
wall_gap = randint(0, HEIGHT-GAP_HEIGHT)

game_over=False

sleep(1)

while not game_over:
    sleep(1/TICKS)

    clicked = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type in {pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN}:
            clicked = True

    if clicked:
        player_v = JUMP_V
    else:
        player_v += GRAVITY
        player_v = min(player_v, MAX_V)
    player_y += player_v
    if player_y > HEIGHT:
        game_over = True
    
    wall_x += wall_v
    if wall_x < 0:
        wall_x = WIDTH
        wall_gap = randint(0, HEIGHT-GAP_HEIGHT)

    screen.fill(WHITE)
    pygame.draw.circle(screen, BLACK, (PLAYER_X, player_y), PLAYER_R)
    pygame.draw.line(screen, BLACK, (wall_x, 0), (wall_x, wall_gap))
    pygame.draw.line(screen, BLACK, (wall_x, wall_gap+GAP_HEIGHT), (wall_x, HEIGHT))

    pygame.display.flip()
```
</details>


## Step 6: Let the player lose

Detecting a collision is a little harder than it might seem. It's not enough to check if the player and wall are in the same place - since the game runs on frames, it's possible for the wall to skip over the player without touching them. Instead, we'll need to compare the wall's position between two given frames. First, add the following line just above `wall_x+=wall_v` so the wall doesn't forget where it was:

```python
    old_wall_x = wall_x
```

Next, add the following code two lines below `wall_gap=randint(0,HEIGHT-GAP_HEIGHT)`. Make sure to delete four spaces before doing so.

```python
    if wall_x <= PLAYER_X <= old_wall_x:
        if not wall_gap <= player_y <= wall_gap+GAP_HEIGHT:
            game_over = True
```

Run the code to test it.

<details>
<summary>Step 6 code</summary>

```python
import pygame
from random import randint
from time import sleep

pygame.init()
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH,HEIGHT))
TICKS = 32

WHITE = (0, 0, 0)
BLACK = (255, 255, 255)
screen.fill(WHITE)
pygame.display.flip()

PLAYER_X = WIDTH/10
player_y = HEIGHT/2
PLAYER_R = 5
player_v = 0
MAX_V = HEIGHT/TICKS
GRAVITY = HEIGHT/4/TICKS
JUMP_V = -HEIGHT/TICKS

wall_x = WIDTH
wall_v = -WIDTH/TICKS
GAP_HEIGHT = HEIGHT//3
wall_gap = randint(0, HEIGHT-GAP_HEIGHT)

game_over = False

sleep(1)

while not game_over:
    sleep(1/TICKS)

    clicked = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type in {pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN}:
            clicked = True

    if clicked:
        player_v = JUMP_V
    else:
        player_v += GRAVITY
        player_v = min(player_v,MAX_V)
    player_y += player_v
    if player_y > HEIGHT:
        game_over = True
    
    wall_x += wall_v
    if wall_x < 0:
        wall_x = WIDTH
        wall_gap = randint(0,HEIGHT-GAP_HEIGHT)
    if wall_x <= PLAYER_X <= old_wall_x:
        if not wall_gap <= player_y <= wall_gap+GAP_HEIGHT:
            game_over = True

    screen.fill(WHITE)
    pygame.draw.circle(screen, BLACK, (PLAYER_X, player_y), PLAYER_R)
    pygame.draw.line(screen, BLACK, (wall_x, 0), (wall_x, wall_gap))
    pygame.draw.line(screen, BLACK, (wall_x, wall_gap+GAP_HEIGHT), (wall_x, HEIGHT))

    pygame.display.flip()
```
</details>

## Step 7: Score

This is a fully functional game! For some flavor, we can add a score. Start by telling the game how many points the player has and how/where to write their score two lines after the first `wall_gap=randint(0,HEIGHT-GAP_HEIGHT)`:

```python
score=0
SCORE_X = WIDTH/2
SCORE_Y = HEIGHT/10
score_font = pygame.font.Font(pygame.font.get_default_font(), 20)
```

Now, give the player a point if they pass the wall without dying. Add these lines right after the second `game_over = True`, deleting four spaces:

```python
        else:
            score += 1
```

Finally, draw the score for the player. Make this the second-last line of the program:

```python
    screen.blit(score_font.render(str(score), 1, BLACK), (SCORE_X, SCORE_Y))
```

That's it! Run the game to see the finished product.

<details>
<summary>Completed game!</summary>

```python
import pygame
from random import randint
from time import sleep

pygame.init()
WIDTH,HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
TICKS = 32

WHITE = (0, 0, 0)
BLACK = (255, 255, 255)
screen.fill(WHITE)
pygame.display.flip()

PLAYER_X = WIDTH/10
player_y = HEIGHT/2
PLAYER_R = 5
player_v = 0
MAX_V = HEIGHT/TICKS
GRAVITY = HEIGHT/4/TICKS
JUMP_V = -HEIGHT/TICKS

wall_x = WIDTH
wall_v = -WIDTH/TICKS
GAP_HEIGHT = HEIGHT//3
wall_gap = randint(0, HEIGHT-GAP_HEIGHT)

score = 0
SCORE_X = WIDTH/2
SCORE_Y = HEIGHT/10
score_font = pygame.font.Font(pygame.font.get_default_font(), 20)

game_over = False

sleep(1)

while not game_over:
    sleep(1/TICKS)

    clicked = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type in {pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN}:
            clicked = True

    if clicked:
        player_v = JUMP_V
    else:
        player_v += GRAVITY
        player_v = min(player_v,MAX_V)
    player_y += player_v
    if player_y > HEIGHT:
        game_over = True
    
    wall_x += wall_v
    if wall_x < 0:
        wall_x = WIDTH
        wall_gap = randint(0, HEIGHT-GAP_HEIGHT)
    if wall_x <= PLAYER_X <= old_wall_x:
        if not wall_gap <= player_y <= wall_gap+GAP_HEIGHT:
            game_over = True
        else:
            score += 1

    screen.fill(WHITE)
    pygame.draw.circle(screen, BLACK, (PLAYER_X, player_y), PLAYER_R)
    pygame.draw.line(screen, BLACK, (wall_x, 0), (wall_x, wall_gap))
    pygame.draw.line(screen, BLACK, (wall_x, wall_gap+GAP_HEIGHT), (wall_x, HEIGHT))
    screen.blit(score_font.render(str(score), 1, BLACK), (SCORE_X, SCORE_Y))
    pygame.display.flip()
```
            </details>
