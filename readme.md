# Library Management System

#### A compact Python-based tool designed to manage books and their related information using a clean, relational SQLite database.
#### Although the project is small , the structure is intentionally internal tool or a personal learning project.
---
## Overview

Is the system brings together several elements of a real library environment: authors, publishers, categories, translators, resources, languages, and of course, the books themselves
Each part is stored in a dedicated table and connected through relation tables , which gives the project a solid , database-driven backbone

All work take place through a simple command-line interface.
There is no flashy UI here—just straightforward commands that allow you to insert, list, or remove data while keeping things transparent and easy to follow.
---
 Key Features
📖 Book Management

A book can include:

- multiple authors

- different languages

- various categories

- cover designers

- translators

- external resources

* The system ensures data consistency and prevents accidental deletion of items that are still linked to books.
---
Possible operations

You can add or remove:

1. Authors

2. Publishers

3. Languages

4. Categories

5. Translators

6. Cover Designers

7. Resources

* **Before anything gets removed, the system checks whether it’s still in use in related tables.**

💻 Command-Line Interface

- Commands feel natural and simple. Examples:

    - insert author John 1978-10-12 American
    - insert category Fantasy
    - delete publisher 2


- Adding a book follows a structure:

    - insert book Title 1045 [1,2] Adult 2020-10-07 [4,3] 85 [3] 4 [1] [3,1] [1,2]


* It may look lengthy or hard at first glance, but after a few tries it becomes second nature.
---
🗂️ **Project_Structures**
Library.sql              → Database schema + sample records
Library.db               → SQLite database file
LibraryDataAdapter.py    → Handles all SQL interactions
model.py                 → Python classes for each entity
main.py                  → CLI loop and command parsing
test.py                  → Quick sanity test

---

*Everything is separated clearly so that the system remains easy to extend later.*

* How It Works
* Data Models

model.py defines simple Python classes for each entity.
They mainly hold data and include a few equality methods to make comparisons convenient during lookups.

* Data Adapter Layer

Each DataAdapter handles:

fetching all entities

inserting new ones

deleting them when safe

It keeps SQL code out of the main program and makes the system easier to understand.

---
* Command Processor 

    * main.py runs an interactive loop:

    * Loads data from the database

    * Prints available commands

    * Waits for the user to type something

    * Parses and executes it

    * Validation uses simple regex rules for lists and date formats.
---
* Getting Started

1. Be ensure Python 3.10+ is installed
    * [link for download Python](https://www.python.org/)

2. Run the program with :

    - `python main.py`


* If the database hasn't been created yet, you can generate it by executing the SQL file or uncommenting the initialization code inside main.py.


---
**Final Thoughts**

This system was built with simplicity and clarity in mind.
It brings together different aspects of a real library database but keeps the project small enough to understand without drowning in complexity.
If you plan to expand it, the modular structure should make the process smooth and intuitive.