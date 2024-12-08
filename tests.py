from ELS import * 
# Test Cases
def test_add_course():
    print("\nRunning Test Case 3: Add Course")
    course_id = "C999"
    course_name = "Test Course"
    if course_id in courses:
        del courses[course_id]  # Clean up if exists
    initial_course_count = len(courses)
    courses[course_id] = course_name
    final_course_count = len(courses)
    assert final_course_count == initial_course_count + 1, "Adding course failed"
    print("Test Case 3 Passed")

def test_enroll_course():
    print("\nRunning Test Case 4: Enroll Course")
    username = "test_student"
    course_id = "C001"
    users[username] = "password123"
    user_courses[username] = []  # Reset enrolled courses
    initial_enrollments = len(user_courses[username])
    enroll_course(username)
    final_enrollments = len(user_courses[username])
    assert final_enrollments == initial_enrollments + 1, "Course enrollment failed"
    print("Test Case 4 Passed")

def test_take_quiz():
    print("\nRunning Test Case 5: Take Quiz")
    username = "test_student"
    course_id = "C001"
    assessments[course_id] = [("Q1", "What is Python?")]
    user_courses[username] = [course_id]
    try:
        take_quiz(username)
        print("Test Case 5 Passed")
    except Exception as e:
        print(f"Test Case 5 Failed: {e}")

# Execute All Tests
if __name__ == "__main__":
    print("Running All Test Cases...\n")
    test_register_user()
    test_login_user()
    test_add_course()
    test_enroll_course()
    test_take_quiz()
    print("\nAll Test Cases Completed!")
