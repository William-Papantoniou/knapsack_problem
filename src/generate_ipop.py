from generate_knapsack import generate_knapsack
import random

#{"memberX": {"values": [1,1,1,1,1], "fitness": int()}}

def generate_initial_pop(min_item, max_item, pop_size):
    returned_value = generate_knapsack(min_item,max_item)
    number_of_items = returned_value["item_number"]
    counter = 0
    inital_pop = {}
    member_list = []

    for i in range(pop_size):
        while counter <= number_of_items:
            member_list.append(random.randint(0,1))
            counter += 1
        
        inital_pop["member_"+str(i+1)] = {"values": member_list, "fitness": 0}

        member_list = []
        counter = 0
    
    return(inital_pop)

if __name__ == "__main__":
    print(generate_initial_pop(1,5,5))
    