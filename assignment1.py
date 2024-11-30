"""
Problem Statement

Consider that the human tower is to be performed on a stage and stage has a maximum weight limit.
Assume that:
Write a python program to find the maximum number of people at the base level such that the total weight of tower does not exceed the maximum weight limit of the stage.
Each person weighs 50 kg.
There will always be odd number of men at the base level of the human tower.
"""
def human_pyramid(no_of_people):

  if no_of_people == 1:
    return 50  # Weight of the single person at the top

  return 50 + 2 * human_pyramid(no_of_people - 1)  # Weight of the current level + weight of the pyramid above

def find_maximum_people(max_weight):

  no_of_people = 1

  while human_pyramid(no_of_people) <= max_weight:
    no_of_people += 2

  return no_of_people - 2

# Example usage:
max_weight = 1000
max_people = find_maximum_people(max_weight)
print(max_people)