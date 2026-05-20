""" from crocodile_game.app import App as CrocodileApp
from slot_machine.app import App as SlotApp
from blackjack.app import App as BlackjackApp


while True:

    print("1. 악어이빨")
    print("2. 슬롯머신")
    print("3. 블랙잭")

    choice = input("선택 : ")

    if choice == "1":
        app = CrocodileApp()
        app.run()

    elif choice == "2":
        app = SlotApp()
        app.run()

    elif choice == "3":
        app = BlackjackApp()
        app.run() """