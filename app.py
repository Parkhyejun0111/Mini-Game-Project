# app.py

from crocodile_game.crocodile_dentist_game import Crocodile
from blackjack.blackjack import BlackjackGame


class App:

    def __init__(self):

        # 악어게임 객체
        self.crocodile = Crocodile()

        # 블랙잭 객체
        self.blackjack = BlackjackGame(
            player_name="USER",
            starting_chips=100
        )

    def print_menu(self):

        print()
        print("=================================")
        print("🎮 MINI GAME MENU 🎮")
        print("=================================")
        print("1. 악어 이빨 게임")
        print("2. 블랙잭")
        print("3. 게임 종료")
        print("=================================")

    def input_menu(self):

        while True:

            try:
                menu = int(input("메뉴를 선택하세요: "))
                return menu

            except ValueError:
                print("숫자만 입력해주세요.")

    def run(self):

        while True:

            self.print_menu()

            menu = self.input_menu()

            # 악어게임
            if menu == 1:

                print("\n🐊 악어 게임 시작!\n")

                self.crocodile.crocodile_game()

            # 블랙잭
            elif menu == 2:

                print("\n🃏 블랙잭 시작!\n")

                self.blackjack.play()

            # 종료
            elif menu == 3:

                print("\n게임을 종료합니다.")
                break

            else:
                print("메뉴를 다시 선택해주세요.")