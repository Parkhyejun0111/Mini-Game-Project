import sys

from config import USER_ID, USER_PW
from crocodile_dentist_game import crocodile_game, game_history


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