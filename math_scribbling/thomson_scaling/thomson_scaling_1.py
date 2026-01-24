import numpy as np

true_chance = 0.7

successes = 0
failures = 0

def show_ad(): 
    if np.random.rand() < 0.7:
        return 1
    return 0

#100 vs 10

for i in range(10):
    result = show_ad()
    print(result)
    if result == 1: 
        successes += 1
    else: 
        failures += 1

average = 0
ai_guesses = []

for _ in range(100):
    ai_guesses.append(np.random.beta(successes, failures))

average = sum(ai_guesses)/len(ai_guesses)

print(average)
print(successes, failures)