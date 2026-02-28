// Lab 1
console.log("Start");

setTimeout(() => {
    console.log("Inside setTimeout");
}, 2000);

console.log("End");

// Lab 2
function delayedMessage(message, delay) {
    setTimeout(() => {
        console.log(message);
    }, delay);
}

delayedMessage("Hello, after 3 seconds!", 3000);

// Lab 3
function startCounter() {
    let counter = 1;

    let c = setInterval(() => {
        console.log("Counter:", counter);

        if (counter == 5) {
            clearInterval(c);
        }

        counter++;
    }, 1000);
}

startCounter();

// Lab 4
function fetchData() {
    return new Promise((resolve, rejetc) => {
        setTimeout(() => {
            let success = true;

            if (success) {
                resolve("Data received");
            } else {
                rejetc("Failed to fetch data");
            }
        }, 2000)
    })
}

fetchData()
    .then((data) => console.log(data))
    .catch((error) => console.error(error))
    .finally(() => console.log("Request completed"));

// Lab 5
function fetchData() {
    return new Promise((resolve, rejetc) => {
        setTimeout(() => {
            if (Math.random() > 0.5) {
                resolve("Data received");
            } else {
                rejetc("Error: Failed to fetch data");
            }
        }, 2000)
    })
}

fetchData()
    .then((data) => console.log(data))
    .catch((error) => console.error(error))
    .finally(() => console.log("Request completed"));