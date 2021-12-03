import random

def crossover_mutation(parents, pop_size, noi):
    crossover_mutated_dict = {}
    counter = 1
    while len(crossover_mutated_dict) <= pop_size:
        first = random.randint(1,len(parents))
        second = random.randint(1,len(parents))
        if noi % 2 == 0 and first != second:
            slice_amount = int(noi/2)
            crossover_mutated_dict["member_"+str(counter)] = {"values": parents["member_"+str(first)]["values"][:(slice_amount)] + parents["member_"+str(second)]["values"][-(slice_amount):], "fitness": 0}
            counter += 1
        
        elif noi % 2 != 0 and first != second:
            slice_amount = int(round(noi/2))
            crossover_mutated_dict["member_"+str(counter)] = {"values": parents["member_"+str(first)]["values"][:(slice_amount)] + parents["member_"+str(second)]["values"][-(slice_amount+1):], "fitness": 0}
            counter += 1

    internal_counter = 0
    for member in crossover_mutated_dict:
        for item in crossover_mutated_dict[member]["values"]:
            mutation = random.randint(1,10000)
            if mutation == 1:
                if item == 1:
                    crossover_mutated_dict[member][internal_counter] = 0
                
                else:
                    crossover_mutated_dict[member][internal_counter] = 1
            
            internal_counter += 1
        internal_counter = 0

    return(crossover_mutated_dict)