// Lab 1
function sum(a, b) {
    return a + b;
}

console.log(sum(12, 31));

let square = (num) => num ** 2;
console.log(square(3));

let max = function (a, b) {
    if (a >= b) {
        return a;
    } else {
        return b;
    }
}

console.log(max(-23, 0));

// Lab 2
let message = "Hello from global";

function printMessage() {
    let localMessage = "Hello from local";

    console.log(localMessage);
}

printMessage();
console.log(message);
// console.log(localMessage); - not defined

// Lab 3
if (true) {
    var a = "Inside block using var";
    let b = "Inside block using let";
    const c = "Inside block using const";

}

console.log(a);
// console.log(b); - not defined
// console.log(c); - not defined

// Lab 4
function counter() {
    let i = 0;

    return function increase() {
        i++;

        console.log(i);
    }
}

let counter1 = counter();
counter1();
counter1();

let counter2 = counter();
counter2();