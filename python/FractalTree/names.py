"""
Lists of tree name modifiers and species.
"""
DIRECTION = [
    "Northern", "Eastern", "Southern", "Western"
]

REGION = [
    "American", "Asian", "European", "African", "Oceanic", "Arctic",  # Continents
    "Canadian", "Brazilian", "Jamaican", "Chinese", "Japanese", "Peruvian", "Polish", "Kenyan", "Finnish", "Russian", "English",  # Countries
    "Mediterranean", "Appalachian", "Himalayan"
]

BIOME = [
    "Mountain", "Swamp", "Coastal", "Inland", "Tropical", "Alpine", "River", "Desert"
]

MISC = [
    "False", "Common", "Water", "King", "Plain", "Smooth", "Devils"
]

COLOUR = [
    "Black", "White", "Blue", "Red", "Green"
]

ALL_MODIFIERS = DIRECTION + REGION + BIOME + MISC + COLOUR

SPECIES = [
    "Maple", "Birch", "Ash", "Aspen", "Oak", "Poplar", "Locust", "Dogwood", "Alder", "Acacia", "Beech", "Ginkgo", 
    "Sycamore", "Hawthorn", "Willow", "Elm",  # Deciduous
    "Fir", "Pine", "Spruce", "Redwood", "Sequoia", "Larch", "Cypress", "Cedar", "Yew",  # Conifer
    "Chestnut", "Walnut",  # Nuts
    "Apple", "Crabapple", "Cherry", "Lemon", "Fig", "Plum",  # Fruit
]
