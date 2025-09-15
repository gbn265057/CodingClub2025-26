# Flappy Guide: Calculator Edition

For this guide, you will need a TI-Nspire calculator with Python. If your TI-Nspire, doesn't have everything you need, you'll know by the end of Step 1.

## Step 0: Make a document

Follow the following steps to make a new Python project.

1. Home
2. New
3. Add Python
4. New
5. Name: FlappyCalculator; Type: Blank Program. Hit Enter.
6. Save (CTRL+S)
7. File Name: Flappy Calculator. Hit Enter.

## Step 1: Imports

These are the external tools we'll be using in the project. All of them will be available from `Menu`. If they're not, switch to the computer guide now!

```python
from random import *
from ti_draw import *
from ti_system import *
from time import *
```

## Step 2: Draw the player

First, add a blank line, then some basic information about the screen and game.

```python
WIDTH,HEIGHT=get_screen_dim()
TICKS=32
```

Next, add one more blank line, then the following lines to decide the player's position and size . Caps matter!

```python
PLAYER_X=WIDTH/10
player_y=HEIGHT/2
PLAYER_R=5
```

Finally, add one last blank line, then start an infinite loop that draws the player on the screen once every tick.

```python
game_over=False

while not game_over:
  sleep(1/TICKS)

  clear()
  fill_circle(PLAYER_X,player_y,PLAYER_R)
```

Hit `CTRL+R` to run the program. It'll draw the player forever. Once you're ready to stop, hold the `Home` button until the program ends.

## Step 3: Make the player fall

Before we can make the player fall, we need to explain what "falling" looks like. Add these lines just below `PLAYER_R=5`:

```python
player_v=0
MAX_V=HEIGHT*2/TICKS
GRAVITY=HEIGHT/2/TICKS
```
These will store how fast the player is moving, how fast they *can* move, and how fast they speed up.

Now that we know those things, we can actually make the following happen. Two lines below `sleep(1/TICKS)`, add the following:

```python
  player_v+=GRAVITY
  player_v=min(player_v,MAX_V)
  player_y+=player_v
  if player_y>HEIGHT:
    game_over=True
```

Make sure the indentation is right! There should be two diamonds before `player_v`, just like before `sleep`.

This will make the player fall. As a bonus, it'll end the game once you fall below the screen, so you won't have to hold `Home` anymore :)

Run the program again to see the physics play out. If something breaks, compare your code to this dropdown:

<details>
<summary>Step 3 code</summary>

```python
from random import *
from ti_draw import *
from ti_system import *
from time import *

WIDTH,HEIGHT=get_screen_dim()
TICKS=32

PLAYER_X=WIDTH/10
player_y=HEIGHT/2
PLAYER_R=5
player_v=0
MAX_V=HEIGHT*2/TICKS
GRAVITY=HEIGHT/2/TICKS

game_over=False

while not game_over:
  sleep(1/TICKS)

  player_v+=GRAVITY
  player_v=min(player_v,MAX_V)
  player_y+=player_v
  if player_y>HEIGHT:
    game_over=True

  clear()
  fill_circle(PLAYER_X,player_y,PLAYER_R)
```
</details>

## Step 4: Jump

So far, this is a video, not a game. To make it interactive, let's let the player jump. First, add this line below `GRAVITY=HEIGHT/2/TICKS` to set how fast the player jumps:

```python
JUMP_V=-HEIGHT*2/TICKS
```

See how it's negative? That's because on the calculator, "negative" means "up" and "positive" means "down" - which is also why gravity is positive!

Then, add the following lines above `player_v+=GRAVITY` to let the player push a button to jump.

```python
  if get_key():
    player_v=JUMP_V
  else:
```

Indent the next two lines. Together with what you just added, it should look like this:

```python
  if get_key():
    player_v=JUMP_V
  else:
    player_v+=GRAVITY
    player_v=min(player_v,MAX_V)
```

Altogether, this means "make the player jump if they hit a button, or fall if they didn't." Run the code to check if it works!

<details>
<summary>Step 4 code</summary>

