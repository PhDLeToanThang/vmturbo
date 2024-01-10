import random

def generate_numbers():
    numbers = random.sample(range(1, 46), 6)
    numbers.sort()
    return numbers

results = []

for _ in range(8000000):
    results.append(generate_numbers())