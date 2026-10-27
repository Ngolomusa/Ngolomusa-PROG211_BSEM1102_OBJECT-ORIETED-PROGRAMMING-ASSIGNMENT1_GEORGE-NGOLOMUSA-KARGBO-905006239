# Student Learning Portal

**PROG211 – Object-Oriented Programming 1**


A small Python program that manages students, courses and results using
object-oriented programming. It was built for the PROG211 individual assignment
and follows the Digital Public Goods (DPG) principles in the brief.

## Author

- **Name:** George N'GoloMusa Kargbo
- **Faculty:** F.I.C.T
- **Programme:** B.S.E.M
- **Class:** BSEM 1102
- **University:** Limkokwing University of Creative Technology (L.U.C.T)

## What the program does

- Creates `Student`, `Course` and `Result` objects.
- Registers students in a dictionary keyed by student ID.
- Displays student and course records.
- Calculates a letter grade from a score using a static method.
- Links each result to a student and a course to demonstrate object interaction.

## Project files

| File | Purpose |
| --- | --- |
| `oop.assignment1.py` | Main source code (classes, registry functions and demo) |
| `README.md` | Project documentation and DPG alignment |
| `Screenshots/` | Screenshots of the program running |

## How to run

1. Install Python 3.
2. Open a terminal in this folder.
3. Run:

   ```bash
   python oop.assignment1.py
   ```

No external packages are required.

## Assignment requirements covered

### Task 1 – OOP basics

| Class | Attributes | Methods |
| --- | --- | --- |
| `Student` | `student_id`, `level`, `faculty` (instance); `total_students`, `University` (class) | `display_info()` (instance), `get_total_students()` (class method) |
| `Course` | `course_id`, `course_name`, `credits` | `display_course()` (instance) |
| `Result` | `student`, `course`, `score`, `grade` | `display_result()` (instance), `calculate_grade()` (static) |

**Object creation and interaction:** objects are created in `main()`. Each
`Result` stores a reference to a `Student` object and a `Course` object, so
`display_result()` can read `self.student.student_id` and
`self.course.course_name`.

### Task 2 – Python data structure

The program uses **one dictionary** to store multiple objects:

```python
students = {}
```

- The key is `student.student_id` and the value is the `Student` object.
- `add_student(registry, student)` adds a record to the dictionary.
- `display_students(registry)` loops through the dictionary and displays every record.

**Optional tuple bonus:** `Result.GRADE_SCALE` is a tuple of
`(minimum, letter)` pairs. The tuple is used correctly by
`calculate_grade()` to look up grades. This is the optional tuple use
mentioned in the brief (extra marks).

### Task 3 – Methods

- **Instance methods:** `display_info()`, `display_course()`, `display_result()`
- **Class method:** `Student.get_total_students()` uses `cls` and returns `cls.total_students`
- **Static method:** `Result.calculate_grade(score)` does not use `self` or `cls`

## Grade scale

| Score range | Grade |
| --- | --- |
| 90 – 100 | A |
| 80 – 89 | B |
| 70 – 79 | C |
| 50 – 69 | D |
| 0 – 49 | F |

The scale is stored in `Result.GRADE_SCALE` and applied by
`Result.calculate_grade()`.

## Sample input

The demo in `main()` creates the following records.

**Students**

| Student ID | Level | Faculty |
| --- | --- | --- |
| 6789 | Year 2 | F.I.C.T - Software Engineering |
| 9800 | Year 1 | D.M.A.B - Photo Theory |
| 9090 | Year 3 | F.I.C.T - OOP |
| 6239 | Year 1 | B.A.B.J - Architectural Studies |

**Courses**

| Course ID | Course name | Credits |
| --- | --- | --- |
| 34 | Computer Systems | 3 |
| 17 | Software Engineering | 3 |
| 5 | Photo Theory | 3 |

**Results**

| Student ID | Course | Score |
| --- | --- | --- |
| 6789 | Computer Systems | 92 |
| 9800 | Software Engineering | 84 |
| 9090 | Photo Theory | 73 |
| 6239 | Computer Systems | 60 |
| 6789 | Software Engineering | 23 |

## Sample output

```text
===== STUDENT LEARNING PORTAL =====

--- Registered Students ---
STUDENT_ID: 6789 | LEVEL: Year 2 | FACULTY: F.I.C.T - Software Engineering | UNIVERSITY: Limkokwing University of Creative Technology
STUDENT_ID: 9800 | LEVEL: Year 1 | FACULTY: D.M.A.B - Photo Theory | UNIVERSITY: Limkokwing University of Creative Technology
STUDENT_ID: 9090 | LEVEL: Year 3 | FACULTY: F.I.C.T - OOP | UNIVERSITY: Limkokwing University of Creative Technology
STUDENT_ID: 6239 | LEVEL: Year 1 | FACULTY: B.A.B.J - Architectural Studies | UNIVERSITY: Limkokwing University of Creative Technology
Total students: 4

--- Courses Offered ---
COURSE_ID: 34 | COURSE_NAME: Computer Systems | CREDITS: 3
COURSE_ID: 17 | COURSE_NAME: Software Engineering | CREDITS: 3
COURSE_ID: 5 | COURSE_NAME: Photo Theory | CREDITS: 3

--- Results ---
Student: 6789 | Computer Systems | Score: 92 | Grade: A
Student: 9800 | Software Engineering | Score: 84 | Grade: B
Student: 9090 | Photo Theory | Score: 73 | Grade: C
Student: 6239 | Computer Systems | Score: 60 | Grade: D
Student: 6789 | Software Engineering | Score: 23 | Grade: F
```

## DPG standards alignment

### Open source

The complete Python source code is provided in this repository and is uploaded
to GitHub for review and reuse. It has no external dependencies, so anyone can
download and run it with a standard Python 3 installation.

### Inclusive and accessible

- Output is plain text with clear labels; no colour or images are needed to understand it.
- Records are read out one per line, which works well with screen readers.
- The program uses only the standard library and runs on any operating system with Python 3.

### Privacy-respecting

- Only non-sensitive academic data is stored: student ID, level, faculty, course, score and grade.
- No names, phone numbers, email addresses, home addresses, dates of birth, health data or financial data are collected.
- Records are displayed by student ID rather than by a person's name.

### Modular and reusable

- `Student`, `Course` and `Result` are independent classes that can be reused in another program.
- `add_student()` and `display_students()` accept any registry dictionary, so they are not tied to the demo data.
- The `main()` guard means importing the file does not run the demo.
