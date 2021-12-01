def fitness(population, items, max_weight):
    inbetween_dict = {"weight": 0, "value": 0, "hardness": 0, "ease_of_sale": 0}
    for member in population:
        for i in range(len(member["values"])):
            if member["values"][i]:
                inbetween_dict["weight"] = inbetween_dict["weight"] + items["item_"+str(i)]["weight"]
                inbetween_dict["value"] = inbetween_dict["value"] + items["item_"+str(i)]["value"]
                inbetween_dict["hardness"] = inbetween_dict["hardness"] + items["item_"+str(i)]["hardness"]
                inbetween_dict["ease_of_sale"] = inbetween_dict["ease_of_sale"] + items["item_"+str(i)]["ease_of_sale"]

        if inbetween_dict["weight"] > max_weight:
            member["fitness"] = 0
        
        else:
            member["fitness"] = inbetween_dict["value"] + 2*inbetween_dict["hardness"] + 1.5*inbetween_dict["ease_of_sale"]
        
        inbetween_dict = {"weight": 0, "value": 0, "hardness": 0, "ease_of_sale": 0}
    
    return(population)
