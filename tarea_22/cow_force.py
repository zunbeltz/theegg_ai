"""Maximize cow milk production subject to cow total weight contrain."""

from itertools import combinations

# we import test data
from data import cows, weight_limit

solution = []
solution_weight = 0  # pylint: disable=C0103
solution_milk = 0  # pylint: disable=C0103
cow_numbers = cows.keys()
all_combinations = sum([list(map(list, combinations(cow_numbers, i)))
                        for i in range(len(cow_numbers) + 1)], [])
#print(all_combinations)

# We iterate for every combination
for combination in all_combinations:
    print(combination)
    weight = sum([cows[i][0] for i in combination])
    if weight < weight_limit:
        milk = sum([cows[i][1] for i in combination])
        print(weight, milk)
        if milk > solution_milk:
            solution_milk = milk
            solution_weight = weight
            solution = combination
    else:
        continue

print()
print("The solution by force")
print("-"*20)
print(f"Limit weight: {weight_limit}")
print(f"Soluiton weight: {solution_weight}")
print(f"Soluiton milk: {solution_milk}")
print(f"Solution cow list: {solution}")
