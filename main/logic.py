import random
from string import ascii_letters, digits


def generate_key(size=50):
    """Function generates and return DJANGO SECRET KEY."""
    return ''.join(random.SystemRandom().choice(ascii_letters+digits+('!@#$%^&*()_+-=')) for _ in range(size))
