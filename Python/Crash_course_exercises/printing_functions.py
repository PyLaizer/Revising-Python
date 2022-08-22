#Exercise 8.15 & 8.16 & 8.17

def print_models(uncompleted,completed):
    """Summarizes and Prints out all the uncompleted design and moves them to a new list"""
    while uncompleted:
        design = uncompleted.pop()
        print(f"Printing model: {design}")
        completed.append(design)


def show_models(completed_designs):
    """Prints out all completed designs in the list"""
    print("\n The following models have been printed")
    for completed_design in completed_designs:
        print(f"- {completed_design}")


unprinted_designs = ["phone case","robot pendant","dodecahedron"]
completed_models = []

print_models(unprinted_designs,completed_models)
show_models(completed_models)        
