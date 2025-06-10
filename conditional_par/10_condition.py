
pet_type = "Dog"
pet_age = 2

if pet_type == "Dog":
    if pet_age <= 2:
        food_type = "Puppy Food"
    else:
        food_type = "Senior Dog Food"
elif pet_type == "Cat":
    if pet_age <= 2:
        food_type = "Kitty Food"
    else:
        food_type = "Senior Cat Food"

print("Your Pet (" + pet_type + ") needs " + food_type )