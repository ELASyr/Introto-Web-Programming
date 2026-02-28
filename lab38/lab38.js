// Lab 1
let str = '{"name":"Alice", "age":25, "occupation":"student"}';

function parseJSON(jsonStr) {
    try {
        let parse = JSON.parse(jsonStr);

        console.log(parse.name);
    } catch (error) {
        console.error("Invalid JSON format");
    }
}

parseJSON(str);
parseJSON('{name:"Alice", "age":25, "occupation":"student"}');

// Lab 2
let numbers = [12, 0, 21, -1, 16, 4, -8];
let sum = 0;

for (let i = 0; i < numbers.length; i++) {
    console.log(numbers[i]);

    if (numbers[i] % 2 == 0) {
        sum += numbers[i];
    }
}

console.log("Sum:", sum);

// Lab 3
let users = [
    {name: "Alice", age: 25},
    {name: "Mark", age: 31},
    {name: "Olive", age: 16}
]

console.table(users);

// Lab 4
function divide(a, b) {
    try {
        if (b === 0) {
            throw new Error("Cannot divide by zero");
        }

        let res = a / b;

        return res;
    } catch (error) {
        console.error(error.message);
    }
}

console.log(divide(16, 4));
console.log(divide(25, 0));

// Lab 5
try {
    console.log(idenVar);
} catch (error) {
    console.error("Variable is not defined");
}