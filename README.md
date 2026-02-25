📘 Student Result Management System (CLI)
📌 Overview

The Student Result Management System is a menu-driven Command Line Interface (CLI) application developed using Python. The project demonstrates core programming concepts such as Object-Oriented Programming (OOP), file handling using JSON, and exception handling.

This system allows users to manage student academic records efficiently through a simple terminal-based interface.

---
🚀 Features

1. Add new student records

2. Automatically calculate grades based on average marks

3. Search students by roll number

4. Display all stored student records

5. Persistent data storage using JSON file

6. Input validation using exception handling
---

🛠️ Technologies Used

Python 3

Object-Oriented Programming (Classes & Methods)

JSON File Handling

Exception Handling

Git & GitHub for version control
---

🧠 System Design

The application is structured using two main classes:

1️⃣ Student Class

Stores student details (roll number, name, marks)

Calculates grade based on average marks

Converts student data into dictionary format for storage
---

2️⃣ StudentManager Class

Handles file operations (load & save)

Manages student records

Implements add, search, and display functionalities

Student data is stored in a students.json file to ensure persistent storage across program executions.
---

▶️ How to Run the Project

Clone the repository:

git clone https://github.com/jadhav2003/Smart-CLI-Appln.git

Navigate to the project folder:

cd Smart-CLI-Appln
---
Run the program:

python main.py
📂 Project Structure
Smart-CLI-Appln/
│── main.py
│── students.json
│── README.md
│── requirements.txt
│── .gitignore
🎯 Learning Outcomes

Through this project, the following concepts were implemented:

Practical implementation of OOP in Python

Working with structured data using JSON

File read/write operations

Handling runtime errors using exceptions

Using Git for version control and GitHub for project hosting