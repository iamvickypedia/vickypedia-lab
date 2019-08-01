import random

sample_set = ['Heads', 'Tails']


def get_res():
    return random.choice(sample_set)


input("Welcome to the Coin Toss Program.\nPress ENTER to toss the coin and see the result")

print("\n\n" + get_res() + "\n\n")
