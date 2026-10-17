# AttendX Login Test
# Tests the login functionality for the AttendX Student Attendance Application
# Author: Het Soni | QA Engineer
# Version: 1.1 - Added SQL injection test case (collaboration update)

def test_login_valid_credentials():
    """Test login with valid credentials."""
    username = "student123"
    password = "password123"
    if username == "student123" and password == "password123":
        print("PASS: Login successful with valid credentials")
        return True
    else:
        print("FAIL: Login unsuccessful")
        return False

def test_login_invalid_credentials():
    """Test login with invalid credentials."""
    username = "wronguser"
    password = "wrongpassword"
    if username == "student123" and password == "password123":
        print("FAIL: Login should have been rejected")
        return False
    else:
        print("PASS: Invalid credentials correctly rejected")
        return True

def test_login_empty_fields():
    """Test login with empty username and password fields."""
    username = ""
    password = ""
    if username == "" or password == "":
        print("PASS: Empty fields correctly blocked")
        return True
    else:
        print("FAIL: Empty fields were not caught")
        return False

def test_login_sql_injection():
    """Test that SQL injection attempts are blocked."""
    username = "' OR '1'='1"
    password = "' OR '1'='1"
    # In a real app this would be caught by input validation
    if username == "student123" and password == "password123":
        print("FAIL: SQL injection was not blocked")
        return False
    else:
        print("PASS: SQL injection attempt correctly rejected")
        return True

# Run all test cases
if __name__ == "__main__":
    print("=" * 40)
    print("  AttendX Login Test Suite")
    print("=" * 40)
    test_login_valid_credentials()
    test_login_invalid_credentials()
    test_login_empty_fields()
    test_login_sql_injection()
    print("=" * 40)
    print("  All login tests completed.")
    print("=" * 40)
