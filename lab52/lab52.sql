CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(100)
);

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT,
    total_amount DECIMAL(10,2),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

INSERT INTO customers (name, email) VALUES
('Alice', 'alice@email.com'),
('Bob', 'bob@email.com'),
('Carol', 'carol@email.com');

INSERT INTO orders (customer_id, total_amount) VALUES
(1, 250.00),
(2, 120.00),
(1, 80.00),
(NULL, 300.00);

SELECT customers.name, orders.order_id, orders.total_amount
FROM customers
INNER JOIN orders
ON customers.customer_id = orders.customer_id;

SELECT customers.name, orders.order_id, orders.total_amount
FROM customers
LEFT JOIN orders
ON customers.customer_id = orders.customer_id;

SELECT customers.name, orders.order_id, orders.total_amount
FROM customers
RIGHT JOIN orders
ON customers.customer_id = orders.customer_id;

SELECT customers.name, orders.order_id, orders.total_amount
FROM customers
FULL JOIN orders
ON customers.customer_id = orders.customer_id;

CREATE TABLE departments (
    dept_id SERIAL PRIMARY KEY,
    dept_name VARCHAR(50)
);

CREATE TABLE employees (
    emp_id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    dept_id INT REFERENCES departments(dept_id)
);

INSERT INTO departments (dept_name) VALUES
('HR'),
('IT'),
('Finance');

INSERT INTO employees (name, dept_id) VALUES
('Alex', 1),
('Ben', 2),
('Clara', NULL);

SELECT employees.name, departments.dept_name
FROM employees
INNER JOIN departments
ON employees.dept_id = departments.dept_id;

SELECT employees.name, departments.dept_name
FROM employees
LEFT JOIN departments
ON employees.dept_id = departments.dept_id;

SELECT employees.name, departments.dept_name
FROM employees
RIGHT JOIN departments
ON employees.dept_id = departments.dept_id;

SELECT employees.name, departments.dept_name
FROM employees
FULL JOIN departments
ON employees.dept_id = departments.dept_id;

CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE courses (
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(50)
);

CREATE TABLE enrollments (
    enroll_id SERIAL PRIMARY KEY,
    student_id INT REFERENCES students(student_id),
    course_id INT REFERENCES courses(course_id)
);

INSERT INTO students (name) VALUES
('Emma'),
('David'),
('Lisa');

INSERT INTO courses (course_name) VALUES
('Math'),
('Science'),
('History');

INSERT INTO enrollments (student_id, course_id) VALUES
(1,1),
(2,2);

SELECT students.name, courses.course_name
FROM students
INNER JOIN enrollments
ON students.student_id = enrollments.student_id
INNER JOIN courses
ON enrollments.course_id = courses.course_id;

SELECT students.name, courses.course_name
FROM students
LEFT JOIN enrollments
ON students.student_id = enrollments.student_id
LEFT JOIN courses
ON enrollments.course_id = courses.course_id;

SELECT students.name, courses.course_name
FROM students
RIGHT JOIN enrollments
ON students.student_id = enrollments.student_id
RIGHT JOIN courses
ON enrollments.course_id = courses.course_id;

SELECT students.name, courses.course_name
FROM students
FULL JOIN enrollments
ON students.student_id = enrollments.student_id
FULL JOIN courses
ON enrollments.course_id = courses.course_id;
