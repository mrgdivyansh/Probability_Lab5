import random

pmf = [(0, 0.25), (1, 0.5), (2, 0.125), (3, 0.125)]

cdf = []
cumulative_prob = 0.0
for value, probability in pmf:
    cumulative_prob += probability
    cdf.append((value, cumulative_prob))

def generate_random_sample():
    random_number = random.uniform(0, 1)
    for value, cumulative_probability in cdf:
        if random_number <= cumulative_probability:
            return value

random_numbers = [generate_random_sample() for _ in range(1500)]

print(random_numbers[:10])

value_counts = {value: random_numbers.count(value) for value in set(random_numbers)}
for value, count in sorted(value_counts.items()):
    print(f"Value {value}: Count {count}")

