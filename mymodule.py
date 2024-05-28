# Aqui se hacen ajustes de último momento antes del Release 1.0
import random
import string

# New mymodule.py file
def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname

def user_id_gen_by_user():
    # Get the number of characters for each ID
    num_characters = int(input("Enter the number of characters for each ID: "))
    
    # Get the number of IDs to generate
    num_ids = int(input("Enter the number of IDs to generate: "))
    
    # Helper function to generate a single ID
    generate_id = lambda: ''.join(random.choices(string.ascii_letters + string.digits, k=num_characters))
    
    # Generate the specified number of IDs using map
    ids = list(map(lambda _: generate_id(), range(num_ids)))
    
    # Print the generated IDs
    print("\n".join(ids))