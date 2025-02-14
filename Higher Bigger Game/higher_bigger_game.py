import random
import game_data
import art

score = 0


def random_pick(database):
    """Returns two random different elements from the database without modifying it."""
    return random.sample(database, 2)


def compare(person1, person2):
    """Compares follower counts and returns the winner or 'wrong' if the user guesses incorrectly."""
    print(f'Compare A: {person1["name"]}, a {person1["description"]}, from {person1["country"]}.')
    print(f"{art.vs}")
    print(f'Against B: {person2["name"]}, a {person2["description"]}, from {person2["country"]}.')

    choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    if choice == 'A' and person1['follower_count'] > person2['follower_count']:
        return person1
    elif choice == 'B' and person2['follower_count'] > person1['follower_count']:
        return person2
    else:
        return 'wrong'


# Pick the first two random people
person1, person2 = random_pick(game_data.data)
print(f"\n" * 30)
print(art.logo)
while True:
    winner = compare(person1, person2)

    if winner == 'wrong':
        print(f"\n" * 30)
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        break  # End the game

    score += 1
    print(f"\n" * 30)
    print(art.logo)
    print(f"You're right! Current score: {score}.")

    # Get a new random person to compare with the winner
    person1 = winner
    person2 = random.choice(game_data.data)  # Get a new competitor
