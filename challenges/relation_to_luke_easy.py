def relation_to_luke(name):
    relation = ""
    if name == "Darth Vader":
        relation = "father"
    elif name == "Leia":
        relation = "sister"
    elif name == "Han": 
        relation = "brother in law" 
    elif name == "R2D2":  
        relation = "droid"
    return "Luke, I am your " + relation + "."