import random

def count_random_numbers(num_trials):
    # Initialize a dictionary to store counts for each number
    counts = {i: 0 for i in range(37)}

    # Perform the specified number of trials
    for _ in range(num_trials):
        # Generate a random number between 0 and 36 (inclusive)
        random_number = random.randint(0, 36)

        # Increment the count for the generated number
        counts[random_number] += 1

    # Calculate the total number of trials
    total_trials = num_trials

    # Print the counts as percentages for each number
    for number, count in counts.items():
        percentage = (count / total_trials) * 100
        print(f"Number {number}: {percentage:.2f}% occurrences")

# Set the number of trials to 1000
num_trials = 1000000

# Call the function with the specified number of trials
count_random_numbers(num_trials)
