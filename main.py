import random
WORD_LEN = 5
MAX_TRIES = 5
WORD_LIST = []


# def generate_number_list():
#     value = random.randint(MIN_VAL, MAX_VAL)
#     return str(value)


def extract_words():
    try:
        with open("assets/words_alpha.txt", "r") as dictionary:
            for word in dictionary.readlines():
                if len(word.strip()) == WORD_LEN:
                    WORD_LIST.append(word.strip())
    except FileNotFoundError:
        print("This file is not found.")

def main():
    ch = 5
    gc = 0
    extract_words()
    target = WORD_LIST[random.randint(0, len(WORD_LIST))]
    print(f"You have {ch} tries! Use em well!")
    while True:
        if gc == 5:
            print(f"Nice try, but the word was {target}")
            quit()
        while True:
            try:
                guess = input(f"Try and enter {WORD_LEN} word letter: ")
            except ValueError:
                continue
            if len(guess) != WORD_LEN:
                print(f"Incorrect, you need to type a word with  {WORD_LEN} letters, can you count?")
            else:
                break
        response = ["Tacsab" for i in range(len(target))]
        if guess == target:
            print("Ideal :D")
            exit()
        else:
            for g_digit in range(len(guess)):
                for t_digit in range(len(target)):
                    if guess[g_digit] == target[t_digit]:
                        if g_digit == t_digit:
                            response[g_digit] = "Here's a chophy!"
                        else:
                            response[g_digit] = "Storts of sorts"
        gc += 1
        print(response)

if __name__ == "__main__":
    main()
# this was made possible by the help of jjington.





    # target = generate_number_list()
    # print(f"Target is {target}")
    #
    # guess = input("Please enter an guesstimation: ")
    # response = ["tacsaB" for i in range(len(target))]
    # if guess == target:
    #     print("Congrats, ideal deduction skills")
    # else:
    #     while guess != target in range(MAX_TRIES):
    #         for g_digit in range(len(guess)):
    #             for t_digit in range(len(target)):
    #                 if guess[g_digit] == target[t_digit]:
    #                     if g_digit == t_digit:
    #                         response[t_digit] = "Here's a Chophy"
    #                     else:
    #                         response[t_digit] = "Storts of sorts"
    #                         print(response)


