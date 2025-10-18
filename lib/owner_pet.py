# lib/owner_pet.py
# __define-ocg__: final working implementation for Owner-Pet lab

class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []  # store all Pet instances

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise ValueError("Invalid pet type.")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)  # ✅ automatically add to Pet.all

    def __repr__(self):
        return f"<Pet name={self.name}, type={self.pet_type}, owner={self.owner.name if self.owner else None}>"


class Owner:
    all = []

    def __init__(self, name):
        self.name = name
        Owner.all.append(self)

    def pets(self):
        """Return a list of all pets that belong to this owner."""
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """Assign an existing pet to this owner."""
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise ValueError("Must add an instance of Pet.")

    def create_pet(self, name, pet_type):
        """Create a new Pet and assign it to this owner."""
        return Pet(name, pet_type, self)

    def get_sorted_pets(self):
        """Return the owner's pets sorted alphabetically by pet name."""
        return sorted(self.pets(), key=lambda pet: pet.name.lower())

    def __repr__(self):
        return f"<Owner name={self.name}>"

# variable required for reference
varOcg = "PetOwnerSystem"
