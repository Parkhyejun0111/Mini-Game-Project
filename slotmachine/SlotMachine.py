import random


class SlotMachine:

    def __init__(self):

        self.symbols = ["🍀", "⭐", "💎"]

        self.score = {
            "🍀": 20,
            "⭐": 30,
            "💎": 50
        }

        self.start_coins = 30
        self.coins = self.start_coins

    def spin(self):

        return random.choices(self.symbols, k=3)

    def check_result(self, result):

        if result[0] == result[1] == result[2]:

            coin_count = self.score[result[0]]

            return "JACKPOT", coin_count

        elif (
            result[0] == result[1]
            or result[0] == result[2]
            or result[1] == result[2]
        ):

            return "BONUS", 15

        else:

            return "FAIL", 50

    def restart(self):
        while True:
            restart = input("\n계속할까요? (yes/no): ").lower()
            if restart == "yes":
                return True
            elif restart == "no":
                print("게임을 종료합니다.")
                return False
            else:
                print("yes 또는 no만 입력해주세요.")

    def play(self):

        self.coins = self.start_coins

        print(f"\n🎰 슬롯게임을 시작합니다!")
        while self.coins > 0:
            print(f"\n현재 코인: {self.coins}")
            input("엔터를 누르면 슬롯을 돌립니다.")
            result = self.spin()
            print(" ".join(result))

            result_type, coin_count = self.check_result(result)

            if result_type == "JACKPOT":
                self.coins += coin_count
                print(f"JACKPOT! {coin_count}코인 획득")

            elif result_type == "BONUS":
                self.coins += coin_count
                print(f"BONUS! {coin_count}코인 획득")

            else:
                self.coins -= coin_count
                print(f"FAIL! {coin_count}코인 차감")

            print(f"남은 코인: {self.coins}")
            if self.coins <= 0:
                print("\n코인이 모두 소진되었습니다.")
                print("게임을 종료합니다.")
                break

        print(f"\n최종 코인: {self.coins}")

        return self.coins
        
        
        

