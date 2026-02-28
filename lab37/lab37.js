// Lab 1
let fruits = [];
fruits.push("apple");
fruits.push("banana");
fruits.push("cherry");

let el = fruits.pop();
console.log("Removed", el);

console.log(fruits);

// Lab 2
let numbers = [10, 20, 30, 40, 50];
let sliced = numbers.slice(1, 3);

console.log(sliced);
console.log(numbers);

//Lab 3
let nums = [1, 2, 3, 4, 5];
let squared = nums.map(n => n ** 2);

console.log("Original -", nums);
console.log("Squared - ", squared);

// Lab 4
let ages = [12, 18, 25, 30, 15];
let filtered = ages.filter(i => i >= 18);

console.log("Filtered ages:", filtered);

// Lab 5
let user = {
    name: "Alice",
    age: 25,
    city: "New York"
}

console.log("Name of the user:", user.name);

user.age = 26;
console.log("Updated age of the user:", user.age);

// Lab 6
let car = {
    brand: "Tesla",
    model: "Model S",
    year: 2023
}

let keys = Object.keys(car);
let values = Object.values(car);

console.log("Keys:", keys);
console.log("Values:", values);