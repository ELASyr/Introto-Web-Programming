CREATE TABLE employees (
	id SERIAL PRIMARY KEY,
	first_name TEXT,
	last_name TEXT,
	department TEXT,
	salary INTEGER,
	hire_date DATE
);

INSERT INTO employees (first_name, last_name, department, salary, hire_date) VALUES
('Alice', 'Smith', 'HR', 50000, '2020-06-15'),
('Bob', 'Johnson', 'IT', 70000, '2019-08-23'),
('Charlie', 'Williams', 'Finance', 65000, '2021-03-11'),
('David', 'Brown', 'IT', 72000, '2018-09-30'),
('Emma', 'Davis', 'HR', 48000, '2022-01-05');

-- COUNT()
SELECT COUNT(*) FROM employees;
SELECT COUNT(*) FROM employees WHERE department = 'IT';
SELECT COUNT(salary) FROM employees;
SELECT department, COUNT(*) FROM employees GROUP BY department;

SELECT department, COUNT(*) 
FROM employees 
GROUP BY department 
HAVING COUNT(*) >= 3;


-- SUM()
SELECT SUM(total_amount) FROM orders;
SELECT SUM(total_amount) FROM orders WHERE order_date BETWEEN '2023-01-01' AND '2023-12-31';

SELECT customer_id, SUM(total_amount) 
FROM orders 
GROUP BY customer_id;

SELECT customer_id, SUM(total_amount) 
FROM orders 
GROUP BY customer_id 
HAVING SUM(total_amount) > 500;

SELECT SUM(price) + SUM(tax) AS total_price_and_tax FROM sales;
SELECT SUM(DISTINCT price) FROM products;


-- AVG()
SELECT AVG(total_amount) FROM sales;
SELECT AVG(total_amount) FROM sales WHERE order_date BETWEEN '2023-01-01' AND '2023-12-31';

SELECT customer_id, AVG(total_amount) 
FROM sales 
GROUP BY customer_id;

SELECT customer_id, AVG(total_amount) 
FROM sales 
GROUP BY customer_id 
HAVING AVG(total_amount) > 100;

SELECT AVG(quantity) FROM order_items;
SELECT AVG(DISTINCT price) FROM products;


-- MIN()
SELECT MIN(price) FROM products;
SELECT MIN(order_date) FROM orders WHERE order_status = 'shipped';
SELECT category, MIN(price) FROM products GROUP BY category;

SELECT category, MIN(price) 
FROM products 
GROUP BY category 
HAVING MIN(price) > 50;

SELECT MIN(hire_date) FROM employees;
SELECT product_name, MIN(quantity_in_stock) FROM inventory;


-- MAX()
SELECT MAX(salary) FROM employees;
SELECT MAX(order_date) FROM orders WHERE order_status = 'shipped';
SELECT category, MAX(price) FROM products GROUP BY category;

SELECT category, MAX(price) 
FROM products 
GROUP BY category 
HAVING MAX(price) > 100;

SELECT MAX(hire_date) FROM employees;
SELECT product_name, MAX(quantity_in_stock) FROM inventory;


-- GROUP BY and HAVING
SELECT store_id, SUM(amount) AS total_sales
FROM sales
GROUP BY store_id;

SELECT store_id, SUM(amount) AS total_sales
FROM sales
GROUP BY store_id
HAVING SUM(amount) > 100000;

SELECT store_id, product_id, SUM(amount) AS total_sales
FROM sales
GROUP BY store_id, product_id;

SELECT customer_id, COUNT(order_id) AS total_orders
FROM orders
GROUP BY customer_id;

SELECT department, AVG(salary) AS average_salary
FROM employees
GROUP BY department;

SELECT department, SUM(salary) AS total_salary
FROM employees
GROUP BY department
HAVING SUM(salary) > 500000;

SELECT customer_id, COUNT(order_id) AS total_orders
FROM orders
GROUP BY customer_id
HAVING COUNT(order_id) > 5;