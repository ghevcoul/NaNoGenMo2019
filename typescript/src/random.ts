// A collection of helper functions interfacing with the JS built-in Math.random

// Get a random integer between min and max inclusive
export function getRandomInt(min: number, max: number): number {
  return Math.floor(Math.random() * (max - min + 1) + min)
}

// Get a random float between min (include) and max (exclusive)
export function getRandomFloat(min: number, max: number): number {
  return Math.random() * (max - min) + min
}

// Get a random value from an input array and return it
export function getValueFromArray(list: Array<any>): any {
  const arrayPos = getRandomInt(0, list.length - 1)
  return list[arrayPos]
}
