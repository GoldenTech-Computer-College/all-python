animals = {
    'mammals': {
        'land': {
            'carnivores': {
                'big_cats': ['lion', 'tiger'],
                'bears': ['grizzly bear', 'polar bear']
            },
            'herbivores': {
                'large': ['elephant', 'giraffe'],
                'small': ['rabbit', 'deer']
            },
            'omnivores': ['bear', 'human']
        },
        'aquatic': {
            'cetaceans': {
                'toothed_whales': ['dolphin', 'killer whale'],
                'baleen_whales': ['blue whale', 'humpback whale']
            },
            'pinnipeds': {
                'true_seals': ['harbor seal', 'elephant seal'],
                'eared_seals': ['sea lion', 'fur seal']
            }
        }
    },
    'birds': {
        'flightless': {
            'ratites': {
                'large': {
                    'ostrich': {
                        'habitat': 'Savannah',
                        'speed': '70 km/h'
                    }
                },
                'small': ['kiwi', 'cassowary']
            },
            'penguins': ['emperor penguin', 'king penguin']
        },
        'birds_of_prey': {
            'diurnal': ['eagle', 'hawk'],
            'nocturnal': ['owl']
        }
    },
    'reptiles': {
        'snakes': {
            'venomous': ['cobra', 'rattlesnake'],
            'non_venomous': ['python', 'boa constrictor']
        },
        'turtles': ['loggerhead', 'leatherback'],
        'lizards': {
            'iguanas': ['green iguana', 'marine iguana'],
            'geckos': ['leopard gecko', 'crested gecko']
        }
    },
    'amphibians': {
        'anurans': {
            'frogs': ['bullfrog', 'tree frog'],
            'toads': ['American toad', 'cane toad']
        },
        'caudates': ['salamander', 'newt']
    },
    'invertebrates': {
        'arthropods': {
            'insects': {
                'hymenoptera': ['ant', 'bee'],
                'lepidoptera': ['butterfly', 'moth']
            },
            'arachnids': {
                'spiders': ['tarantula', 'black widow'],
                'scorpions': ['emperor scorpion', 'bark scorpion']
            },
            'crustaceans': ['crab', 'lobster']
        },
        'mollusks': {
            'cephalopods': ['octopus', 'squid'],
            'gastropods': ['snail', 'slug']
        }
    }
}

# Implement the following functions:
# 2. get_animal() Method that takes an animal type as a parameter and returns the list of animals of that type. If the animal type is not found, return "Animal type {animal_type} not found."
# 3. get_animals() Method that returns the animals dictionary. If the dictionary is empty, return "Animal dictionary is empty."
# 4. get_land_mammals() Method that returns the list of land mammals.
# 5. get_aquatic_mammals() Method that returns the list of aquatic mammals.
# 6. get_flightless_birds() Method that returns the list of flightless birds.
# 7. get_birds_of_prey() Method that returns the list of birds of prey.
# 8. get_snakes() Method that returns the list of snakes.
# 9. count_insects() Method that returns the count of insects in the animals dictionary.
# 10. get_flightless_birds_habitat() Method that returns the habitat of the ostrich. The output should be "Savannah".

def get_land_mammals(animals):
    canivores = animals['mammals']['land']['carnivores']
    herbivores = animals['mammals']['land']['herbivores']
    omnivores = animals['mammals']['land']['omnivores']
    # print (f"Land mammals include: {canivores}, {herbivores} and {omnivores}")
    return f"Land mammals include: {canivores}, {herbivores} and {omnivores}"
# print(get_land_mammals(animals))

def get_flightless_birds_habitat(animals):
    habitat = animals['birds']['flightless']['ratites']['large']['ostrich']['habitat']
    return f"The habitat of the ostrich is: {habitat}"
print(get_flightless_birds_habitat(animals))

def get_aquatic_mammals(animals):
    cetaceans = animals.get('mammals').get('aquatic').get('cetaceans')
    pinnipeds = animals.get('mammals').get('aquatic').get('pinnipeds')
    return f"Aquatic mammals include: {cetaceans} and {pinnipeds}"