import random
import time

def generate_random_binary(length):
    binary = ''.join(random.choice('01') for _ in range(length))
    return binary

def print_random_binary(length, num_samples, delay):
    for _ in range(num_samples):
        binary = generate_random_binary(length)
        print(binary)
        time.sleep(delay)

# Set the desired length of each binary number
binary_length = 500

# Set the number of random binary numbers to generate and print
num_samples = 500000

# Set the delay between each iteration in seconds
delay = 0.025

# Generate and print random binary numbers with animation
print_random_binary(binary_length, num_samples, delay)
