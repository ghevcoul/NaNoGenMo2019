export const DIRECTION = [
  "Northern", "Eastern", "Southern", "Western"
]

export const REGION = [
  "American", "Asian", "European", "African", "Oceanic", "Arctic",  // Continents
  "Canadian", "Brazilian", "Jamaican", "Chinese", "Japanese", "Peruvian", "Polish", "Kenyan", "Finnish", "Russian", "English",  // Countries
  "Mediterranean", "Appalachian", "Himalayan"
]

export const BIOME = [
  "Mountain", "Swamp", "Coastal", "Inland", "Tropical", "Alpine", "River", "Desert"
]

export const MISC = [
  "False", "Common", "Water", "King", "Plain", "Smooth", "Devils"
]

export const COLOUR = [
  "Black", "White", "Blue", "Red", "Green"
]

export const ALL_MODIFIERS = DIRECTION.concat(REGION, BIOME, MISC, COLOUR)

export const SPECIES = [
  "Maple", "Birch", "Ash", "Aspen", "Oak", "Poplar", "Locust", "Dogwood", "Alder", "Acacia", "Beech", "Ginkgo", 
  "Sycamore", "Hawthorn", "Willow", "Elm",  // Deciduous
  "Fir", "Pine", "Spruce", "Redwood", "Sequoia", "Larch", "Cypress", "Cedar", "Yew",  // Conifer
  "Chestnut", "Walnut",  // Nuts
  "Apple", "Crabapple", "Cherry", "Lemon", "Fig", "Plum",  // Fruit
]