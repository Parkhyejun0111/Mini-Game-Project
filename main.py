from blackjack.blackjack_game import BlackJackGame
from slot_machine.slot_machine_game import SlotMachineGame


class App:

    def run(self):

        while True:

            print()
            print("🎪 DEVIL CASINO 🎪")
            print("1. 블랙잭")
            print("2. 슬롯머신")
            print("3. 게임 종료")

            menu = input("메뉴 선택 : ")

            if menu == "1":
                game = BlackJackGame()
                game.play()

            elif menu == "2":
                game = SlotMachineGame()
                game.play()

            elif menu == "3":
                print("게임 종료")
                break

            else:
                print("다시 입력해주세요.")