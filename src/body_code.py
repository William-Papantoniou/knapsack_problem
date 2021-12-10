import csv

from generate_ipop import generate_initial_pop
from generate_fitness import fitness
from generate_knapsack import generate_knapsack
from select_pop import select_pop
from crossover_mutation import crossover_mutation


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

#Itteration of generations start
generation_counter = 0

best_performing_gnome = []
top_performer = {"value": [], "fitness": 0}

while generation_counter < no_generations:
    parent_pop = select_pop(fitness_retrun_value)

    crossover_mutated_pop = crossover_mutation(parent_pop, population_size, knapsack_return_value["item_number"])

    fitness_retrun_value = fitness(crossover_mutated_pop, knapsack_return_value["items"], knapsack_return_value["knapsack"])

    max_fit = 0

    for item in fitness_retrun_value:
        if fitness_retrun_value[item]["fitness"] >= max_fit:
            max_fit = fitness_retrun_value[item]["fitness"]
            best_performing_gnome.append(fitness_retrun_value[item])
            
            if fitness_retrun_value[item]["fitness"] > top_performer["fitness"]:
                top_performer = fitness_retrun_value[item]



    generation_counter += 1

print(best_performing_gnome)
print("\n\n\n")
print(top_performer)

#Itteration of generations end
