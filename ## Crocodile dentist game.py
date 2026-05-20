## Crocodile dentist game


## Crocodile Game

import random
import sys

USER_ID = "admin"
USER_PW = "1234"


def login():
    for i in range(3):
        user_id = input("Enter ID: ")
        user_pw = input("Enter PASSWORD: ")

        if user_id == USER_ID and user_pw == USER_PW:
            print(f"\n{user_id} logged in.\n")
            return True
        else:
            print(f"Unable to log in ({i+1}/3)")

    print("Access denied.")
    sys.exit()


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


def menu():

    while True:

        print("\n1. 게임 시작")
        print("2. 기록 보기")
        print("3. 게임 종료")

        choice = input("메뉴를 선택하세요: ")

        if choice == "1":
            crocodile_game()

        elif choice == "2":
            game_history()

        elif choice == "3":
            print("게임 종료합니다.")
            break

        else:
            print("메뉴를 다시 선택하세요.")


login()
menu()