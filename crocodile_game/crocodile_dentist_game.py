import random

history = []


def crocodile_game():

    teeth = list(range(1, 21))
    bomb = random.choice(teeth)

    used_teeth = []
    turn = "USER"

    while True:

        print("\n====================")
        print("Teeth left:")

        for tooth in teeth:
            if tooth not in used_teeth:
                print(tooth, end=" ")

        print("\n====================")

        # USER TURN
        if turn == "USER":

            try:
                choice = int(input("\nUSER turn - Pick a tooth: "))

            except ValueError:
                print("Enter a number.")
                continue

            if choice < 1 or choice > 20:
                print("It should be number of 1 ~ 20.")
                continue

            if choice in used_teeth:
                print("Already taken.")
                continue

            used_teeth.append(choice)

            if choice == bomb:
                print("\nSnap!!")
                print("Crocodile bit YOU!!")
                history.append("COMPUTER WIN")
                break

            turn = "COMPUTER"

        # COMPUTER TURN
        else:

            possible_choices = []

            for tooth in teeth:
                if tooth not in used_teeth:
                    possible_choices.append(tooth)

            computer_choice = random.choice(possible_choices)

            print(f"\nCOMPUTER chose {computer_choice} !")

            used_teeth.append(computer_choice)

            if computer_choice == bomb:
                print("\nSnap!!")
                print("Crocodile bit COMPUTER!!")
                history.append("USER WIN")
                break

            turn = "USER"


def game_history():

    print("\n===== GAME HISTORY =====")

    if len(history) == 0:
        print("None")

    else:
        for result in history:
            print("-", result)