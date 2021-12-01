import random

#{"memberX": {"values": [1,1,1,1,1], "fitness": int()}}

def generate_initial_pop(number_of_items, pop_size):
    counter = 0
    inital_pop = {}
    member_list = []

    for i in range(pop_size):
        while counter < number_of_items:
            member_list.append(random.randint(0,1))
            counter += 1
        
        inital_pop["member"+str(i+1)] = {"values": member_list, "fitness": 0}

        member_list = []
        counter = 0
    
    return{"population": inital_pop}

if __name__ == "__main__":
    print(generate_initial_pop(6,5))
    