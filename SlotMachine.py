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
            win = self.score[result[0]]
            return "JACKPOT", win

        elif result[0] == result[1] or result[0] == result[2] or result[1] == result[2]:
            return "BONUS", 15

        else:
            return "FAIL", 50

    def play(self, nickname):
        self.coins = self.start_coins

        print(f"\n🎰 {nickname}님의 슬롯게임을 시작합니다!")

        while self.coins > 0:
            print(f"\n현재 코인: {self.coins}")
            input("엔터를 누르면 슬롯을 돌립니다.")

            result = self.spin()
            print(" ".join(result))

            result_type, win = self.check_result(result)

            if result_type == "JACKPOT":
                self.coins += win
                print(f"JACKPOT! {win}코인 획득")

            elif result_type == "BONUS":
                self.coins += win
                print(f"BONUS! {win}코인 획득")

            else:
                self.coins -= win
                print(f"FAIL! {win}코인 차감")

            print(f"남은 코인: {self.coins}")

        print("\n코인이 모두 소진되어 슬롯게임을 종료합니다.")
        print(f"{nickname}님의 최종 코인: {self.coins}")

        while True:
            restart = input("\n다시 시작하시겠습니까? (yes/no): ").lower()

            if restart == "yes":
                print("\n코인을 30으로 리셋합니다!")
                return self.play(nickname)

            elif restart == "no":
                print("게임을 종료합니다.")
                return self.coins

            else:
                print("yes 또는 no만 입력해주세요.")


if __name__ == "__main__": #test용
    game = SlotMachine()
    nickname = input("닉네임을 입력하세요: ")
    game.play(nickname)





