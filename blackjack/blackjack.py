import random

try:
    from .config import DEALER_STAND_SCORE, RANKS, RESHUFFLE_CARD_LIMIT, SUITS, SUIT_SYMBOLS
except ImportError:
    from config import DEALER_STAND_SCORE, RANKS, RESHUFFLE_CARD_LIMIT, SUITS, SUIT_SYMBOLS


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def value(self):
        if self.rank == "A":
            return 11
        if self.rank in ("J", "Q", "K"):
            return 10
        return int(self.rank)

    def __str__(self):
        return f"{self.rank}{SUIT_SYMBOLS[self.suit]}"


class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in SUITS for rank in RANKS]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        if not self.cards:
            self.__init__()
        return self.cards.pop()


class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def clear(self):
        self.cards.clear()

    def score(self):
        total = sum(card.value() for card in self.cards)
        ace_count = sum(1 for card in self.cards if card.rank == "A")

        while total > 21 and ace_count > 0:
            total -= 10
            ace_count -= 1

        return total

    def is_blackjack(self):
        return len(self.cards) == 2 and self.score() == 21

    def is_bust(self):
        return self.score() > 21

    def show(self, hide_first=False):
        if hide_first and self.cards:
            visible_cards = ["??"] + [str(card) for card in self.cards[1:]]
            return " ".join(visible_cards)
        return " ".join(str(card) for card in self.cards)


class Participant:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()

    def reset_hand(self):
        self.hand.clear()

    def take_card(self, deck):
        self.hand.add_card(deck.draw())


class BlackjackGame:
    def __init__(self, player_name, starting_chips):
        self.deck = Deck()
        self.player = Participant(player_name)
        self.dealer = Participant("딜러")
        self.chips = starting_chips
        self.rounds_played = 0
        self.wins = 0
        self.losses = 0
        self.draws = 0

    def play(self):
        self.print_title()

        while self.chips > 0:
            print(f"\n현재 칩: {self.chips}")
            if not self.ask_yes_no("블랙잭 한 판을 시작할까요? (y/n): "):
                break

            bet = self.ask_bet()
            result = self.play_round()
            self.apply_result(result, bet)

        print("\n블랙잭 게임을 종료합니다.")
        print(f"진행한 판: {self.rounds_played}, 승리: {self.wins}, 패배: {self.losses}, 무승부: {self.draws}")
        print(f"최종 칩: {self.chips}")
        return self.result()

    def result(self):
        return {
            "game": "blackjack",
            "rounds": self.rounds_played,
            "wins": self.wins,
            "losses": self.losses,
            "draws": self.draws,
            "chips": self.chips,
        }

    def print_title(self):
        print("=" * 35)
        print(" 블랙잭")
        print("=" * 35)
        print("딜러보다 21에 더 가까우면 승리합니다.")
        print("A는 1 또는 11, J/Q/K는 10으로 계산합니다.")

    def play_round(self):
        self.rounds_played += 1
        self.prepare_round()
        self.deal_initial_cards()
        self.show_table(hide_dealer=True)

        if self.player.hand.is_blackjack() or self.dealer.hand.is_blackjack():
            return self.decide_blackjack_result()

        if not self.player_turn():
            return "lose"

        self.dealer_turn()
        return self.compare_scores()

    def prepare_round(self):
        if len(self.deck.cards) < RESHUFFLE_CARD_LIMIT:
            self.deck = Deck()
        self.player.reset_hand()
        self.dealer.reset_hand()

    def deal_initial_cards(self):
        for _ in range(2):
            self.player.take_card(self.deck)
            self.dealer.take_card(self.deck)

    def player_turn(self):
        while True:
            if self.player.hand.is_bust():
                self.show_table(hide_dealer=False)
                print("21점을 초과했습니다. 패배입니다.")
                return False

            choice = input("카드를 더 받으려면 h, 멈추려면 s를 입력하세요 (h/s): ").strip().lower()
            if choice in ("h", "hit", "히트", "더받기", "받기"):
                self.player.take_card(self.deck)
                self.show_table(hide_dealer=True)
            elif choice in ("s", "stand", "스탠드", "멈춤", "멈추기"):
                return True
            else:
                print("h 또는 s를 입력해주세요.")

    def dealer_turn(self):
        print("\n딜러 차례입니다.")
        self.show_table(hide_dealer=False)

        while self.dealer.hand.score() < DEALER_STAND_SCORE:
            print("딜러가 카드를 한 장 더 받습니다.")
            self.dealer.take_card(self.deck)
            self.show_table(hide_dealer=False)

        if self.dealer.hand.is_bust():
            print("딜러가 21점을 초과했습니다.")
        else:
            print("딜러가 멈춥니다.")

    def compare_scores(self):
        player_score = self.player.hand.score()
        dealer_score = self.dealer.hand.score()

        if self.dealer.hand.is_bust():
            return "win"
        if player_score > dealer_score:
            return "win"
        if player_score < dealer_score:
            return "lose"
        return "draw"

    def decide_blackjack_result(self):
        self.show_table(hide_dealer=False)
        player_blackjack = self.player.hand.is_blackjack()
        dealer_blackjack = self.dealer.hand.is_blackjack()

        if player_blackjack and dealer_blackjack:
            print("플레이어와 딜러 모두 블랙잭입니다.")
            return "draw"
        if player_blackjack:
            print("블랙잭! 승리했습니다.")
            return "blackjack"
        print("딜러가 블랙잭입니다.")
        return "lose"

    def apply_result(self, result, bet):
        if result == "blackjack":
            reward = int(bet * 1.5)
            self.chips += reward
            self.wins += 1
            print(f"{reward}칩을 얻었습니다.")
        elif result == "win":
            self.chips += bet
            self.wins += 1
            print(f"{bet}칩을 얻었습니다.")
        elif result == "lose":
            self.chips -= bet
            self.losses += 1
            print(f"{bet}칩을 잃었습니다.")
        else:
            self.draws += 1
            print("무승부입니다. 베팅한 칩은 그대로 유지됩니다.")

    def show_table(self, hide_dealer):
        dealer_score = "?" if hide_dealer else self.dealer.hand.score()
        print("\n" + "-" * 35)
        print(f"딜러: {self.dealer.hand.show(hide_first=hide_dealer)}  점수: {dealer_score}")
        print(f"{self.player.name}: {self.player.hand.show()}  점수: {self.player.hand.score()}")
        print("-" * 35)

    def ask_bet(self):
        while True:
            raw_bet = input(f"베팅할 칩을 입력하세요 (1-{self.chips}): ").strip()
            if raw_bet.isdigit():
                bet = int(raw_bet)
                if 1 <= bet <= self.chips:
                    return bet
            print("올바른 베팅 금액을 입력해주세요.")

    def ask_yes_no(self, message):
        while True:
            answer = input(message).strip().lower()
            if answer in ("y", "yes", "예", "네", "ㅇ"):
                return True
            if answer in ("n", "no", "아니오", "아니요", "ㄴ"):
                return False
            print("y 또는 n을 입력해주세요.")
