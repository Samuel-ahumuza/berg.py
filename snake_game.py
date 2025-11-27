# --- Python Snake Game ---
# This game uses the built-in 'turtle' module for graphics and 'time' for delays.
# The 'turtle' module is an easy-to-use way to introduce simple graphics in Python.

import turtle
import time
import random

# Global score variable
score = 0
high_score = 0

# --- 1. Setup the Screen ---
# The screen object is the window where the game takes place.
wn = turtle.Screen()
wn.setup(width=600, height=600) # Standard game window size
wn.bgcolor("dark green")
wn.title("Python Snake Game")
wn.tracer(0) # Turns off screen updates, must be manually updated for smooth animation

# --- 2. Create the Snake Head ---
# The snake head is a square turtle object.
head = turtle.Turtle()
head.speed(0) # Animation speed (0 is fastest)
head.shape("square")
head.color("white")
head.penup() # Prevents drawing lines as it moves
head.goto(0, 0)
head.direction = "stop" # Initial direction

# --- 3. Create the Food ---
# The food will appear randomly on the screen.
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100) # Start food at a random initial position

# --- 4. Scoreboard Pen ---
# This turtle object is used purely to write text (the score) on the screen.
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# List to hold the snake segments (body)
segments = []

# --- 5. Game Functions ---

def go_up():
    """Sets the snake's direction to 'up', preventing reversal (down)."""
    if head.direction != "down":
        head.direction = "up"

def go_down():
    """Sets the snake's direction to 'down', preventing reversal (up)."""
    if head.direction != "up":
        head.direction = "down"

def go_left():
    """Sets the snake's direction to 'left', preventing reversal (right)."""
    if head.direction != "right":
        head.direction = "left"

def go_right():
    """Sets the snake's direction to 'right', preventing reversal (left)."""
    if head.direction != "left":
        head.direction = "right"

def move():
    """Moves the snake head based on its current direction."""
    if head.direction == "up":
        y = head.ycor() # Get current Y coordinate
        head.sety(y + 20) # Move up 20 pixels (one segment size)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20) # Move down 20 pixels

    if head.direction == "left":
        x = head.xcor() # Get current X coordinate
        head.setx(x - 20) # Move left 20 pixels

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20) # Move right 20 pixels

def update_score(current_score, highscore):
    """Clears and rewrites the scoreboard with the current score and high score."""
    pen.clear()
    pen.write(f"Score: {current_score}  High Score: {highscore}",
              align="center", font=("Courier", 24, "normal"))

def reset_game():
    """Resets the game state after a collision."""
    global score, high_score
    
    # Pause for a brief moment
    time.sleep(1) 
    
    # Hide all segments and clear the list
    for segment in segments:
        segment.goto(1000, 1000) # Move segments off-screen
    segments.clear()
    
    # Move head back to center and stop movement
    head.goto(0, 0)
    head.direction = "stop"
    
    # Reset the score
    score = 0
    # Update high score if necessary is handled in the main loop, but we ensure it's written now.
    update_score(score, high_score)
    

# --- 6. Keyboard Bindings ---
# Listen for keyboard input and map keys to direction functions.
wn.listen()
wn.onkey(go_up, "Up")
wn.onkey(go_down, "Down")
wn.onkey(go_left, "Left")
wn.onkey(go_right, "Right")
# Also map WASD for alternative controls
wn.onkey(go_up, "w")
wn.onkey(go_down, "s")
wn.onkey(go_left, "a")
wn.onkey(go_right, "d")


# --- 7. Main Game Loop ---
while True:
    # Update the screen once per loop iteration
    wn.update()

    # A. Check for Border Collision
    # If the snake hits the edge (300px on either side), reset the game.
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        reset_game()

    # B. Check for Food Collision
    # The distance method checks the distance between two turtles.
    if head.distance(food) < 20:
        # Move food to a new random location
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        # Add a new segment to the snake body
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Increase the score
        score += 10

        # Check for new high score
        if score > high_score:
            high_score = score

        # Update the scoreboard
        update_score(score, high_score)

    # C. Move the End Segments First (Body Movement Logic)
    # The last segment moves to where the second-to-last segment was, and so on.
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 (the first segment) to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    # D. Move the Head
    move()

    # E. Check for Body Collision (Head vs. Segments)
    # Check if the head's position matches any segment's position.
    for segment in segments:
        if segment.distance(head) < 20:
            reset_game()

    # Set game speed (determines how fast the main loop runs)
    # Lower sleep time = faster game
    time.sleep(0.1)

# Keep the window open (in case of running outside a full IDE)
# wn.mainloop() # This is generally not needed in modern environments but included for completeness.