import random

sample_set = ['Heads', 'Tails']


def get_res():
    return random.choice(sample_set)


print("\n\n" + get_res() + "\n\n")
