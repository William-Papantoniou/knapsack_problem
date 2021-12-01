from generate_ipop import generate_initial_pop
from generate_fitness import fitness
from generate_knapsack import generate_knapsack

minimum_number_of_items = 5
maximum_number_of_items = 10
population_size = 5

knapsack_return_value = generate_knapsack(minimum_number_of_items, maximum_number_of_items)

inital_pop_return_value = generate_initial_pop(knapsack_return_value["item_number"], population_size)

fitness_retrun_value = fitness(inital_pop_return_value["population"], knapsack_return_value["items"], knapsack_return_value["knapsack"])

print(fitness_retrun_value)
