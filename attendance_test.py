# AttendX Attendance Marking Test
# Tests the attendance marking functionality for the AttendX Student Attendance Application
# Author: Het Soni | QA Engineer
# Version: 1.0

# Simulated attendance database (empty at start)
attendance_records = {}

def mark_attendance(student_id, student_name, status="Present"):
    """Mark attendance for a given student."""
    if not student_id or not student_name:
        return False, "Student ID and name cannot be empty"
    attendance_records[student_id] = {
        "name": student_name,
        "status": status
    }
    return True, f"Attendance marked: {student_name} is {status}"

def test_mark_attendance_present():
    """Test marking a student as present."""
    success, message = mark_attendance("STU101", "Priya Sharma", "Present")
    if success and attendance_records.get("STU101", {}).get("status") == "Present":
        print("PASS:", message)
    else:
        print("FAIL: Could not mark student as Present")

def test_mark_attendance_absent():
    """Test marking a student as absent."""
    success, message = mark_attendance("STU102", "Ravi Kumar", "Absent")
    if success and attendance_records.get("STU102", {}).get("status") == "Absent":
        print("PASS:", message)
    else:
        print("FAIL: Could not mark student as Absent")

def test_mark_attendance_empty_id():
    """Test that empty student ID is rejected."""
    success, message = mark_attendance("", "Unknown Student")
    if not success:
        print("PASS: Empty student ID correctly rejected -", message)
    else:
        print("FAIL: Empty student ID was not caught")

def test_view_attendance_records():
    """Test viewing all attendance records."""
    if len(attendance_records) > 0:
        print("PASS: Attendance records retrieved successfully")
        for sid, data in attendance_records.items():
            print(f"  Student ID: {sid} | Name: {data['name']} | Status: {data['status']}")
    else:
        print("INFO: No records found yet")

# Run all test cases
if __name__ == "__main__":
    print("=" * 40)
    print("  AttendX Attendance Test Suite")
    print("=" * 40)
    test_mark_attendance_present()
    test_mark_attendance_absent()
    test_mark_attendance_empty_id()
    test_view_attendance_records()
    print("=" * 40)
    print("  All attendance tests completed.")
    print("=" * 40)
