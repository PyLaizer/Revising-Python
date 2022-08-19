

def print_models(uncompleted,completed):
    while uncompleted:
        design = uncompleted.pop()
        print(f"Printing model: {design}")
        completed.append(design)

unprinted_designs = ["phone case","robot pendant","dodecahedron"]
completed_models = []
print_models(unprinted_designs,completed_models)


def show_models(completed_designs):
    print("\n The following models have been printed")
    for completed_design in completed_designs:
        print(f"- {completed_design}")

show_models(completed_models)        
