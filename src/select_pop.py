import random
def select_pop(population_and_fitness):
    parent_pop = {}
    counter = 1
    max_fit = 0
    best_gnome = {}

    # This code adds superority
    for member in population_and_fitness:
        if population_and_fitness[member]["fitness"] >= max_fit:
            max_fit = population_and_fitness[member]["fitness"]
            best_gnome = population_and_fitness[member]
    
    parent_pop["member_"+str(counter)] = best_gnome
    counter += 1

    while len(parent_pop) != int(len(population_and_fitness)/2):
        first_fighter = random.randint(1, len(population_and_fitness))
        second_fighter = random.randint(1, len(population_and_fitness))
        
        # Need to find a better solution to having two ppl who equal 0 just select the first one
        if population_and_fitness["member_"+str(first_fighter)]["fitness"] >= population_and_fitness["member_"+str(second_fighter)]["fitness"]:
            parent_pop["member_"+str(counter)] = population_and_fitness["member_"+str(first_fighter)]
            counter += 1
        
        elif population_and_fitness["member_"+str(first_fighter)]["fitness"] < population_and_fitness["member_"+str(second_fighter)]["fitness"]:
            parent_pop["member_"+str(counter)] = population_and_fitness["member_"+str(second_fighter)]
            counter += 1
        
    
    return(parent_pop)

    