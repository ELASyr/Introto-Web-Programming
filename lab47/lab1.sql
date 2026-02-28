CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    age INT
);

INSERT INTO users (name, email, age) 
VALUES ('Alice', 'alice@example.com', 20);

SELECT * FROM users;
