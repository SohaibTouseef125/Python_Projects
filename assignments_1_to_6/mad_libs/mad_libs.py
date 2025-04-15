def mad_libs():
    print("Let\'s play mad libs fill in the blanks!😊")
    name:str = input("Enter a name: ")
    place:str = input("Enter a place: ")
    funny_adjective:str = input("Enter an adjective: ")
    random_object:str = input("Enter an object: ")
    animal:str = input("Enter an animal: ")
    action_verb:str = input("Enter an action verb: ")
    funny_expression:str = input("Enter an expression: ")

    story = f"""
    There once was a person named {name}.
    They lived in {place}.
    They loved {funny_adjective} {random_object}.
    They also loved {animal}.
    They {action_verb} {funny_expression}.
    """
    print(f"\nHere is your Mad Lib story:{story}")
if __name__ == "__main__":
        mad_libs()