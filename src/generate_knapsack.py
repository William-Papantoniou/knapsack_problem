import random

def generate_knapsack(min_noi, max_noi):

    if min_noi > max_noi:
        raise ValueError("min number of items needs to be smaller than max number of items")

    knapsack = random.randint(1,100)
    noi = random.randint(min_noi,max_noi)
    counter = 1

    return_dict = {"knapsack": knapsack}

    while counter <= noi:
        return_dict["item_"+str(counter)] = {"weight": random.randint(1,50), "value": random.randint(1,2000), "hardness": random.random(), "ease_of_sale": random.random()}
        counter += 1

    return{"item_number": noi ,"items": return_dict}
