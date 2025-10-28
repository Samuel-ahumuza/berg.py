
import random
import time
import sys

def generate_memorable_password():
    # A list of diverse, easily-remembered words
    word_list = [
        "guitar", "rocket", "purple", "octopus", "cloud",
        "zebra", "mountain", "coffee", "whisper", "jungle",
        "diamond", "velvet", "puzzle", "soccer", "pirate"
    ]

    # --- Part 1: Select Random Components ---
    # Use random.sample to pick 4 unique words from the list
    random_words = random.sample(word_list, 4)

    # Choose a random number and a random special character
    random_number = random.randint(10, 99)
    special_chars = ['!', '@', '#', '$', '%', '&']
    random_symbol = random.choice(special_chars)

    # --- Part 2: Assemble the Password ---
    
    # Capitalize the first letter of each word and join them with the symbol
    # Example: Guitar-Rocket-Purple-Octopus
    word_part = "-".join([word.capitalize() for word in random_words])
    
    # Combine everything to form the final strong password
    final_password = f"{word_part}{random_symbol}{random_number}"

    # --- Part 3: Output the Result ---
    print("Generating a strong, memorable password...")
    time.sleep(1.5)

    print("--- NEW PASSWORD ---")
    time.sleep(0.5)

    # Use the typing effect for the reveal
    for char in final_password:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    
    print(f"\n\nLength: {len(final_password)} characters.")
    print("\Hint: Remember the four words, the symbol, and the number!)")

# Execute the function
if __name__ == "__main__":
    generate_memorable_password()