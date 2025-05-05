CREATE TABLE Role (
    role_id INTEGER PRIMARY KEY AUTOINCREMENT,
    role_name TEXT NOT NULL UNIQUE
);
CREATE TABLE Users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    role_id INTEGER NOT NULL,
    full_name TEXT NOT NULL,
    employee_id INTEGER,
    FOREIGN KEY (role_id) REFERENCES Role(role_id) FOREIGN KEY (employee_id) REFERENCES Employees(employee_id)
);
CREATE TABLE Tasks (
    task_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    employee_id INTEGER NOT NULL,
    start_date DATE,
    due_date DATE,
    status TEXT,
    FOREIGN KEY (employee_id) REFERENCES Employees(employee_id)
);
CREATE TABLE Employees (
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    email TEXT,
    phone text,
    position TEXT
);