#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    pass
    def __init__(self, name= "tom", breed="Mastiff"):
        self.name = name
        self.breed = breed
    def get_name(self):
        return self._name
    def set_name(self, name):
        if type(name) == str:
            if len(name) < 1 or len(name) > 25:
                print("Name must be string between 1 and 25 characters.")
                self.name = "tom"
            else:
                self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")
            self.name = "tom"
    name = property(get_name, set_name)
    def get_breed(self):
        return self._breed
    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")
            self.breed = "Mastiff"
    breed = property(get_breed, set_breed)        