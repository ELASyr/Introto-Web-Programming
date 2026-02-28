-- Lab 1
CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	full_name TEXT NOT NULL,
	email VARCHAR(100) NOT NULL UNIQUE,
	birth_date DATE NOT NULL,
	is_active BOOLEAN DEFAULT TRUE
);

SELECT * FROM users;

-- Lab 2
CREATE TABLE products (
	product_id SERIAL PRIMARY KEY,
	name TEXT NOT NULL,
	price DECIMAL(10, 2) NOT NULL,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

SELECT * FROM products;

-- Lab 3
DROP TABLE IF EXISTS products;
SELECT * FROM products;

-- Lab 4
ALTER TABLE users ADD phone_number VARCHAR(20);
SELECT phone_number FROM users;

-- Lab 5
ALTER TABLE users DROP COLUMN phone_number;
SELECT phone_number FROM users;

-- Lab 6
ALTER TABLE users RENAME COLUMN full_name TO name;
SELECT name FROM users;

-- Lab 7
ALTER TABLE products ALTER COLUMN price type INTEGER;
SELECT price FROM products;