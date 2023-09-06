from itertools import product

# Define the number of dice rolls and the number of sides on each die
num_rolls = 3
num_sides = 6

# Generate all possible outcomes of rolling the dice
outcomes = list(product(range(1, num_sides + 1), repeat=num_rolls))

# Initialize a dictionary to store the counts of each sum
sum_counts = {}

# Calculate the sum of each outcome and count the occurrences
for outcome in outcomes:
    total_sum = sum(outcome)
    if total_sum in sum_counts:
        sum_counts[total_sum] += 1
    else:
        sum_counts[total_sum] = 1

# Calculate the total number of possible outcomes
total_outcomes = num_sides ** num_rolls

# Calculate the probability distribution for Y
probability_distribution = {sum_value: count / total_outcomes for sum_value, count in sum_counts.items()}

# Print the probability distribution
for sum_value, probability in sorted(probability_distribution.items()):
    print(f'Sum = {sum_value}: Probability = {probability:.4f}')
