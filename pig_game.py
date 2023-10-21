
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_score(self, turn_score):
        self.score += turn_score

    def __str__(self):
        return f"Player: {self.name}, Score: {self.score}"


class Die:
    def __init__(self, sides=6):
        self.sides = sides
        random.seed(0)
    
    def roll(self):
        return random.randint(1, self.sides)


class Game:
    def __init__(self, players):
        self.players = players
        self.die = Die()
        self.current_player_index = 0

    def switch_player(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def play_turn(self):
        current_player = self.players[self.current_player_index]
        turn_score = 0
        
        while True:
            decision = input(f"{current_player.name}, do you want to roll or hold? (r/h): ").strip().lower()
            if decision == 'r':
                roll = self.die.roll()
                if roll == 1:
                    print(f"Sorry, {current_player.name}, you rolled a 1. No points for this turn.")
                    turn_score = 0
                    break
                else:
                    turn_score += roll
                    print(f"{current_player.name}, you rolled a {roll}. Turn score: {turn_score}, Total score: {current_player.score + turn_score}")
            elif decision == 'h':
                break
            else:
                print("Invalid input. Please enter 'r' to roll or 'h' to hold.")
        
        current_player.add_score(turn_score)
        self.switch_player()

    def check_winner(self):
        for player in self.players:
            if player.score >= 100:
                return player
        return None


def play_game(num_players=2):
    while True:
        players = [Player(f"Player {i+1}") for i in range(num_players)]
        game = Game(players)
        
        while True:
            game.play_turn()
            winner = game.check_winner()
            if winner:
                print(f"Congratulations, {winner.name}! You won with a score of {winner.score}.")
                break
        
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            break


if __name__ == "__main__":
    play_game()
