class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        if pet_type in Pet.PET_TYPES:
            self.pet_type = pet_type
        else:
            raise ValueError("Invalid pet type")
        self.owner = owner
        if owner is not None:
            owner.add_pet(self)  
        Pet.all.append(self)

    
class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        return self._pets 

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
            self._pets.append(pet)
        else:
            raise ValueError("Pet not added")
    
    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)
    
mitchelle = Owner("Mitchelle")
dog = Pet('Boomer', "dog", mitchelle)
print(dog.name, dog.pet_type, dog.owner.name)