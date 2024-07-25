import random

def get_words():
    return [
        "python", "developer", "programming", "puzzle", "challenge",
        "algorithm", "function", "variable", "syntax", "compiler",
        "interpreter", "framework", "library", "module", "package",
        "recursion", "iteration", "data", "structure", "abstract"
    ]

def shuffle_word(word):
    word = list(word)
    random.shuffle(word)
    return ''.join(word)

def play_game():
    words = get_words()
    score = 0
    
    print("Welcome to WordWhiz Quest!")
    print("Solve the word puzzles. You get +1 point for each correct answer. The game ends when you give a wrong answer.")
    print("Let's begin!\n")
    
    while True:
        word = random.choice(words)
        shuffled_word = shuffle_word(word)
        print(f"Solve this puzzle: {shuffled_word}")
        user_answer = input("Your answer: ").strip().lower()
        
        if user_answer == word:
            score += 1
            print("Correct! Your score is now", score, "\n")
        else:
            print(f"Wrong! The correct word was {word}.")
            print(f"Game over! Your final score is: {score}")
            break

if __name__ == "__main__":
    play_game()
