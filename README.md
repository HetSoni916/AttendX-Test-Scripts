# AttendX-Test-Scripts

## Overview
This repository contains the QA test scripts for the **AttendX Student Attendance Application**. 
It was created to solve the problem of QA engineers sharing test scripts via email and pen drives, which caused files to be overwritten or lost.

By using Git and GitHub, the team can now:
- Track every change made to test scripts
- Work collaboratively without overwriting each other's work
- Revert to previous versions if something breaks

---

## Repository Structure

```
AttendX-Test-Scripts/
│
├── login_test.py         # Test cases for the login module
├── attendance_test.py    # Test cases for the attendance marking module
└── README.md             # Project documentation (this file)
```

---

## Test Scripts

### `login_test.py`
Tests the login functionality of the AttendX application.

| Test Case | Description | Expected Result |
|-----------|-------------|-----------------|
| `test_login_valid_credentials` | Login with correct username and password | PASS |
| `test_login_invalid_credentials` | Login with wrong credentials | PASS (rejected) |
| `test_login_empty_fields` | Login with empty fields | PASS (blocked) |

### `attendance_test.py`
Tests the attendance marking functionality of the AttendX application.

| Test Case | Description | Expected Result |
|-----------|-------------|-----------------|
| `test_mark_attendance_present` | Mark a student as Present | PASS |
| `test_mark_attendance_absent` | Mark a student as Absent | PASS |
| `test_mark_attendance_empty_id` | Attempt with empty student ID | PASS (rejected) |
| `test_view_attendance_records` | View all stored records | PASS |

---

## How to Run the Tests

Make sure you have Python installed. Then run:

```bash
python login_test.py
python attendance_test.py
```

---

## Team

| Name | Role |
|------|------|
| Het Soni | QA Engineer / Repository Owner |

---

## Version History
- **v1.0** - Initial commit: Added login and attendance test scripts
