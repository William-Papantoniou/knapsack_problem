import random
def select_pop(population_and_fitness):
    parent_pop = {}
    counter = 1
    
    while len(parent_pop) != len(population_and_fitness)/2:
        first_fighter = random.randint(1, len(population_and_fitness))
        second_fighter = random.randint(1, len(population_and_fitness))
        
        if population_and_fitness["member_"+str(first_fighter)]["fitness"] >= population_and_fitness["member_"+str(second_fighter)]["fitness"]:
            parent_pop["member_"+str(counter)] = population_and_fitness["member_"+str(first_fighter)]
            counter += 1
        
        elif population_and_fitness["member_"+str(first_fighter)]["fitness"] < population_and_fitness["member_"+str(second_fighter)]["fitness"]:
            parent_pop["member_"+str(counter)] = population_and_fitness["member_"+str(second_fighter)]
            counter += 1
        
    
    return(parent_pop)

    