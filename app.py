from blackjack.app import run_blackjack
from crocodile_game.crocodile_dentist_game import Crocodile
from slotmachine.SlotMachine import SlotMachine


class App:
    def __init__(self):
        self.crocodile = Crocodile()
        self.slotmachine = SlotMachine()

    def print_menu(self):
        print()
        print("=================================")
        print(" 🎪🎪🎪 MINI GAME MENU 🎪🎪🎪")
        print("=================================")
        print("1. 악어 이빨 게임")
        print("2. 블랙잭")
        print("3. 슬롯 머신")
        print("4. 게임 종료")
        print("=================================")

    def input_menu(self):
        while True:
            try:
                return int(input("메뉴를 선택하세요: "))
            except ValueError:
                print("숫자만 입력해주세요.")

    def run(self):
        while True:
            self.print_menu()
            menu = self.input_menu()

            if menu == 1:
                print("\n악어 이빨 게임을 시작합니다.\n")
                self.crocodile.crocodile_game()
            elif menu == 2:
                print("\n블랙잭을 시작합니다.\n")
                run_blackjack()
            elif menu == 3:
                print("\n슬롯 머신을 시작합니다.\n")
                self.slotmachine.play()
            elif menu == 4:
                print("\n게임을 종료합니다.")
                break
            else:
                print("메뉴를 다시 선택해주세요.")
