from crocodile_game.crocodile_dentist_game import CrocodileDentistGame
from blackjack.blackjack_game import BlackJackGame


class App:

    def print_menu(self):

        print()
        print("🎪 DEVIL CASINO 🎪")
        print("1. 악어이빨게임")
        print("2. 블랙잭")
        print("3. 게임 종료")


    def input_menu(self):

        while True:

            try:
                menu = int(input("메뉴 선택 : "))
                return menu

            except ValueError:
                print("숫자만 입력해주세요.")


    def run(self):

        while True:

            self.print_menu()

            menu = self.input_menu()

            if menu == 1:

                game = CrocodileDentistGame()
                game.play()

            elif menu == 2:

                game = BlackJackGame()
                game.play()

            elif menu == 3:

                print("게임 종료")
                break

            else:
                print("다시 입력해주세요.")