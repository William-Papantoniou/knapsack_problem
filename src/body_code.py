from generate_ipop import generate_initial_pop
from generate_fitness import fitness
from generate_knapsack import generate_knapsack
from select_pop import select_pop

#Generate inital pop Start
minimum_number_of_items = int(input("Please enter the minimum number of items "))
maximum_number_of_items = int(input("Please enter the maximum number of items "))
population_size = int(input("Please enter the population size "))
no_generations = int(input("Please enter how many generations you would like to run "))

if population_size % 2 != 0:
    population_size += 1

knapsack_return_value = generate_knapsack(minimum_number_of_items, maximum_number_of_items)

inital_pop_return_value = generate_initial_pop(knapsack_return_value["item_number"], population_size)

fitness_retrun_value = fitness(inital_pop_return_value["population"], knapsack_return_value["items"], knapsack_return_value["knapsack"])
#Generate inital pop End

parent_pop = select_pop(fitness_retrun_value)

print(parent_pop)
#Itteration of generations start
"""generation_counter = 0
while generation_counter < no_generations:
    #Selection begin
    #Selection End

    #Crossover/Mutation Begin
    #Crossover/Mutation End

    fitness_retrun_value = fitness()

    pass
#Itteration of generations end
"""