```python
from random import *
from ti_draw import *
from ti_system import *
from time import *

WIDTH,HEIGHT=get_screen_dim()
TICKS=32

PLAYER_X=WIDTH/10
player_y=HEIGHT/2
PLAYER_R=5
player_v=0
MAX_V=HEIGHT*2/TICKS
GRAVITY=HEIGHT/2/TICKS
JUMP_V=-HEIGHT*2/TICKS

game_over=False

while not game_over:
  sleep(1/TICKS)

  if get_key():
    player_v=JUMP_V
  else:
    player_v+=GRAVITY
    player_v=min(player_v,MAX_V)
  player_y+=player_v
  if player_y>HEIGHT:
    game_over=True

  clear()
  fill_circle(PLAYER_X,player_y,PLAYER_R)
```
</details>

## Step 5: Moving wall

So far, the game is just a dot jumping endlessly. To make it more interesting, let's add a wall for the player to avoid. First, set what the wall should look like two lines below `JUMP_V=-HEIGHT*2/TICKS`:

```python
wall_x=WIDTH
wall_v=-WIDTH*2/TICKS
GAP_HEIGHT=HEIGHT//3
wall_gap=randint(0,HEIGHT-GAP_HEIGHT)
```

Next, make it move across the scene, moving all the way to the right if it reaches the end. Place these two lines below `game_over=True`, but delete two of the diamonds before you do so:

```python
  wall_x+=wall_v
  if wall_x<0:
    wall_x=WIDTH
    wall_gap=randint(0,HEIGHT-GAP_HEIGHT)
```

Finally, add these lines below `fill_circle(PLAYER_X,player_y,PLAYER_R)` to draw the top and bottom halves of the wall.

```
  draw_line(wall_x,0,wall_x,wall_gap)
  draw_line(wall_x,wall_gap+GAP_HEIGHT,wall_x,HEIGHT)
```

Run the code to see the wall move. Nothing will happen if you hit the wall quite yet - you'll have to imagine that you're losing in your mind.

<details>
<summary>Step 5 code</summary>

```python
from random import *
from ti_draw import *
from ti_system import *
from time import *

WIDTH,HEIGHT=get_screen_dim()
TICKS=32

PLAYER_X=WIDTH/10
player_y=HEIGHT/2
PLAYER_R=5
player_v=0
MAX_V=HEIGHT*2/TICKS
GRAVITY=HEIGHT/2/TICKS
JUMP_V=-HEIGHT*2/TICKS

wall_x=WIDTH
wall_v=-WIDTH*2/TICKS
GAP_HEIGHT=HEIGHT//3
wall_gap=randint(0,HEIGHT-GAP_HEIGHT)

game_over=False

while not game_over:
  sleep(1/TICKS)

  if get_key():
    player_v=JUMP_V
  else:
    player_v+=GRAVITY
    player_v=min(player_v,MAX_V)
  player_y+=player_v
  if player_y>HEIGHT:
    game_over=True

  wall_x+=wall_v
  if wall_x<0:
    wall_x=WIDTH
    wall_gap=randint(0,HEIGHT-GAP_HEIGHT)

  clear()
  fill_circle(PLAYER_X,player_y,PLAYER_R)
  draw_line(wall_x,0,wall_x,wall_gap)
  draw_line(wall_x,wall_gap+GAP_HEIGHT,wall_x,HEIGHT)
```
</details>

## Step 6: Let the player lose

Detecting a collision is a little harder than it might seem. It's not enough to check if the player and wall are in the same place - since the game runs on frames, it's possible for the wall to skip over the player without touching them. Instead, we'll need to compare the wall's position between two given frames. First, add the following line just above `wall_x+=wall_v` so the wall doesn't forget where it was:

```python
  old_wall_x = wall_x
```

Next, add the following code two lines below `wall_gap=randint(0,HEIGHT-GAP_HEIGHT)`. Make sure to delete two diamonds before doing so.

```python
  if wall_x<=PLAYER_X<=old_wall_x:
    if not wall_gap<=player_y<=wall_gap+GAP_HEIGHT:
      game_over = True
```

Run the code to test it.

<details>
<summary>Step 6 code</summary>

