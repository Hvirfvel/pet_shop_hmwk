# WRITE YOUR FUNCTIONS HERE
import pdb
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, input_cash):
    pet_shop["admin"]["total_cash"] += input_cash
    
    
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]
    
def increase_pets_sold(pet_shop, pets_sold):
    pet_shop["admin"]["pets_sold"] += pets_sold
    
def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, input_breed):
    list_of_breed = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == input_breed:
            list_of_breed.append(pet)
    return list_of_breed

def find_pet_by_name(pet_shop, input_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == input_name:
            return pet

def remove_pet_by_name(pet_shop, input_name):
    list_index = -1
    for pet in pet_shop["pets"]:
        list_index += 1
        if pet["name"] == input_name:
            del pet_shop["pets"][list_index]
            break

def add_pet_to_stock(pet_shop, input_new_pet):
    pet_shop["pets"].append(input_new_pet)

def get_customer_cash (customer):
    return customer["cash"]

def remove_customer_cash(customer, used_cash):
    customer["cash"] -= used_cash

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, input_new_pet):
    customer["pets"].append(input_new_pet)