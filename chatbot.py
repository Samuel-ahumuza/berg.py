import time

def run_chatbot():
    # --- Part 1: Gather Information ---
    print("Welcome to the Destiny Predictor Bot! I just need a few details...")
    time.sleep(1)

    name = input("1. Enter your secret agent codename: ")
    color = input("2. What is your favorite color? ")
    pet = input("3. What's a funny, weird animal (e.g., penguin, sloth, tapir, panda)? ")

    # --- Part 2: Generate Fortune ---
    print("\nCalculating your destiny...")
    time.sleep(2)
    print("...37% complete...")
    time.sleep(1.5)
    print("...99% complete...\n")
    time.sleep(0.5)

    # Use f-strings to combine the user's input with a witty response
    if color.lower() == "red":
        fortune = f"Agent {name}, your future is a blaze of glory! You will be famous for inventing a perpetually-squeezing machine powered by a tiny {pet}."
    elif color.lower() == "blue":
        fortune = f"Agent {name}, your life path is cool and mysterious. You will eventually live on a remote island and train a highly-intelligent {pet} to fetch you snacks."
    else:
        fortune = f"Agent {name}, your destiny is totally unique, just like your color choice! You will open a chain of boutique stores that exclusively sells tiny hats for {pet}s."

    # --- Part 3: Output Result ---
    # The output is printed slowly to be more visually engaging for a video
    print("--- DESTINY REVEALED ---")
    time.sleep(0.5)
    for char in fortune:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04) # Slightly faster typing speed
    print("\n\n(Thank you for your data. Good luck.)")

# Execute the function
if __name__ == "__main__":
    # Import sys here if you want to use the typing effect
    try:
        import sys
    except ImportError:
        # Fallback if sys somehow isn't available
        pass
    
    run_chatbot()