```python
from random import *
from ti_draw import *
from ti_system import *
from time import *

WIDTH,HEIGHT=get_screen_dim()
TICKS=32

PLAYER_X=WIDTH/10
player_y=HEIGHT/2
PLAYER_R=5
player_v=0
MAX_V=HEIGHT*2/TICKS
GRAVITY=HEIGHT/2/TICKS
JUMP_V=-HEIGHT*2/TICKS

wall_x=WIDTH
wall_v=-WIDTH*2/TICKS
GAP_HEIGHT=HEIGHT//3
wall_gap=randint(0,HEIGHT-GAP_HEIGHT)

game_over=False

while not game_over:
  sleep(1/TICKS)

  if get_key():
    player_v=JUMP_V
  else:
    player_v+=GRAVITY
    player_v=min(player_v,MAX_V)
  player_y+=player_v
  if player_y>HEIGHT:
    game_over=True

  old_wall_x = wall_x
  wall_x+=wall_v
  if wall_x<0:
    wall_x=WIDTH
    wall_gap=randint(0,HEIGHT-GAP_HEIGHT)

  if wall_x<=PLAYER_X<=old_wall_x:
    if not wall_gap<=player_y<=wall_gap+GAP_HEIGHT:
      game_over = True

  clear()
  fill_circle(PLAYER_X,player_y,PLAYER_R)
  draw_line(wall_x,0,wall_x,wall_gap)
  draw_line(wall_x,wall_gap+GAP_HEIGHT,wall_x,HEIGHT)
```
</details>

## Step 7: Score

This is a fully functional name! For some flavor, we can add a score. Start by telling the game how many points the player has and where to write their score two lines after `wall_gap=randint(0,HEIGHT-GAP_HEIGHT)`:

```python
score = 0
SCORE_X = WIDTH/2
SCORE_Y = HEIGHT/10
```

Now, give the player a point if they pass the wall without dying. Add these lines right after the second `game_over = True`, deleting two diamonds:

```python
    else:
      score += 1
```

Finally, draw the score for the player. Make this the last line of the program:

```python
  draw_text(SCORE_X,SCORE_Y,str(score))
```

That's it! Run the game to see the finished product.

<details>
<summary>Completed game!</summary>

```python
from random import *
from ti_draw import *
from ti_system import *
from time import *

WIDTH,HEIGHT=get_screen_dim()
TICKS=32

PLAYER_X=WIDTH/10
player_y=HEIGHT/2
PLAYER_R=5
player_v=0
MAX_V=HEIGHT*2/TICKS
GRAVITY=HEIGHT/2/TICKS
JUMP_V=-HEIGHT*2/TICKS

wall_x=WIDTH
wall_v=-WIDTH*2/TICKS
GAP_HEIGHT=HEIGHT//3
wall_gap=randint(0,HEIGHT-GAP_HEIGHT)

score=0
SCORE_X=WIDTH/2
SCORE_Y=HEIGHT/10

game_over=False

while not game_over:
  sleep(1/TICKS)

  if get_key():
    player_v=JUMP_V
  else:
    player_v+=GRAVITY
    player_v=min(player_v,MAX_V)
  player_y+=player_v
  if player_y>HEIGHT:
    game_over=True
  
  old_wall_x = wall_x
  wall_x+=wall_v
  if wall_x<0:
    wall_x=WIDTH
    wall_gap=randint(0,HEIGHT-GAP_HEIGHT)

  if wall_x<=PLAYER_X<=old_wall_x:
    if not wall_gap<=player_y<=wall_gap+GAP_HEIGHT:
      game_over = True
    else:
      score += 1

  clear()
  fill_circle(PLAYER_X,player_y,PLAYER_R)
  draw_line(wall_x,0,wall_x,wall_gap)
  draw_line(wall_x,wall_gap+GAP_HEIGHT,wall_x,HEIGHT)
  draw_text(SCORE_X,SCORE_Y,str(score))
```
</details>

## Steps 8+: Your choice!

Feel free to add as much or as little to this game as you want. Here are some suggestions to get you started:

- Tweak the game’s settings
- Add a game over screen
- Make the game get harder over time

There's also a tiny visual glitch that can happen if you lose by hitting the wall. Can you see it? If you can, can you fix it?
