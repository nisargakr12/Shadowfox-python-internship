import random

hangman_stages = [
    """
      +---+
          |
          |
          |
         ===""",
    """
      +---+
      O   |
          |
          |
         ===""",
    """
      +---+
      O   |
      |   |
          |
         ===""",
    """
      +---+
      O   |
     /|   |
          |
         ===""",
    """
      +---+
      O   |
     /|\\  |
          |
         ===""",
    """
      +---+
      O   |
     /|\\  |
     /    |
         ===""",
    """
      +---+
      O   |
     /|\\  |
     / \\  |
         ==="""
]

word_list = [
    ("python", "A popular programming language."),
    ("giraffe", "Tall animal found in Africa."),
    ("hangman", "A classic word guessing game."),
    ("keyboard", "An input device with keys."),
    ("pizza", "A popular Italian dish."),
    ("astronaut", "A person trained to travel in space."),
    ("bicycle", "A two-wheeled vehicle powered by pedals."),
    ("elephant", "The largest land animal."),
    ("internet", "A global network connecting computers."),
    ("volcano", "A mountain that can erupt with lava."),
    ("rainbow", "A colorful arc that appears after rain."),
    ("library", "A place where books are kept."),
    ("mountain", "A large natural elevation of the earth's surface."),
    ("penguin", "A bird that cannot fly but swims very well."),
    ("calendar", "It helps you track days and months."),
    ("diamond", "A precious gemstone."),
    ("football", "A popular sport played with a round ball."),
    ("galaxy", "A huge system of stars, planets, and dust."),
    ("hurricane", "A powerful tropical storm."),
    ("island", "Land surrounded by water."),
    ("jungle", "A dense forest."),
    ("kangaroo", "A marsupial from Australia."),
    ("lighthouse", "A tower with a bright light to guide ships."),
    ("microscope", "An instrument to see tiny things."),
    ("notebook", "Used for writing notes."),
    ("octopus", "Sea creature with eight arms."),
    ("pyramid", "Famous ancient Egyptian structure."),
    ("quarantine", "Period of isolation to prevent disease spread."),
    ("robotics", "Technology involving robots."),
    ("saxophone", "A musical instrument."),
    ("telescope", "Used to see distant objects."),
    ("unicorn", "Mythical horse with a horn."),
    ("volleyball", "Sport played with a ball over a net."),
    ("waterfall", "Water flowing over a cliff."),
    ("xylophone", "A musical instrument with wooden bars."),
    ("yacht", "A luxury boat."),
    ("zeppelin", "A type of airship.")
]

max_tries = len(hangman_stages) - 1

def play_round(total_score):
    word, hint = random.choice(word_list)
    guessed_letters = []
    tries = 0
    score = 0

    print("\n🎮 New Round Started!")
    print(f"💡 Hint: {hint}")

    while tries < max_tries:
        display_word = [letter if letter in guessed_letters else "_" for letter in word]
        print("\nWord: ", " ".join(display_word))
        print(f"🔢 Current Round Score: {score}")
        print(f"🎯 Total Score: {total_score}")

        guess = input("🔤 Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("❌ Please enter a single alphabetical character.")
            continue

        if guess in guessed_letters:
            print("⚠️ You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Good guess!")
            score += 10
        else:
            print("❌ Incorrect!")
            score -= 5
            tries += 1

        print(hangman_stages[tries])

        if all(letter in guessed_letters for letter in word):
            score += 50  # Bonus for winning
            total_score += score
            print(f"\n🎉 You guessed the word: {word}")
            print(f"🏆 Round Score: {score}")
            print(f"🏅 Total Score: {total_score}")
            return total_score

    # If here, player lost this round
    print(hangman_stages[-1])
    print(f"\n💀 Game Over! The word was: {word}")
    total_score += score
    print(f"🏆 Round Score: {score}")
    print(f"🏅 Total Score: {total_score}")
    return total_score


def main():
    total_score = 0
    print("Welcome to Multi-Round Hangman! The game will continue automatically.\n")
    try:
        while True:
            total_score = play_round(total_score)
            print("\nStarting next round...\n")
    except KeyboardInterrupt:
        print(f"\n\nThanks for playing! Your final total score: {total_score}")
        print("Goodbye!")


if __name__ == "__main__":
    main()
