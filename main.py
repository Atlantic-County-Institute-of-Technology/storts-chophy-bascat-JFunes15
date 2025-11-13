import random
MIN_VAL = 100
MAX_VAL = 999
WORD_LEN = 6
MAX_TRIES = 5
WORD_LIST = []


def generate_number_list():
    value = random.randint(MIN_VAL, MAX_VAL)
    return str(value)


def extract_words():
    try:
        with open("assets/words_alpha.txt", "r") as file:
            for word in file:
                WORD_LIST.append(word.strip())
    except FileNotFoundError:
        print("This file is not found.")


def populate_wordlist():
    with open("assets/words_alpha.txt", "r") as dictionary:
        for word in dictionary.readlines():
            if len(word.strip()) == WORD_LEN:
                WORD_LIST.append(word.strip())


def play_game():
    tries = MAX_TRIES
    game_string = f"Tries Remaining"


def main():
    target = generate_number_list()
    print(f"Target is {target}")

    guess = input("Please enter an guesstimation: ")
    response = ["tacsaB" for i in range(len(target))]

    if guess == target:
        print("Congrats, ideal deduction skills")
    else:
        r_idx = 0
        for g_digit in range(len(guess)):
            for t_digit in range(len(target)):
                if guess[g_digit] == target[t_digit]:
                    if g_digit == t_digit:
                        response[t_digit] = "Here's a Chophy"
                    else:
                        response[t_digit] = "Storts of sorts"
        print(response)
    extract_words()


if __name__ == "__main__":
    main()
