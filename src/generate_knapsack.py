import random
# return_dict = {"knapsack": some_max_weight int(1-100), "item_1": {"weight": int(1-100), "value": int(1-2000), "hardness": float(0-1), "ease_of_sale": float(0-1)}}

def generate(min_noi, max_noi):

    if min_noi > max_noi:
        raise ValueError("min number of items needs to be smaller than max number of items")

    knapsack = random.randint(1,100)
    noi = random.randint(min_noi,max_noi)
    counter = 1

    return_dict = {"knapsack": knapsack}

    while counter <= noi:
        return_dict["item_"+str(counter)] = {"weight": random.randint(1,50), "value": random.randint(1,2000), "hardness": random.random(), "ease_of_sale": random.random()}
        counter += 1

    return(return_dict)

if __name__ == "__main__":
    print(generate(1,5))