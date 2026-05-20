try:
    from .blackjack import BlackjackGame
    from .config import STARTING_CHIPS
except ImportError:
    from blackjack import BlackjackGame
    from config import STARTING_CHIPS


def run_blackjack(player_name="플레이어"):
    game = BlackjackGame(player_name=player_name, starting_chips=STARTING_CHIPS)
    return game.play()


def main():
    return run_blackjack()


if __name__ == "__main__":
    main()
